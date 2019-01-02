#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(0,0, 800, 600)
        self.setWindowTitle('Biblioteka')
        self.setWindowIcon(QIcon('books.png'))

        self.show()


if __name__ == '__main__':

    db = QSqlDatabase.addDatabase('QMYSQL')

    app = QApplication(sys.argv)

    ex = App()

    sys.exit(app.exec_())