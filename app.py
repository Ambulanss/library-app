
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox
import atexit
from UI.main import Ui_Form


class TextTransformer:

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
            if i.isdigit():
                result.append(i)
            else:
                result.append(char + i + char)
        return result

class MyRegexs:

    varchar64 = QRegExpValidator(QRegExp(r"^[a-zA-Z0-9_ ]*$"))
    decimal72 = QRegExpValidator(QRegExp(r"^[1-9][0-9]{1,4}\.[0-9]{2}$"))
    int10unsigned = QRegExpValidator(QRegExp(r"[0-9]{10}"))
    decimal82 = QRegExpValidator(QRegExp(r"^[1-9][0-9]{1,5}\.[0-9]{2}$"))
    year4 = QRegExpValidator(QRegExp(r"^[1-9][0-9]{3}"))
    search_bar = QRegExpValidator(QRegExp(r"^[a-zA-Z0-9_\- ]*$"))

    def __init__(self):
        pass


class App(Ui_Form):

    errorDict = {
        -1: "Coś się stało",
        -5:   "Nie podałeś żadnych argumentów",
        1062: "Niektóre z wprowadzonych wartości się powtarzają!",
        #1064:   "",
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

    colNamesDict = {
        "Numer egzemplarza": "`Numer egzemplarza`"
    }

    modelTab = QtSql.QSqlTableModel()
    registerTab = QtSql.QSqlTableModel()
    borrowTab = QtSql.QSqlTableModel()
    addingTab = QtSql.QSqlTableModel()
    adminTab = QtSql.QSqlTableModel()

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
        self.adminSearchLabels, self.adminSearchEdits = [], []
        self.addSearchLabels, self.addSearchEdits = [], []
        self.borrowSearchLabels, self.borrowSearchEdits = [], []
        self.registerSearchLabels, self.registerSearchEdits = [], []
        self.searchButton.released.connect(lambda: self.searchTable(self.comboBox_3, self.adminSearchLabels,
                                                                    self.adminSearchEdits, self.tableView_2, self.adminTab))
        self.addingSearchButton.released.connect(lambda: self.searchTable(self.comboBox_7, self.addSearchLabels,
                                                                    self.addSearchEdits, self.tableView_3, self.addingTab))
        self.borrowSearchButton.released.connect(lambda: self.searchTable(self.comboBox_8, self.borrowSearchLabels,
                                                                    self.borrowSearchEdits, self.tableView_4, self.borrowTab))
        self.registerSearchButton.released.connect(lambda: self.searchTable(self.comboBox_9, self.registerSearchLabels,
                                                                    self.registerSearchEdits, self.tableView_5, self.registerTab))
        # MODELS AND TABLES
        self.modelTab = QtSql.QSqlTableModel(db=self.conn)
        self.registerTab = QtSql.QSqlTableModel(db=self.conn)
        self.addingTab = QtSql.QSqlTableModel(db=self.conn)
        self.borrowTab = QtSql.QSqlTableModel(db=self.conn)
        self.adminTab = QtSql.QSqlTableModel(db=self.conn)
        self.modelTab.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTab.dataChanged.connect(lambda: self.editHandle(self.modelTab))
        self.tableView.setModel(self.modelTab)
        self.tableView.setSortingEnabled(True)

        self.tableView_5.setModel(self.registerTab)
        self.tableView_5.setSortingEnabled(True)

        self.tableView_2.setModel(self.adminTab)
        self.tableView_2.setSortingEnabled(True)
        self.tableView_3.setModel(self.addingTab)
        self.tableView_3.setSortingEnabled(True)
        self.tableView_4.setModel(self.adminTab)
        self.tableView_4.setSortingEnabled(True)

        self.comboBox_7.currentTextChanged.connect(lambda: self.showing(self.comboBox_7, self.addSearchLabelsLayout,
                                                                        self.addSearchLabels, self.addSearchEdits))
        self.comboBox_8.currentTextChanged.connect(lambda: self.showing(self.comboBox_8, self.borrowSearchLabelsLayout,
                                                                        self.borrowSearchLabels, self.borrowSearchEdits))
        self.comboBox_9.currentTextChanged.connect(lambda: self.showing(self.comboBox_9, self.registerSearchLabelsLayout,
                                                                        self.registerSearchLabels,
                                                                        self.registerSearchEdits))
        self.tabWidget.currentChanged.connect(lambda: self.putDataIntoTableView(self.comboBox.currentText()))
        self.tabWidget.currentChanged.connect(lambda: self.showTableParameters(self.comboBox_2.currentText()))
        self.tabWidget.currentChanged.connect(lambda: self.showing(self.comboBox_3, self.horizontalLayout,
                                                                self.adminSearchLabels, self.adminSearchEdits))
        self.tabWidget.currentChanged.connect(lambda: self.showing(self.comboBox_7, self.addSearchLabelsLayout,
                                                                        self.addSearchLabels, self.addSearchEdits))
        self.tabWidget.currentChanged.connect(lambda: self.showing(self.comboBox_8, self.borrowSearchLabelsLayout,
                                                                        self.borrowSearchLabels,
                                                                        self.borrowSearchEdits))
        self.tabWidget.currentChanged.connect(
            lambda: self.showing(self.comboBox_9, self.registerSearchLabelsLayout,
                                 self.registerSearchLabels,
                                 self.registerSearchEdits))
        # show tables correctly when tab is changed
        self.tabWidget.currentChanged.connect(lambda: self.searchTable(self.comboBox_3, self.adminSearchLabels,
                                                                    self.adminSearchEdits, self.tableView_2, self.adminTab))
        self.tabWidget.currentChanged.connect(lambda: self.searchTable(self.comboBox_7, self.addSearchLabels,
                                                                          self.addSearchEdits, self.tableView_3, self.addingTab))
        self.tabWidget.currentChanged.connect(lambda: self.searchTable(self.comboBox_8, self.borrowSearchLabels,
                                                                          self.borrowSearchEdits, self.tableView_4, self.borrowTab))
        self.tabWidget.currentChanged.connect(lambda: self.searchTable(self.comboBox_9, self.registerSearchLabels,
                                                                            self.registerSearchEdits, self.tableView_5, self.registerTab))
        #show tables correctly when user changes table
        self.comboBox_3.currentTextChanged.connect(lambda: self.searchTable(self.comboBox_3, self.adminSearchLabels,
                                                                    self.adminSearchEdits, self.tableView_2, self.adminTab))
        self.comboBox_7.currentTextChanged.connect(lambda: self.searchTable(self.comboBox_7, self.addSearchLabels,
                                                                          self.addSearchEdits, self.tableView_3, self.addingTab))
        self.comboBox_8.currentTextChanged.connect(lambda: self.searchTable(self.comboBox_8, self.borrowSearchLabels,
                                                                          self.borrowSearchEdits, self.tableView_4, self.borrowTab))
        self.comboBox_9.currentTextChanged.connect(lambda: self.searchTable(self.comboBox_9, self.registerSearchLabels,
                                                                            self.registerSearchEdits, self.tableView_5, self.registerTab))
        self.returnButton.released.connect(self.__return)
        self.reserveButton.released.connect(self.reservation)
        self.addButton_2.released.connect(self.addBook)
        self.searchTable(self.comboBox_9, self.registerSearchLabels, self.registerSearchEdits, self.tableView_5, self.registerTab)

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

    def editHandle(self, model):
        model.submitAll()
        model.select()
        if model.lastError().isValid():
            self.showError(model.lastError())

    def searchTable(self, comboBox, searchLabels, searchEdits, tableView, projectModel):
        tablename = comboBox.currentText()
        argnames = []
        args = []
        print(len(searchLabels))
        for i in range(len(searchLabels)):
            if len(searchEdits[i].text()) > 0:
                args.append(searchEdits[i].text())
                argnames.append(self.colNamesDict.get(searchLabels[i].text(), searchLabels[i].text()))
        filter = None
        if args:
            args = self.textTr.wrapStringsWith(args, "'")
            parsed_args = [argnames[i] + "=" + args[i] for i in range(len(args))]
            parsed_args = self.textTr.listToCommaStr(parsed_args, False)
            print(parsed_args)

            sql = "SELECT * FROM " + tablename + " WHERE " + parsed_args
            filter = parsed_args
        else:
            sql = "SELECT * FROM " + tablename

        projectModel.setTable(tablename)
        if filter != None:
            projectModel.setFilter(filter)
        projectModel.select()

        #tableView.show()

    def addBook(self):
        title = self.lineEdit_2.text()
        authorname = self.lineEdit_3.text()
        authorsurname = self.lineEdit_4.text()
        filia = self.lineEdit.text()
        dzial = self.comboBox_6.currentText()
        type = self.comboBox_4.currentText()
        message = ""
        mistake = 0
        id_autora = -1
        if title == "":
            mistake += 1
            message += "Tytuł\n"
        if authorname == "":
            mistake += 1
            message += "Imię autora\n"
        if authorsurname == "":
            mistake += 1
            message += "Nazwisko autora\n"
        if filia == "":
            mistake += 1
            message += "Numer filii\n"
        if dzial == "":
            mistake += 1
            message += "Dział"
        if mistake > 0:
            QMessageBox.information(None, "Błąd!", "Uzupełnij następujące pola:\n " + message)
            return
        checkQuery = QtSql.QSqlQuery(self.conn)
        checkQuery.exec_("SELECT * from Filia where numer = '" + str(filia) + "'")
        if checkQuery.next():
            pass
        else:
            QMessageBox.critical(None, "Błąd!", "Nie ma filii o podanym numerze!")
            return
        checkAuthorSql = "SELECT id_autora FROM Autor WHERE imie like '" + authorname + "' and nazwisko like '" + authorsurname + "'"
        checkQuery.exec_(checkAuthorSql)
        if checkQuery.next():
            id_autora = checkQuery.value(0)
            print("DEBUG autor: ", id_autora)
        else:
            print(authorname, authorsurname)
            id_autora = self.addAuthor(authorname, authorsurname)
        print("Id autora: ", id_autora)
        checkQuery.exec_("SELECT id_dziela from Dzieło where tytul =  '" + title + "'")
        if checkQuery.next():
            pass
        else:
            checkQuery.exec_("INSERT IGNORE INTO Dzieło(tytul, typ) VALUES('" + title + "', '" + type + "')")
        checkQuery.exec_("SELECT id_dziela from Dzieło where tytul =  '" + title + "'")
        checkQuery.next()
        id_dziela = checkQuery.value(0)
        print("Id dzieła: ", id_dziela)
        checkQuery.exec_("INSERT IGNORE INTO Dział VALUES('" + dzial + "', ' " + filia + "')")
        values = [str(id_dziela), type, filia, dzial]
        foo = self.textTr.listToCommaStr(values, True)
        sql = "INSERT INTO Egzemplarz(dzielo_id_dziela, dzielo_typ, dzial_filia_numer, dzial_nazwa) VALUES(" + foo + ")"
        print(sql)
        checkQuery.exec_(sql)
        checkQuery.exec_("INSERT IGNORE INTO Autorstwo_dzieła VALUES(" + str(id_dziela) + ", " + str(id_autora) + ")")

        if checkQuery.lastError().isValid():
            print(checkQuery.lastError().text())



    def addAuthor(self, name, surname):
        query = QtSql.QSqlQuery(self.conn)
        query.exec_("INSERT INTO Autor(imie, nazwisko)"
                    "VALUES ('" + name + "', '" + surname + "')")

        query.exec_("SELECT id_autora FROM Autor where imie like '" + name + "' and nazwisko like '" + surname +"'")
        query.next()
        return query.value(0)

    def reservation(self):

        pesel = self.lineEdit_9.text()
        number = self.lineEdit_10.text()
        days = self.lineEdit_11.value()
        if pesel == "":
            QMessageBox.information(None, "Błąd!", "Uzupełnij pesel!")
            return
        if number == "":
            QMessageBox.information(None, "Błąd!", "Uzupełnij numer egzemplarza!")
            return
        if not number.isdigit():
            QMessageBox.information(None, "Błąd!", "Numer egzemplarza to liczba!")
            return
        if days == "":
            QMessageBox.information(None, "Błąd!", "Uzupełnij liczbę dni do upłynięcia rezerwacji!")
            return

        query = QtSql.QSqlQuery(self.conn)
        sql = "INSERT INTO Rezerwacja VALUES( CURDATE(), ADDDATE(CURDATE(), " + str(days) + "), '" + pesel + "', '" + number + "', 'AKTYWNA')"
        print(sql)
        query.exec_(sql)
        if query.lastError().isValid():
            QMessageBox.critical(None, "Błąd!", query.lastError().text())
        else:
            QMessageBox.information(None, "Sukces!", "Pomyślnie dodano rezerwację!")


    def showing(self, comboBox, horizontalLayout, searchLabels, searchEdits):
        name = comboBox.currentText()
        query = QtSql.QSqlQuery(self.conn)
        query.exec_("SELECT * FROM " + name)
        x = query.record().count()
        for i in range(horizontalLayout.count()):
            horizontalLayout.itemAt(i).widget().close()
        names = [query.record().fieldName(i) for i in range(x)]
        types = [self.fieldTypeDict.get(query.record().field(i).type(), "") for i in range(x)]
        searchLabels.clear()
        searchEdits.clear()
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
        time = self.borrowEdit_2.value()
        if pesel == "":
            QMessageBox.critical(None, "Błąd!", "Wypełnij pole pesel")
            return
        if number == "":
            QMessageBox.critical(None, "Błąd!", "Wypełnij pole Numer egzemplarza")
            return
        if time == "":
            QMessageBox.critical(None, "Błąd!", "Wypełnij pole Dni na oddanie")
            return
        sql = "CALL borrow_book('" + pesel + "', " + number + ", " + str(time) + ")"
        query.exec_(sql)

        if query.lastError().isValid():
            self.showError(query.lastError())
            return
        QMessageBox.information(None, "Sukces!", "Dodano wypożyczenie!")


    def __return(self):
        number = self.returnEdit.text()
        if number == "":
            QMessageBox.critical(None, "Błąd!", "Wypełnij pole Numer egzemplarza")
            return
        if not number.isdigit():
            QMessageBox.critical(None, "Błąd!", "Pole numer egzemplarza musi zawierać tylko numer!")
            return
        query = QtSql.QSqlQuery(self.conn)
        sql = "SELECT * FROM Wypożyczenie WHERE rzeczywista_data_oddania IS NULL and egzemplarz_id_egzemplarza = "\
              + number
        print(sql)
        query.exec_(sql)
        helpQuery = QtSql.QSqlQuery(self.conn)
        if(query.next()):
            helpQuery.exec_("UPDATE Wypożyczenie SET rzeczywista_data_oddania = CURDATE() "
                            "WHERE rzeczywista_data_oddania IS NULL and egzemplarz_id_egzemplarza = " + number)
        else:
            QMessageBox.information(None, "Brak danej", "W bazie nie ma wypożyczonego egzemplarza o tym numerze")
            return
        if query.lastError().isValid():
            QMessageBox.critical(None, "Błąd!", query.lastError().text())
        if helpQuery.lastError().isValid():
            QMessageBox.critical(None, "Błąd!", helpQuery.lastError().text())

    def __addUser(self):
        query = QtSql.QSqlQuery(self.conn)

        args = [self.lineEdit_1_1, self.lineEdit_1_2, self.lineEdit_1_3,
                self.lineEdit_1_4, self.lineEdit_1_5, self.lineEdit_1_6,
                self.lineEdit_1_7, self.lineEdit_1_8, self.lineEdit_1_9,
                self.lineEdit_1_10, self.lineEdit_1_11]
        # TODO make regex for each field
        regexes = []
        text_ = QtWidgets.QLineEdit.text
        arg_values = [text_(i) for i in args[:-1]]
        filia = "'" + args[-1].text() + "'"
        for i in range(len(arg_values)):
            if len(arg_values[i]) == 0:
                QMessageBox.information(None, "Błąd!", "Pole nr " + str(i + 1) + " jest puste!")
                return
        w_args = self.textTr.wrapStringsWith(arg_values, "'")
        sql = "SELECT * FROM Użytkownik WHERE pesel like " + w_args[0]
        query.exec_(sql)
        if not query.next():
            addingtext = self.textTr.listToCommaStr(w_args, False)
            query.exec_("CALL add_user(" + addingtext + ")")
            query.exec_("INSERT INTO Przynależność_do_filii VALUES(" + filia + ", " + w_args[0] + ")")
        else:
            query.exec_("SELECT * FROM Przynależność_do_filii WHERE filia_numer = " + filia + " and uzytkownik_pesel = " + w_args[0])
            if query.next():
                QMessageBox.information(None, "Informacja", "Użytkownik o takim peselu należy już do tej filii.")
                return
            else:
                query.exec_("INSERT INTO Przynależność_do_filii VALUES(" + filia + ", " + w_args[0] + ")")
        if query.lastError().isValid():
            self.showError(query.lastError())
        else:
            QMessageBox.information(None, "Sukces!", "Pomyślnie dodano użytkownika!")

    def closeConnection(self):
        self.conn.close()
        print("Is conn open? " + str(self.conn.isOpen()))
        self.conn.removeDatabase("biblioteka")
        print("Connection closed")

    def showError(self, error):
        QMessageBox.critical(self.tabWidget, "Błąd nr " + str(error.number()), self.errorDict.get(error.number(),\
                             error.text()), QMessageBox.Ok)
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

