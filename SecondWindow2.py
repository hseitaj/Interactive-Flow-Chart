# -*- coding: utf-8 -*-
# CMPSC 487W Final Project
# Second UI

from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_SecondWindow(object):
    def setupUi_2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.courseCodeLbl = QtWidgets.QLabel(self.centralwidget)
        self.courseCodeLbl.setGeometry(QtCore.QRect(220, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.courseCodeLbl.setFont(font)
        self.courseCodeLbl.setObjectName("courseCodeLbl")
        self.changeCourseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.changeCourseBtn.setGeometry(QtCore.QRect(490, 310, 75, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.changeCourseBtn.setFont(font)
        self.changeCourseBtn.setStyleSheet("border-radius: 10;\n"
"background-color: rgb(95, 91, 85);\n"
"border: 1px solid black;\n"
"color: white;")
        self.changeCourseBtn.setObjectName("changeCourseBtn")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 150, 113, 35))
        self.lineEdit.setStyleSheet("border: 1px solid black;")
        self.lineEdit.setObjectName("lineEdit")
        self.blueBtn = QtWidgets.QPushButton(self.centralwidget)
        self.blueBtn.setGeometry(QtCore.QRect(130, 390, 70, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.blueBtn.setFont(font)
        self.blueBtn.setStyleSheet("border-radius: 10px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.blueBtn.setAutoRepeatDelay(300)
        self.blueBtn.setAutoRepeatInterval(100)
        self.blueBtn.setFlat(False)
        self.blueBtn.setObjectName("blueBtn")
        self.pinkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pinkBtn.setGeometry(QtCore.QRect(220, 390, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pinkBtn.setFont(font)
        self.pinkBtn.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(249, 210, 222);\n"
"border: 1px solid black;")
        self.pinkBtn.setAutoRepeatDelay(300)
        self.pinkBtn.setAutoRepeatInterval(100)
        self.pinkBtn.setFlat(False)
        self.pinkBtn.setObjectName("pinkBtn")
        self.violetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.violetBtn.setGeometry(QtCore.QRect(400, 390, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.violetBtn.setFont(font)
        self.violetBtn.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(179, 145, 181);\n"
"border: 1px solid black;")
        self.violetBtn.setAutoRepeatDelay(300)
        self.violetBtn.setAutoRepeatInterval(100)
        self.violetBtn.setFlat(False)
        self.violetBtn.setObjectName("violetBtn")
        self.yellowBtn = QtWidgets.QPushButton(self.centralwidget)
        self.yellowBtn.setGeometry(QtCore.QRect(310, 390, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.yellowBtn.setFont(font)
        self.yellowBtn.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 219, 169);\n"
"border: 1px solid black;")
        self.yellowBtn.setAutoRepeatDelay(300)
        self.yellowBtn.setAutoRepeatInterval(100)
        self.yellowBtn.setFlat(False)
        self.yellowBtn.setObjectName("yellowBtn")
        self.takenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.takenBtn.setGeometry(QtCore.QRect(580, 390, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.takenBtn.setFont(font)
        self.takenBtn.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(164, 164, 164);\n"
"border: 1px solid black;")
        self.takenBtn.setAutoRepeatDelay(300)
        self.takenBtn.setAutoRepeatInterval(100)
        self.takenBtn.setFlat(False)
        self.takenBtn.setObjectName("takenBtn")
        self.cnotcBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cnotcBtn.setGeometry(QtCore.QRect(490, 390, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.cnotcBtn.setFont(font)
        self.cnotcBtn.setStyleSheet("border-radius: 10px;\n"
"border: 1px solid black;")
        self.cnotcBtn.setAutoRepeatDelay(300)
        self.cnotcBtn.setAutoRepeatInterval(100)
        self.cnotcBtn.setFlat(False)
        self.cnotcBtn.setObjectName("cnotcBtn")
        self.courseIDLbl = QtWidgets.QLabel(self.centralwidget)
        self.courseIDLbl.setGeometry(QtCore.QRect(220, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.courseIDLbl.setFont(font)
        self.courseIDLbl.setObjectName("courseIDLbl")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 210, 113, 35))
        self.lineEdit_2.setStyleSheet("border: 1px solid black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.numberOfCreditsLbl = QtWidgets.QLabel(self.centralwidget)
        self.numberOfCreditsLbl.setGeometry(QtCore.QRect(220, 280, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.numberOfCreditsLbl.setFont(font)
        self.numberOfCreditsLbl.setObjectName("numberOfCreditsLbl")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 270, 113, 35))
        self.lineEdit_3.setStyleSheet("border: 1px solid black;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.errorLbl = QtWidgets.QLabel(self.centralwidget)
        self.errorLbl.setGeometry(QtCore.QRect(320, 330, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.errorLbl.setFont(font)
        self.errorLbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.errorLbl.setText("")
        self.errorLbl.setObjectName("errorLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """
            ADD CODE BELOW THIS COMMENT SECTION
            ADD CODE BELOW THIS COMMENT SECTION
            ADD CODE BELOW THIS COMMENT SECTION
            ADD CODE BELOW THIS COMMENT SECTION
        """

        self.changeCourseBtn.clicked.connect(self.changeCourse)
    """ self.blueBtn.clicked.connect(self.changeCourse)
        self.pinkBtn.clicked.connect(self.changeCourse)
        self.yellowBtn.clicked.connect(self.changeCourse)
        self.violetBtn.clicked.connect(self.changeCourse)
        self.cnotcBtn.clicked.connect(self.changeCourse)
        self.takenBtn.clicked.connect(self.changeCourse)"""

    def test(self, button):
        #button.clicked.disconnect()
        text = self.changeCouse()
        button.setText(text)
        #button.setText("Click me")
        #button.clicked.connect(self.test(button))


    def buttonClick(self, button):
        text = self.changeCouse()
        self.button.setText(text)
        print(text, button.title(), end= "  ")
        """for button in buttonArr:
            while not button.isChecked():
                if button.isChecked():
                    self.button.setText(text)"""
        """while not button.isChecked():
            if button.isChecked():
                self.button.setText(text)
                break
            continue"""

    def changeCourse(self):
        self.errorLbl.clear()
        courseCode = self.lineEdit.text()
        courseID = self.lineEdit_2.text()
        numberOfCredits = self.lineEdit_3.text()

        courseCodeRegex = re.search("^\s*[A-Za-z]{5}\s*$", courseCode)
        courseIDRegex = re.search("^\s*[0-9]{3}\s*$", courseID)
        numberOfCreditsRegex = re.search("^\s*[0-9]{1}\s*$", numberOfCredits)

        if not courseCodeRegex or not courseIDRegex or not numberOfCreditsRegex:
            self.errorLbl.setText("Error")
        else:
            f = open('CourseInfo.txt', 'r')
            w = open('UpdatedCourseInfo.txt', 'w')

            courseCodeFinal = courseCode.replace(" ", ", ")
            courseIDFinal = courseID.replace(" ", ", ")
            numberOfCreditsFinal = numberOfCredits.replace(" ", ", ")
            myline = (courseCodeFinal, courseIDFinal, numberOfCreditsFinal)
            line = ", ".join(myline)
            print(line)

            data = f.readlines()
            data[0] = f"{line} \n"
            w.writelines(data)

            f.close()
            w.close()

            #return line


    """
            ADD CODE aBOVE THIS COMMENT SECTION
            ADD CODE BELOW THIS COMMENT SECTION
            ADD CODE BELOW THIS COMMENT SECTION
            ADD CODE BELOW THIS COMMENT SECTION
    """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.courseCodeLbl.setText(_translate("MainWindow", "Course Code"))
        self.changeCourseBtn.setText(_translate("MainWindow", "Change"))
        self.blueBtn.setText(_translate("MainWindow", "Core\n"
"(In\n"
" Major)"))
        self.pinkBtn.setText(_translate("MainWindow", "Gen.\n"
"Ed."))
        self.violetBtn.setText(_translate("MainWindow", "Major &\n"
"Gen.\n"
" Ed."))
        self.yellowBtn.setText(_translate("MainWindow", "Elective"))
        self.takenBtn.setText(_translate("MainWindow", "Taken"))
        self.cnotcBtn.setText(_translate("MainWindow", "C or\n"
"Better \n"
"Required"))
        self.courseIDLbl.setText(_translate("MainWindow", "Course ID"))
        self.numberOfCreditsLbl.setText(_translate("MainWindow", "# of Credits"))
        #self.buttonArray = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_02 = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi_2(MainWindow_02)
    MainWindow_02.show()
    sys.exit(app.exec_())
