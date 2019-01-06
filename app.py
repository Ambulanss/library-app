
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox
import atexit

class App(object):

    def __init__(self, Form):
        self.getDB()
        print("gotDB")
        print("setupUi")
        self.setupUi(Form)
        print("setupUi finished")


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())

        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))

        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(10, 30, 761, 511))
        self.tableView.setObjectName("tableView")

        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 0, 141, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)

        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentTextChanged.connect(lambda: self.putDataIntoTableView(self.comboBox.currentText()))
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(232, 0, 531, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(166, 0, 61, 21))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 391, 481))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        #formLayout_2 - formLayout for getting args to add or remove rows
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_2.setGeometry(QtCore.QRect(19, 49, 381, 461))
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(412, 75, 43, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")

        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(475, 75, 200, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.currentTextChanged.connect(lambda: self.showTableParameters(self.comboBox_2.currentText()))
        for i in range(16):
            self.comboBox.addItem("")
            self.comboBox_2.addItem("")

        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(410, 10, 351, 60))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.deleteButton = QtWidgets.QPushButton(self.widget)
        self.deleteButton.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.deleteButton)
        self.deleteButton.released.connect(self.deleteData)

        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.searchButton)

        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.addButton)
        self.addButton.released.connect(self.insertData)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Biblioteka"))

        icon = QtGui.QIcon("books.png")
        Form.setWindowIcon(icon)

        itemTexts = ["autor", "autorstwo_dziela", "dzial", "dzielo", "egzemplarz", "filia",\
                     "filie_egzemplarze", "filie_uzytkownicy", "gatunek",\
                     "przynaleznosc_do_filii", "przynaleznosc_do_gatunku", "rezerwacja", "spoznialscy",\
                     "uzytkownicy_wypozyczenia", "uzytkownik", "wypozyczenie"]
        for i in range(len(itemTexts)):
            self.comboBox.setItemText(i, _translate("Form", itemTexts[i]))

        self.label.setText(_translate("Form", "Wyszukaj"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Baza"))
        self.label_2.setText(_translate("Form", "Tabela:"))

        for i in range(len(itemTexts)):
            self.comboBox_2.setItemText(i, _translate("Form", itemTexts[i]))

        self.deleteButton.setText(_translate("Form", "Usuń"))
        self.searchButton.setText(_translate("Form", "Szukaj"))
        self.addButton.setText(_translate("Form", "Dodaj"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Modyfikacja"))

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
        query = QtSql.QSqlQueryModel()
        query.setQuery("SELECT * FROM " + tableName, self.conn)
        self.tableView.setModel(query)

    def showTableParameters(self, name: str):
        query = QtSql.QSqlQuery(self.conn)
        query.exec_("SELECT * FROM " + name)
        x = query.record().count()
        names = [query.record().fieldName(i) for i in range(x)]

        for i in reversed(range(self.formLayout_2.rowCount())):
            self.formLayout_2.removeRow(i)
        self.addDelLabels = []
        self.addDelLineEdits = []
        for i in range(x):
            self.addDelLabels.append(QtWidgets.QLabel(names[i]))
            self.addDelLineEdits.append(QtWidgets.QLineEdit())
            self.formLayout_2.addRow(self.addDelLabels[i], self.addDelLineEdits[i])

    def __listToCommaStr(self, list, funny: bool):
        output = ""
        if funny:
            list = self.__wrapStringsWith(list, "'")
        for i in list[:-1]:
            output += i + ", "
        output += list[-1]
        return output

    def __getFieldsFromUI(self):
        fieldNames = []
        args = []
        for i in range(len(self.addDelLabels)):
            if len(self.addDelLineEdits[i].text()) > 0:
                fieldNames.append(self.addDelLabels[i].text())
                args.append(self.addDelLineEdits[i].text())
        return fieldNames, args

    def insertData(self):
        fieldNames, args = self.__getFieldsFromUI()
        tabFields = self.__listToCommaStr(fieldNames, False)
        values = self.__listToCommaStr(args, True)
        query = QtSql.QSqlQuery(self.conn)
        tableName = self.comboBox_2.currentText()
        try:
            print(tableName)
            print(tabFields)
            print(values)
            print("INSERT INTO " + tableName + "(" + tabFields + ")"
                 "VALUES (" + values + ")")
            query.exec_("INSERT INTO " + tableName + "(" + tabFields + ")"
                        "VALUES (" + values + ")")
        except QtSql.QSqlError:
            print("SqlError occured :(")

    def __wrapStringsWith(self, strList, char):
        result = []
        for i in strList:
            result.append(char + i + char)
        return result

    def deleteData(self):
        fieldNames, args = self.__getFieldsFromUI()
        args = self.__wrapStringsWith(args, "'")
        tableName = self.comboBox_2.currentText()
        query = QtSql.QSqlQuery(self.conn)
        conditions = []
        for i in range(len(fieldNames)):
            conditions.append(fieldNames[i]+"="+str(args[i]))
        print(conditions)
        sql = "DELETE FROM " + tableName + " WHERE " + self.__listToCommaStr(conditions, False)
        print(sql)
        query.exec_(sql)


    def closeConnection(self):
        self.conn.close()
        print("Is conn open? " + str(self.conn.isOpen()))
        self.conn.removeDatabase("biblioteka")
        print("Connection closed")

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

