
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox
import atexit
from UI.main import Ui_Form


class TextTransformer():
    def __init__(self):
        pass

    def listToCommaStr(self, list, funny: bool):
        output = ""
        if funny:
            list = self.wrapStringsWith(list, "'")
        for i in list[:-1]:
            output += i + ", "
        output += list[-1]
        return output

    def wrapStringsWith(self, strList, char):
        result = []
        for i in strList:
            result.append(char + i + char)
        return result


class App(Ui_Form):

    errorDict = {
        -1: "Coś się stało",
        -5:   "Nie podałeś żadnych argumentów",
        1062: "Wprowadzona wartość klucza głównego jest nieunikatowa",
        1064:   "",
        1364: "Nie wypełniłeś pól obowiązkowych",
        1366: "Niewłaściwy typ argumentu",
        1452: "Jedno z pól obowiązkowych nie ma odpowiednika w tabeli docelowej.\n Np. nie ma użytkownika o podanym peselu.",
        4025: "Niespełnione ograniczenie"
    }

    fieldTypeDict = {
        2: "Liczba naturalna",
        6: "Liczba rzeczywista",
        10: "Ciąg znaków",
        14: "Data w formacie YYYY-MM-DD"
    }

    modelTab = QtSql.QSqlTableModel()

    def __init__(self, Form):
        self.getDB()
        print("gotDB")
        self.textTr = TextTransformer()
        print("setupUi")
        self.setupUi(Form)
        print("setupUi finished")
        self.setupWidgets()

    def setupWidgets(self):
        itemTexts = ["autor", "autorstwo_dziela", "dzial", "dzielo", "egzemplarz", "filia",
                     "filie_egzemplarze", "filie_uzytkownicy", "gatunek",
                     "przynaleznosc_do_filii", "przynaleznosc_do_gatunku", "rezerwacja", "spoznialscy",
                     "uzytkownicy_wypozyczenia", "uzytkownik", "wypozyczenie"]
        for i in range(16):
            self.comboBox.addItem("")
            self.comboBox_2.addItem("")

        _translate = QtCore.QCoreApplication.translate
        for i in range(len(itemTexts)):
            self.comboBox.setItemText(i, _translate("Form", itemTexts[i]))

        for i in range(len(itemTexts)):
            self.comboBox_2.setItemText(i, _translate("Form", itemTexts[i]))

        self.comboBox_2.removeItem(self.comboBox_2.findText("spoznialscy"))
        self.comboBox_2.removeItem(self.comboBox_2.findText("uzytkownicy_wypozyczenia"))
        self.comboBox.currentTextChanged.connect(lambda: self.putDataIntoTableView(self.comboBox.currentText()))
        self.putDataIntoTableView(self.comboBox.currentText())
        self.putDataIntoTableView(self.comboBox.currentText())
        self.comboBox_2.currentTextChanged.connect(lambda: self.showTableParameters(self.comboBox_2.currentText()))
        self.showTableParameters(self.comboBox_2.currentText())
        self.deleteButton.released.connect(self.deleteData)
        self.addButton.released.connect(self.insertData)
        self.borrowButton.released.connect(self.borrow)
        self.addUserButton.released.connect(self.addUser)

        self.modelTab = QtSql.QSqlTableModel(db=self.conn)
        self.modelTab.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTab.dataChanged.connect(self.editHandle)
        self.tableView.setModel(self.modelTab)
        self.comboBox.currentTextChanged.connect(self.showing)
        self.searchLabels, self.searchEdits = [], []


    def getDB(self):
        self.conn = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.conn.setHostName("localhost")
        self.conn.setDatabaseName("biblioteka")
        self.conn.setUserName("root")
        self.conn.setPassword("longlivefoss")

        if not self.conn.open():
            QMessageBox.critical(None, "ERROR", "Cannot open database\n", QMessageBox.Ok)
            sys.exit(self.exec_())

    def putDataIntoTableView(self, tableName):

        self.modelTab.setTable(tableName)
        self.modelTab.select()

    def editHandle(self):
        self.modelTab.submitAll()
        self.modelTab.select()
        if self.modelTab.lastError().isValid():
            self.showError(self.modelTab.lastError())

    def showing(self):
        name = self.comboBox.currentText()
        query = QtSql.QSqlQuery(self.conn)
        query.exec_("SELECT * FROM " + name)
        count = len(self.searchLabels)
        x = query.record().count()
        for i in range(self.horizontalLayout.count()):
            self.horizontalLayout.itemAt(i).widget().close()
        names = [query.record().fieldName(i) for i in range(x)]
        types = [self.fieldTypeDict[query.record().field(i).type()] for i in range(x)]
        self.searchLabels, self.searchEdits = [], []

        for i in range(x):
            self.searchLabels.append(QtWidgets.QLabel(names[i]))
            self.searchEdits.append(QtWidgets.QLineEdit())
            self.horizontalLayout.addWidget(self.searchLabels[-1])
            self.horizontalLayout.addWidget(self.searchEdits[-1])


    def searchTableView(self, value):
        model = self.tableView.model()
        self.tableView.clearSelection()
        for i in range(model.columnCount()):
            start = model.index(0, i)
            matches = model.match(start, QtCore.Qt.DisplayRole, value, -1,  QtCore.Qt.MatchContains)
            for i in matches:
                index = i
                self.tableView.selectionModel().select(index, QtCore.QItemSelectionModel.Select)

    def showTableParameters(self, name: str):
        query = QtSql.QSqlQuery(self.conn)
        query.exec_("SELECT * FROM " + name)
        x = query.record().count()
        names = [query.record().fieldName(i) for i in range(x)]
        types = [self.fieldTypeDict[query.record().field(i).type()] for i in range(x)]
        for i in reversed(range(self.formLayout.rowCount())):
            self.formLayout.removeRow(i)
        self.addDelLabels = []
        self.addDelLineEdits = []
        #TODO getPrimaryKeys()
        #keys = [query.record().field().is]

        for i in range(x):
            self.addDelLabels.append(QtWidgets.QLabel(names[i]))
            self.addDelLineEdits.append(QtWidgets.QComboBox())
            options_query = QtSql.QSqlQuery(db=self.conn, query="SELECT DISTINCT " + names[i] + " FROM " + name)
            self.addDelLineEdits[-1].setEditable(True)
            if types[i] == "Ciąg znaków":
                while options_query.next():
                    self.addDelLineEdits[-1].addItem(str(options_query.value(0)))
            #TODO self.addDelLineEdits[-1].setInputMask("X")
            self.addDelLineEdits[-1].setToolTip(types[i])
            self.formLayout.addRow(self.addDelLabels[i], self.addDelLineEdits[i])


    def __getFieldsFromUI(self):
        fieldNames = []
        args = []
        for i in range(len(self.addDelLabels)):
            if len(self.addDelLineEdits[i].currentText()) > 0:
                fieldNames.append(self.addDelLabels[i].text())
                args.append(self.addDelLineEdits[i].currentText())
        return fieldNames, args

    def insertData(self):
        fieldNames, args = self.__getFieldsFromUI()
        if args:
            tabFields = self.textTr.listToCommaStr(fieldNames, False)
            values = self.textTr.listToCommaStr(args, True)
            query = QtSql.QSqlQuery(self.conn)
            tableName = self.comboBox_2.currentText()

            query.exec_("INSERT INTO " + tableName + "(" + tabFields + ")"
                        "VALUES (" + values + ")")
            if query.lastError().isValid():
                s = query.lastError().text()
                print("ERROR: ", s)
                self.showError(query.lastError())
        else:
            self.showError(-5)

    def deleteData(self):

        fieldNames, args = self.__getFieldsFromUI()
        if args:
            args = self.textTr.wrapStringsWith(args, "'")
            tableName = self.comboBox_2.currentText()
            query = QtSql.QSqlQuery(self.conn)
            conditions = []
            for i in range(len(fieldNames)):
                conditions.append(fieldNames[i]+"="+str(args[i]))
            print(conditions)
            sql = "DELETE FROM " + tableName + " WHERE " + self.textTr.listToCommaStr(conditions, False)
            print(sql)
            query.exec_(sql)
            if query.lastError().isValid():
                self.showError(query.lastError())
                print(query.lastError().text())
        else:
            self.showError(-5)

    def borrow(self):
        query = QtSql.QSqlQuery()
        pesel = self.lineEdit_0_1.text()
        number = self.spinBox.text()
        time = self.spinBox_2.text()
        sql = "CALL borrow_book(" + pesel + ", " + number + ", " + time + ")"
        query.exec_(sql)
        if query.lastError().isValid():
            self.showError(query.lastError())

    def addUser(self):
        query = QtSql.QSqlQuery()
        args = [self.lineEdit_1_1, self.lineEdit_1_2, self.lineEdit_1_3,
                self.lineEdit_1_4, self.lineEdit_1_5, self.lineEdit_1_6,
                self.lineEdit_1_7, self.lineEdit_1_8, self.lineEdit_1_9,
                self.lineEdit_1_10]
        text_ = QtWidgets.QLineEdit.text
        foo = []
        for i in args:
            if len(text_(i)) > 0:
                foo.append(text_(i))
            else:
                foo = []
                break
        if len(foo):
            bar = []
            for i in foo:
                bar.append(i)
            bar = self.textTr.listToCommaStr(list, True)
            sql = "CALL add_user(" + bar + ")"
            query.exec_(sql)
            if query.lastError().isValid():
                self.showError(query.lastError())
        else:
            self.showError(query.lastError())



    def closeConnection(self):
        self.conn.close()
        print("Is conn open? " + str(self.conn.isOpen()))
        self.conn.removeDatabase("biblioteka")
        print("Connection closed")

    def showError(self, error):
        QMessageBox.critical(self.tabWidget, "Błąd nr " + str(error.number()), self.errorDict.get(error.number(),\
                             "Niezdefiniowany błąd"), QMessageBox.Ok)
        print(error.text())


def main():
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()

    Form.setWindowModality(QtCore.Qt.ApplicationModal)
    ui = App(Form)
    Form.show()
    atexit.register(ui.closeConnection)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

