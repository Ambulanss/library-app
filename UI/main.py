# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addUserButton = QtWidgets.QPushButton(self.tab_3)
        self.addUserButton.setObjectName("addUserButton")
        self.gridLayout_2.addWidget(self.addUserButton, 1, 1, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_1_1 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_1_1.setMaxLength(11)
        self.lineEdit_1_1.setPlaceholderText("PESEL")
        self.lineEdit_1_1.setObjectName("lineEdit_1_1")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_1)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_1_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_2.setMaxLength(50)
        self.lineEdit_1_2.setPlaceholderText("Imię")
        self.lineEdit_1_2.setObjectName("lineEdit_1_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_2)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_1_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_3.setMaxLength(50)
        self.lineEdit_1_3.setPlaceholderText("Kowalski")
        self.lineEdit_1_3.setObjectName("lineEdit_1_3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_3)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_1_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_4.setInputMethodHints(QtCore.Qt.ImhDate)
        self.lineEdit_1_4.setText("")
        self.lineEdit_1_4.setMaxLength(10)
        self.lineEdit_1_4.setPlaceholderText("1900-01-01")
        self.lineEdit_1_4.setObjectName("lineEdit_1_4")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_4)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_1_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_5.setMaxLength(50)
        self.lineEdit_1_5.setPlaceholderText("Poznań")
        self.lineEdit_1_5.setObjectName("lineEdit_1_5")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_5)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_1_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_6.setMaxLength(50)
        self.lineEdit_1_6.setPlaceholderText("Poznań")
        self.lineEdit_1_6.setObjectName("lineEdit_1_6")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_6)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_1_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_7.setMaxLength(50)
        self.lineEdit_1_7.setPlaceholderText("Wielkopolska")
        self.lineEdit_1_7.setObjectName("lineEdit_1_7")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_7)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_1_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_8.setText("")
        self.lineEdit_1_8.setPlaceholderText("")
        self.lineEdit_1_8.setObjectName("lineEdit_1_8")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_8)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_1_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_9.setPlaceholderText("")
        self.lineEdit_1_9.setObjectName("lineEdit_1_9")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_9)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_1_10 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_1_10.setMaxLength(6)
        self.lineEdit_1_10.setPlaceholderText("")
        self.lineEdit_1_10.setObjectName("lineEdit_1_10")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1_10)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label)
        self.gridLayout_2.addLayout(self.formLayout_3, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3)
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_9)
        self.registerSearchButton = QtWidgets.QPushButton(self.tab_3)
        self.registerSearchButton.setObjectName("registerSearchButton")
        self.horizontalLayout_11.addWidget(self.registerSearchButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.registerSearchLabelsLayout = QtWidgets.QHBoxLayout()
        self.registerSearchLabelsLayout.setObjectName("registerSearchLabelsLayout")
        self.verticalLayout_9.addLayout(self.registerSearchLabelsLayout)
        self.tableView_5 = QtWidgets.QTableView(self.tab_3)
        self.tableView_5.setObjectName("tableView_5")
        self.verticalLayout_9.addWidget(self.tableView_5)
        self.gridLayout_5.addLayout(self.verticalLayout_9, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_32 = QtWidgets.QLabel(self.tab_4)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_7.addWidget(self.label_32)
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_8)
        self.borrowSearchButton = QtWidgets.QPushButton(self.tab_4)
        self.borrowSearchButton.setObjectName("borrowSearchButton")
        self.horizontalLayout_7.addWidget(self.borrowSearchButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.borrowSearchLabelsLayout = QtWidgets.QHBoxLayout()
        self.borrowSearchLabelsLayout.setObjectName("borrowSearchLabelsLayout")
        self.verticalLayout_8.addLayout(self.borrowSearchLabelsLayout)
        self.tableView_4 = QtWidgets.QTableView(self.tab_4)
        self.tableView_4.setObjectName("tableView_4")
        self.verticalLayout_8.addWidget(self.tableView_4)
        self.gridLayout_7.addLayout(self.verticalLayout_8, 0, 1, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.borrowButton = QtWidgets.QPushButton(self.tab_5)
        self.borrowButton.setObjectName("borrowButton")
        self.gridLayout_9.addWidget(self.borrowButton, 1, 0, 1, 1)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_33 = QtWidgets.QLabel(self.tab_5)
        self.label_33.setObjectName("label_33")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.label_34 = QtWidgets.QLabel(self.tab_5)
        self.label_34.setObjectName("label_34")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.label_35 = QtWidgets.QLabel(self.tab_5)
        self.label_35.setObjectName("label_35")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit.setMaxLength(11)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_7.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_8.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.gridLayout_9.addLayout(self.formLayout_8, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.reserveButton = QtWidgets.QPushButton(self.tab_6)
        self.reserveButton.setObjectName("reserveButton")
        self.gridLayout_8.addWidget(self.reserveButton, 1, 0, 1, 1)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_36 = QtWidgets.QLabel(self.tab_6)
        self.label_36.setObjectName("label_36")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_36)
        self.label_37 = QtWidgets.QLabel(self.tab_6)
        self.label_37.setObjectName("label_37")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.label_38 = QtWidgets.QLabel(self.tab_6)
        self.label_38.setObjectName("label_38")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_9.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_9.setMaxLength(11)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_9.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.gridLayout_8.addLayout(self.formLayout_9, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.resAndBorButton = QtWidgets.QPushButton(self.tab_8)
        self.resAndBorButton.setObjectName("resAndBorButton")
        self.gridLayout_10.addWidget(self.resAndBorButton, 1, 0, 1, 1)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_39 = QtWidgets.QLabel(self.tab_8)
        self.label_39.setObjectName("label_39")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.label_40 = QtWidgets.QLabel(self.tab_8)
        self.label_40.setObjectName("label_40")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.gridLayout_10.addLayout(self.formLayout_7, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.cancelResButton = QtWidgets.QPushButton(self.tab_7)
        self.cancelResButton.setObjectName("cancelResButton")
        self.gridLayout_11.addWidget(self.cancelResButton, 2, 0, 1, 1)
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.label_41 = QtWidgets.QLabel(self.tab_7)
        self.label_41.setObjectName("label_41")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.gridLayout_11.addLayout(self.formLayout_10, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.gridLayout_7.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_4.addWidget(self.label_30)
        self.comboBox_7 = QtWidgets.QComboBox(self.tab)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_7)
        self.addingSearchButton = QtWidgets.QPushButton(self.tab)
        self.addingSearchButton.setObjectName("addingSearchButton")
        self.horizontalLayout_4.addWidget(self.addingSearchButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.addSearchLabelsLayout = QtWidgets.QHBoxLayout()
        self.addSearchLabelsLayout.setObjectName("addSearchLabelsLayout")
        self.verticalLayout_5.addLayout(self.addSearchLabelsLayout)
        self.tableView_3 = QtWidgets.QTableView(self.tab)
        self.tableView_3.setObjectName("tableView_3")
        self.verticalLayout_5.addWidget(self.tableView_3)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setObjectName("label_22")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setObjectName("label_23")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setObjectName("label_24")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setObjectName("label_26")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setObjectName("label_27")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setObjectName("label_28")
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setObjectName("label_29")
        self.formLayout_6.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.comboBox_5 = QtWidgets.QComboBox(self.tab)
        self.comboBox_5.setObjectName("comboBox_5")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_5)
        self.comboBox_6 = QtWidgets.QComboBox(self.tab)
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setObjectName("comboBox_6")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_6.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setObjectName("label_25")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.gridLayout_4.addLayout(self.formLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout.addLayout(self.formLayout)
        self.addButton = QtWidgets.QPushButton(self.tab_2)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(self.tab_2)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setEnabled(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.searchButton = QtWidgets.QPushButton(self.tab_2)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tableView_2 = QtWidgets.QTableView(self.tab_2)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_3.addWidget(self.tableView_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.gridLayout_6.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_1_1, self.lineEdit_1_2)
        Form.setTabOrder(self.lineEdit_1_2, self.lineEdit_1_3)
        Form.setTabOrder(self.lineEdit_1_3, self.lineEdit_1_4)
        Form.setTabOrder(self.lineEdit_1_4, self.lineEdit_1_5)
        Form.setTabOrder(self.lineEdit_1_5, self.lineEdit_1_6)
        Form.setTabOrder(self.lineEdit_1_6, self.lineEdit_1_7)
        Form.setTabOrder(self.lineEdit_1_7, self.lineEdit_1_8)
        Form.setTabOrder(self.lineEdit_1_8, self.lineEdit_1_9)
        Form.setTabOrder(self.lineEdit_1_9, self.lineEdit_1_10)
        Form.setTabOrder(self.lineEdit_1_10, self.addUserButton)
        Form.setTabOrder(self.addUserButton, self.addButton)
        Form.setTabOrder(self.addButton, self.comboBox)
        Form.setTabOrder(self.comboBox, self.tableView)
        Form.setTabOrder(self.tableView, self.tabWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Biblioteka"))
        self.addUserButton.setText(_translate("Form", "Zatwierdź"))
        self.label_6.setText(_translate("Form", "Pesel*"))
        self.label_7.setText(_translate("Form", "Imię*"))
        self.label_8.setText(_translate("Form", "Nazwisko*"))
        self.label_9.setText(_translate("Form", "Data urodzenia"))
        self.label_10.setText(_translate("Form", "Miasto*"))
        self.label_11.setText(_translate("Form", "Powiat*"))
        self.label_14.setText(_translate("Form", "Województwo*"))
        self.label_15.setText(_translate("Form", "Numer lokalu*"))
        self.label_16.setText(_translate("Form", "Ulica*"))
        self.label_17.setText(_translate("Form", "Kod pocztowy*"))
        self.label.setText(_translate("Form", "* - pole obowiązkowe"))
        self.label_3.setText(_translate("Form", "Przeszukaj tabelę:"))
        self.comboBox_9.setItemText(0, _translate("Form", "Spóźnialscy"))
        self.comboBox_9.setItemText(1, _translate("Form", "Użytkownicy_w_filiach"))
        self.comboBox_9.setItemText(2, _translate("Form", "Wypożyczenia_użytkowników"))
        self.comboBox_9.setItemText(3, _translate("Form", "Egzemplarze_i_dzieła"))
        self.comboBox_9.setItemText(4, _translate("Form", "Autorzy_i_dzieła"))
        self.registerSearchButton.setText(_translate("Form", "Przeszukaj"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Zarejestruj użytkownika"))
        self.label_32.setText(_translate("Form", "Przeszukaj tabelę:"))
        self.comboBox_8.setItemText(0, _translate("Form", "Spóźnialscy"))
        self.comboBox_8.setItemText(1, _translate("Form", "Użytkownicy_w_filiach"))
        self.comboBox_8.setItemText(2, _translate("Form", "Wypożyczenia_użytkowników"))
        self.comboBox_8.setItemText(3, _translate("Form", "Egzemplarze_i_dzieła"))
        self.comboBox_8.setItemText(4, _translate("Form", "Autorzy_i_dzieła"))
        self.borrowSearchButton.setText(_translate("Form", "Przeszukaj"))
        self.borrowButton.setText(_translate("Form", "Zatwierdź wypożyczenie"))
        self.label_33.setText(_translate("Form", "PESEL"))
        self.label_34.setText(_translate("Form", "Numer egzemplarza"))
        self.label_35.setText(_translate("Form", "Dni na oddanie"))
        self.lineEdit_8.setText(_translate("Form", "21"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "Wypożycz"))
        self.reserveButton.setText(_translate("Form", "Zatwierdź rezerwację"))
        self.label_36.setText(_translate("Form", "PESEL"))
        self.label_37.setText(_translate("Form", "Numer egzemplarza"))
        self.label_38.setText(_translate("Form", "Dni do wygaśnięcia"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Form", "Zarezerwuj"))
        self.resAndBorButton.setText(_translate("Form", "Zatwierdź"))
        self.label_39.setText(_translate("Form", "Numer egzemplarza"))
        self.label_40.setText(_translate("Form", "Dni na oddanie"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Form", "Zatwierdź rezerwację i wypożycz"))
        self.cancelResButton.setText(_translate("Form", "Potwierdź ANULOWANIE rezerwacji"))
        self.label_41.setText(_translate("Form", "Numer egzemplarza"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Form", "Anuluj rezerwację"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Wypożyczenia i rezerwacje"))
        self.label_30.setText(_translate("Form", "Przeszukaj tabelę:"))
        self.comboBox_7.setItemText(0, _translate("Form", "Spóźnialscy"))
        self.comboBox_7.setItemText(1, _translate("Form", "Użytkownicy_w_filiach"))
        self.comboBox_7.setItemText(2, _translate("Form", "Wypożyczenia_użytkowników"))
        self.comboBox_7.setItemText(3, _translate("Form", "Egzemplarze_i_dzieła"))
        self.comboBox_7.setItemText(4, _translate("Form", "Autorzy_i_dzieła"))
        self.addingSearchButton.setText(_translate("Form", "Przeszukaj"))
        self.label_31.setText(_translate("Form", "* - pole obowiązkowe"))
        self.pushButton.setText(_translate("Form", "Dodaj"))
        self.label_22.setText(_translate("Form", "Tytuł*"))
        self.label_23.setText(_translate("Form", "Imię autora*"))
        self.label_24.setText(_translate("Form", "Nazwisko autora*"))
        self.label_26.setText(_translate("Form", "Numer filii*"))
        self.label_27.setText(_translate("Form", "Dział*"))
        self.label_28.setText(_translate("Form", "Rok wydania"))
        self.label_29.setText(_translate("Form", "Gatunek"))
        self.label_25.setText(_translate("Form", "Typ*"))
        self.comboBox_4.setItemText(0, _translate("Form", "Ksiazka"))
        self.comboBox_4.setItemText(1, _translate("Form", "Film"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Dodaj egzemplarz"))
        self.label_2.setText(_translate("Form", "Tabela:"))
        self.comboBox_2.setToolTip(_translate("Form", "Wybierz tabelę, którą chcesz zmodyfikować"))
        self.comboBox_2.setItemText(0, _translate("Form", "Autor"))
        self.comboBox_2.setItemText(1, _translate("Form", "Użytkownik"))
        self.comboBox_2.setItemText(2, _translate("Form", "Filia"))
        self.comboBox_2.setItemText(3, _translate("Form", "Gatunek"))
        self.comboBox_2.setItemText(4, _translate("Form", "Dzieło"))
        self.comboBox_2.setItemText(5, _translate("Form", "Dział"))
        self.comboBox_2.setItemText(6, _translate("Form", "Autorstwo_dzieła"))
        self.comboBox_2.setItemText(7, _translate("Form", "Egzemplarz"))
        self.comboBox_2.setItemText(8, _translate("Form", "Przynależność_do_filii"))
        self.comboBox_2.setItemText(9, _translate("Form", "Przynależność_do_gatunku"))
        self.comboBox_2.setItemText(10, _translate("Form", "Rezerwacja"))
        self.comboBox_2.setItemText(11, _translate("Form", "Wypożyczenie"))
        self.addButton.setText(_translate("Form", "Dodaj"))
        self.deleteButton.setText(_translate("Form", "Usuń"))
        self.label_21.setText(_translate("Form", "Podejrzyj tabelę:"))
        self.comboBox.setToolTip(_translate("Form", "Wybierz tabelę, którą chcesz obejrzeć"))
        self.comboBox.setItemText(0, _translate("Form", "Autor"))
        self.comboBox.setItemText(1, _translate("Form", "Użytkownik"))
        self.comboBox.setItemText(2, _translate("Form", "Filia"))
        self.comboBox.setItemText(3, _translate("Form", "Gatunek"))
        self.comboBox.setItemText(4, _translate("Form", "Dzieło"))
        self.comboBox.setItemText(5, _translate("Form", "Dział"))
        self.comboBox.setItemText(6, _translate("Form", "Autorstwo_dzieła"))
        self.comboBox.setItemText(7, _translate("Form", "Egzemplarz"))
        self.comboBox.setItemText(8, _translate("Form", "Przynależność_do_filii"))
        self.comboBox.setItemText(9, _translate("Form", "Przynależność_do_gatunku"))
        self.comboBox.setItemText(10, _translate("Form", "Rezerwacja"))
        self.comboBox.setItemText(11, _translate("Form", "Wypożyczenie"))
        self.label_20.setText(_translate("Form", "Przeszukaj tabelę"))
        self.comboBox_3.setToolTip(_translate("Form", "Wybierz tabelę, którą chcesz przeszukać"))
        self.comboBox_3.setItemText(0, _translate("Form", "Autor"))
        self.comboBox_3.setItemText(1, _translate("Form", "Użytkownik"))
        self.comboBox_3.setItemText(2, _translate("Form", "Filia"))
        self.comboBox_3.setItemText(3, _translate("Form", "Gatunek"))
        self.comboBox_3.setItemText(4, _translate("Form", "Dzieło"))
        self.comboBox_3.setItemText(5, _translate("Form", "Dział"))
        self.comboBox_3.setItemText(6, _translate("Form", "Autorstwo_dzieła"))
        self.comboBox_3.setItemText(7, _translate("Form", "Egzemplarz"))
        self.comboBox_3.setItemText(8, _translate("Form", "Przynależność_do_filii"))
        self.comboBox_3.setItemText(9, _translate("Form", "Przynależność_do_gatunku"))
        self.comboBox_3.setItemText(10, _translate("Form", "Rezerwacja"))
        self.comboBox_3.setItemText(11, _translate("Form", "Wypożyczenie"))
        self.searchButton.setText(_translate("Form", "Wyszukaj wg wzorca"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Widok administratora"))

