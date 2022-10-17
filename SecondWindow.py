# -*- coding: utf-8 -*-
# CMPSC 487W Final Project
# Second UI

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi_2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.editCourseName = QtWidgets.QPushButton(self.centralwidget)
        self.editCourseName.setGeometry(QtCore.QRect(440, 150, 75, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.editCourseName.setFont(font)
        self.editCourseName.setStyleSheet("border-radius: 10;\n"
"background-color: rgb(95, 91, 85);\n"
"border: 1px solid black;\n"
"color: white;")
        self.editCourseName.setObjectName("editCourseName")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 150, 113, 35))
        self.lineEdit.setStyleSheet("border: 1px solid black;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 380, 70, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton.setAutoRepeatDelay(300)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 380, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(249, 210, 222);\n"
"border: 1px solid black;")
        self.pushButton_2.setAutoRepeatDelay(300)
        self.pushButton_2.setAutoRepeatInterval(100)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 380, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(179, 145, 181);\n"
"border: 1px solid black;")
        self.pushButton_3.setAutoRepeatDelay(300)
        self.pushButton_3.setAutoRepeatInterval(100)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 380, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 219, 169);\n"
"border: 1px solid black;")
        self.pushButton_4.setAutoRepeatDelay(300)
        self.pushButton_4.setAutoRepeatInterval(100)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 380, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(164, 164, 164);\n"
"border: 1px solid black;")
        self.pushButton_5.setAutoRepeatDelay(300)
        self.pushButton_5.setAutoRepeatInterval(100)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.editCourseName.clicked.connect(self.changeCouse)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeCouse(self, index):
        input = self.lineEdit.text()
        print(input)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Edit Course:"))
        self.editCourseName.setText(_translate("MainWindow", "Edit"))
        self.pushButton.setText(_translate("MainWindow", "Core\n"
"(In\n"
" Major)"))
        self.pushButton_2.setText(_translate("MainWindow", "Gen.\n"
"Ed."))
        self.pushButton_3.setText(_translate("MainWindow", "Major &\n"
"Gen.\n"
" Ed."))
        self.pushButton_4.setText(_translate("MainWindow", "Elective"))
        self.pushButton_5.setText(_translate("MainWindow", "Taken"))

def buttonClicked():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_02 = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi_2(MainWindow_02)
    MainWindow_02.show()
    sys.exit(app.exec_())
