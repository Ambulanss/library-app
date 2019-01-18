
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
        1062: "Niektóre z wprowadzonych wartości się powtarzają!",
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

        _translate = QtCore.QCoreApplication.translate

        self.comboBox.currentTextChanged.connect(lambda: self.putDataIntoTableView(self.comboBox.currentText()))
        self.putDataIntoTableView(self.comboBox.currentText())
        self.putDataIntoTableView(self.comboBox.currentText())
        self.comboBox_2.currentTextChanged.connect(lambda: self.showTableParameters(self.comboBox_2.currentText()))
        self.showTableParameters(self.comboBox_2.currentText())
        self.deleteButton.released.connect(self.__deleteData)
        self.addButton.released.connect(self.__insertData)
        self.borrowButton.released.connect(self.__borrow)
        self.addUserButton.released.connect(self.__addUser)
        self.searchButton.released.connect(lambda: self.searchTable(self.comboBox_3, self.adminSearchLabels,
                                                                    self.adminSearchEdits, self.tableView_2))
        self.addingSearchButton.released.connect(lambda: self.searchTable(self.comboBox_7, self.addSearchLabels,
                                                                    self.addSearchEdits, self.tableView_3))
        self.borrowSearchButton.released.connect(lambda: self.searchTable(self.comboBox_8, self.borrowSearchLabels,
                                                                    self.borrowSearchEdits, self.tableView_4))
        self.registerSearchButton.released.connect(lambda: self.searchTable(self.comboBox_9, self.registerSearchLabels,
                                                                    self.registerSearchEdits, self.tableView_5))
        self.modelTab = QtSql.QSqlTableModel(db=self.conn)
        self.modelTab.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTab.dataChanged.connect(self.editHandle)
        self.tableView.setModel(self.modelTab)
        self.tableView.setSortingEnabled(True)
        self.adminSearchLabels, self.adminSearchEdits = [], []
        self.addSearchLabels, self.addSearchEdits = [], []
        self.borrowSearchLabels, self.borrowSearchEdits = [], []
        self.registerSearchLabels, self.registerSearchEdits = [], []
        self.comboBox_3.currentTextChanged.connect(lambda: self.showing(self.comboBox_3, self.horizontalLayout,
                                                                        self.adminSearchLabels, self.adminSearchEdits))
        self.comboBox_7.currentTextChanged.connect(lambda: self.showing(self.comboBox_7, self.addSearchLabelsLayout,
                                                                        self.addSearchLabels, self.addSearchEdits))
        self.comboBox_8.currentTextChanged.connect(lambda: self.showing(self.comboBox_8, self.borrowSearchLabelsLayout,
                                                                        self.borrowSearchLabels, self.borrowSearchEdits))
        self.comboBox_9.currentTextChanged.connect(lambda: self.showing(self.comboBox_9, self.registerSearchLabelsLayout,
                                                                        self.registerSearchLabels,
                                                                        self.registerSearchEdits))
        self.tabWidget.currentChanged.connect(lambda: self.putDataIntoTableView(self.comboBox.currentText()))
        self.tabWidget.currentChanged.connect(lambda: self.showTableParameters(self.comboBox_2.currentText()))


        self.borrowButton.released.connect(self.__borrow)
        self.returnButton.released.connect(self.__return)

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

    def searchTable(self, comboBox, searchLabels, searchEdits, tableView):
        tablename = comboBox.currentText()
        argnames = []
        args = []
        print(len(searchLabels))

        for i in range(len(searchLabels)):
            if len(searchEdits[i].text()) > 0:
                args.append(searchEdits[i].text())
                argnames.append(searchLabels[i].text())
        query = QtSql.QSqlQuery(self.conn)
        if args:
            args = self.textTr.wrapStringsWith(args, "'")
            parsed_args = [argnames[i] + "=" + args[i] for i in range(len(args))]
            parsed_args = self.textTr.listToCommaStr(parsed_args, False)
            print(parsed_args)

            sql = "SELECT * FROM " + tablename + " WHERE " + parsed_args
        else:
            sql = "SELECT * FROM " + tablename
        projectModel = QtSql.QSqlQueryModel()
        projectModel.setQuery(sql, self.conn)
        print(sql)
        query.exec_(sql)
        tableView.setModel(projectModel)
        tableView.show()

    def showing(self, comboBox, horizontalLayout, searchLabels, searchEdits):
        name = comboBox.currentText()
        query = QtSql.QSqlQuery(self.conn)
        query.exec_("SELECT * FROM " + name)
        x = query.record().count()
        for i in range(horizontalLayout.count()):
            horizontalLayout.itemAt(i).widget().close()
        names = [query.record().fieldName(i) for i in range(x)]
        types = [self.fieldTypeDict.get(query.record().field(i).type(), "") for i in range(x)]
        searchLabels, searchEdits = [], []

        for i in range(x):
            searchLabels.append(QtWidgets.QLabel(names[i]))
            searchEdits.append(QtWidgets.QLineEdit())
            horizontalLayout.addWidget(searchLabels[-1])
            horizontalLayout.addWidget(searchEdits[-1])

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

        for i in range(x):
            self.addDelLabels.append(QtWidgets.QLabel(names[i]))
            self.addDelLineEdits.append(QtWidgets.QComboBox())
            options_query = QtSql.QSqlQuery(db=self.conn, query="SELECT DISTINCT " + names[i] + " FROM " + name)
            self.addDelLineEdits[-1].setEditable(True)
            if types[i] == "Ciąg znaków":
                while options_query.next():
                    self.addDelLineEdits[-1].addItem(str(options_query.value(0)))
            if types[i] == "Data w formacie YYYY-MM-DD":
                self.addDelLineEdits[-1].setCurrentText("YYYY-MM-DD")
            self.addDelLineEdits[-1].setToolTip(types[i])
            self.formLayout.addRow(self.addDelLabels[i], self.addDelLineEdits[i])

    def checkBook(self):
        query = QtSql.QSqlQuery(self.conn)
        sql = "SELECT czy_wypozyczony(" + self.lineEdit_2_1.text().strip() + ")"
        try:
            query.exec_(sql)
        except:
            self.showError(query.lastError())
        QMessageBox.information(None, "Informacja", "Egzemplarz " +
                                ("wypożyczony" if query.value(1) else "nie jest wypożyczony lub nie istnieje"))


    def __getFieldsFromUI(self):
        fieldNames = []
        args = []
        for i in range(len(self.addDelLabels)):
            if len(self.addDelLineEdits[i].currentText()) > 0:
                fieldNames.append(self.addDelLabels[i].text())
                args.append(self.addDelLineEdits[i].currentText())
        return fieldNames, args

    def __insertData(self):
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
            QMessageBox.critical(None, "Błąd", "Wypełnij pola!")

    def __deleteData(self):

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
            QMessageBox.critical(None, "Błąd", "Wypełnij pola!")

    def __borrow(self):
        query = QtSql.QSqlQuery()
        pesel = self.borrowEdit.text()
        number = self.borrowEdit_1.text()
        time = self.borrowEdit_2.text()
        if pesel == "":
            QMessageBox.critical(None, "Błąd!", "Wypełnij pole pesel")
            return
        if number == "":
            QMessageBox.critical(None, "Błąd!", "Wypełnij pole Numer egzemplarza")
            return
        if time == "":
            QMessageBox.critical(None, "Błąd!", "Wypełnij pole Dni na oddanie")
            return
        sql = "CALL borrow_book(" + pesel + ", " + number + ", " + time + ")"
        query.exec_(sql)

        if query.lastError().isValid():
            self.showError(query.lastError())
            return
        QMessageBox.information(self, "Sukces!", "Dodano wypożyczenie!")


    def __return(self):
        number = self.returnEdit.text()
        if number == "":
            QMessageBox.critical(None, "Błąd!", "Wypełnij pole Numer egzemplarza")
            return
        query = QtSql.QSqlQuery(self.conn)
        sql = "SELECT * FROM Wypożyczenie WHERE rzeczywista_data_oddania = NULL and egzemplarz_id_egzemplarza = "\
              + number
        query.exec_(sql)
        helpQuery = QtSql.QSqlQuery(self.conn)
        if(query.next()):
            helpQuery.exec_("UPDATE Wypożyczenie SET rzeczywista_data_oddania = CURDATE() "
                            "WHERE rzeczywista_data_oddania = NULL and egzemplarz_id_egzemplarza = " + number)
        if query.lastError().isValid():
            QMessageBox.critical(None, "Błąd!", query.lastError().text())


    def __addUser(self):
        query = QtSql.QSqlQuery(self.conn)
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
            bar = self.textTr.listToCommaStr(bar, True)
            sql = "CALL add_user(" + bar + ")"
            query.exec_(sql)
            if query.lastError().isValid():
                self.showError(query.lastError())
            else:
                QMessageBox.information(None, "Sukces!", "Pomyślnie dodano użytkownika!")
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

