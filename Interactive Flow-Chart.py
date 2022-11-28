# -*- coding: utf-8 -*-

# Interactive Flow Chart for CRIMJ 2022, Penn State Abington

# Please do not change the code - every part is crucial to not be dealing with errors.
# Feel free to reach the collaborators with your questions.

# All right reserved to Penn State Abington and collaborators.

# Date: 11/27/2022

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import re
import os

# Global Variables
buttonIndex = 0
buttonArray = []
classColor = ''
className = ''
additionalCredits = 0
name = ""
fileName = ""

# The main User Interface Window
class Ui_MainWindow(object):
        # Will generate the second user interface
        def openWindow(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_SecondWindow()
                self.ui.setupUi_2(self.window)
                self.window.show()

        # Generate the structure of the main window
        def setupUi(self, MainWindow):
                #Reuse initial flags and negate the flag you want to unset
                #Negate the Maximize button
                MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1201, 950)
                font = QtGui.QFont()
                font.setPointSize(8)
                MainWindow.setFont(font)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(190, 10, 771, 31))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(18)
                self.label.setFont(font)
                self.label.setMouseTracking(True)
                self.label.setStyleSheet("color: blue;")
                self.label.setMidLineWidth(1)
                self.label.setObjectName("label")

                self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.buttonClickedWindow())

                self.pushButton.setGeometry(QtCore.QRect(20, 180, 121, 91))
                self.pushButton.setStyleSheet("background-color: blue;\n"
                "color: white;\n"
                "")
                self.pushButton.setCheckable(False)
                self.pushButton.setAutoDefault(True)
                self.pushButton.setObjectName("pushButton")
                self.splitter = QtWidgets.QSplitter(self.centralwidget)
                self.splitter.setGeometry(QtCore.QRect(10, 100, 1151, 71))
                font = QtGui.QFont()
                font.setPointSize(16)
                self.splitter.setFont(font)
                self.splitter.setOrientation(QtCore.Qt.Horizontal)
                self.splitter.setObjectName("splitter")
                self.label_2 = QtWidgets.QLabel(self.splitter)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(16)
                self.label_2.setFont(font)
                self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_2.setAutoFillBackground(False)
                self.label_2.setFrameShape(QtWidgets.QFrame.Box)
                self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
                self.label_2.setTextFormat(QtCore.Qt.RichText)
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setWordWrap(False)
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.splitter)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(16)
                self.label_3.setFont(font)
                self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_3.setAutoFillBackground(False)
                self.label_3.setFrameShape(QtWidgets.QFrame.Box)
                self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
                self.label_3.setTextFormat(QtCore.Qt.RichText)
                self.label_3.setAlignment(QtCore.Qt.AlignCenter)
                self.label_3.setWordWrap(False)
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.splitter)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(16)
                self.label_4.setFont(font)
                self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_4.setAutoFillBackground(False)
                self.label_4.setFrameShape(QtWidgets.QFrame.Box)
                self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
                self.label_4.setTextFormat(QtCore.Qt.RichText)
                self.label_4.setAlignment(QtCore.Qt.AlignCenter)
                self.label_4.setWordWrap(False)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.splitter)
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(16)
                self.label_5.setFont(font)
                self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.label_5.setAutoFillBackground(False)
                self.label_5.setFrameShape(QtWidgets.QFrame.Box)
                self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
                self.label_5.setTextFormat(QtCore.Qt.RichText)
                self.label_5.setAlignment(QtCore.Qt.AlignCenter)
                self.label_5.setWordWrap(False)
                self.label_5.setIndent(-2)
                self.label_5.setObjectName("label_5")
                self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_2.setGeometry(QtCore.QRect(20, 280, 121, 91))
                self.pushButton_2.setStyleSheet("color: green;\n"
                "")
                self.pushButton_2.setCheckable(False)
                self.pushButton_2.setAutoDefault(True)
                self.pushButton_2.setObjectName("pushButton_2")
                self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_3.setGeometry(QtCore.QRect(20, 380, 121, 91))
                self.pushButton_3.setStyleSheet("color: black;\n"
                "")
                self.pushButton_3.setCheckable(False)
                self.pushButton_3.setObjectName("pushButton_3")
                self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_4.setGeometry(QtCore.QRect(20, 480, 121, 91))
                self.pushButton_4.setStyleSheet("color: black;\n"
                "")
                self.pushButton_4.setCheckable(False)
                self.pushButton_4.setObjectName("pushButton_4")
                self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_5.setGeometry(QtCore.QRect(20, 580, 121, 91))
                self.pushButton_5.setStyleSheet("color: black;\n"
                "")
                self.pushButton_5.setCheckable(False)
                self.pushButton_5.setObjectName("pushButton_5")
                self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_6.setGeometry(QtCore.QRect(150, 380, 121, 91))
                self.pushButton_6.setStyleSheet("color: black;\n"
                "border : 3px solid rgb(8, 115, 255);\n"
                "")
                self.pushButton_6.setCheckable(False)
                self.pushButton_6.setObjectName("pushButton_6")
                self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_7.setGeometry(QtCore.QRect(150, 480, 121, 91))
                self.pushButton_7.setStyleSheet("background-color: yellow;\n"
                "color: black;\n"
                "border : 3px solid blue;\n"
                "")
                self.pushButton_7.setCheckable(False)
                self.pushButton_7.setObjectName("pushButton_7")
                self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_8.setGeometry(QtCore.QRect(150, 180, 121, 91))
                self.pushButton_8.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                "color: white;\n"
                "border : 3px solid blue;\n"
                "")
                self.pushButton_8.setCheckable(False)
                self.pushButton_8.setAutoDefault(True)
                self.pushButton_8.setObjectName("pushButton_8")
                self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_9.setGeometry(QtCore.QRect(150, 280, 121, 91))
                self.pushButton_9.setStyleSheet("color: green;\n"
                "")
                self.pushButton_9.setCheckable(False)
                self.pushButton_9.setAutoDefault(True)
                self.pushButton_9.setObjectName("pushButton_9")
                self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_10.setGeometry(QtCore.QRect(150, 580, 121, 91))
                self.pushButton_10.setStyleSheet("background-color: purple;\n"
                "color: white;\n"
                "border : 4px solid blue;\n"
                "")
                self.pushButton_10.setCheckable(False)
                self.pushButton_10.setObjectName("pushButton_10")
                self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_11.setGeometry(QtCore.QRect(450, 180, 121, 91))
                self.pushButton_11.setStyleSheet("background-color: blue;\n"
                "color: white;\n"
                "")
                self.pushButton_11.setCheckable(False)
                self.pushButton_11.setAutoDefault(True)
                self.pushButton_11.setObjectName("pushButton_11")
                self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_12.setGeometry(QtCore.QRect(450, 580, 121, 91))
                self.pushButton_12.setStyleSheet("color: black;\n"
                "")
                self.pushButton_12.setCheckable(False)
                self.pushButton_12.setObjectName("pushButton_12")
                self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_13.setGeometry(QtCore.QRect(320, 380, 121, 91))
                self.pushButton_13.setStyleSheet("background-color: pink;\n"
                "color: white;\n"
                "border : 3px solid blue;\n"
                "")
                self.pushButton_13.setCheckable(False)
                self.pushButton_13.setObjectName("pushButton_13")
                self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_14.setGeometry(QtCore.QRect(450, 380, 121, 91))
                self.pushButton_14.setStyleSheet("color: black;\n"
                "")
                self.pushButton_14.setCheckable(False)
                self.pushButton_14.setObjectName("pushButton_14")
                self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_15.setGeometry(QtCore.QRect(450, 280, 121, 91))
                self.pushButton_15.setStyleSheet("color: green;\n"
                "")
                self.pushButton_15.setCheckable(False)
                self.pushButton_15.setAutoDefault(True)
                self.pushButton_15.setObjectName("pushButton_15")
                self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_16.setGeometry(QtCore.QRect(320, 480, 121, 91))
                self.pushButton_16.setStyleSheet("border-radius: 10px;\n"
                "background-color: rgb(249, 210, 222);\n"
                "border: 3px solid blue;")
                self.pushButton_16.setCheckable(False)
                self.pushButton_16.setObjectName("pushButton_16")
                self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_17.setGeometry(QtCore.QRect(320, 180, 121, 91))
                self.pushButton_17.setStyleSheet("background-color: blue;\n"
                "color: white;\n"
                "")
                self.pushButton_17.setCheckable(False)
                self.pushButton_17.setAutoDefault(True)
                self.pushButton_17.setObjectName("pushButton_17")
                self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_18.setGeometry(QtCore.QRect(450, 480, 121, 91))
                self.pushButton_18.setStyleSheet("color: black;\n"
                "")
                self.pushButton_18.setCheckable(False)
                self.pushButton_18.setObjectName("pushButton_18")
                self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_19.setGeometry(QtCore.QRect(320, 280, 121, 91))
                self.pushButton_19.setStyleSheet("color: green;\n"
                "")
                self.pushButton_19.setCheckable(False)
                self.pushButton_19.setAutoDefault(True)
                self.pushButton_19.setObjectName("pushButton_19")
                self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_20.setGeometry(QtCore.QRect(320, 580, 121, 91))
                self.pushButton_20.setStyleSheet("color: black;\n"
                "")
                self.pushButton_20.setCheckable(False)
                self.pushButton_20.setObjectName("pushButton_20")
                self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_21.setGeometry(QtCore.QRect(740, 180, 121, 91))
                self.pushButton_21.setStyleSheet("background-color: blue;\n"
                "color: white;\n"
                "")
                self.pushButton_21.setCheckable(False)
                self.pushButton_21.setAutoDefault(True)
                self.pushButton_21.setObjectName("pushButton_21")
                self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_22.setGeometry(QtCore.QRect(740, 580, 121, 91))
                self.pushButton_22.setStyleSheet("color: black;\n"
                "")
                self.pushButton_22.setCheckable(False)
                self.pushButton_22.setObjectName("pushButton_22")
                self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_23.setGeometry(QtCore.QRect(610, 380, 121, 91))
                self.pushButton_23.setStyleSheet("color: black;\n"
                "")
                self.pushButton_23.setCheckable(False)
                self.pushButton_23.setObjectName("pushButton_23")
                self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_24.setGeometry(QtCore.QRect(740, 380, 121, 91))
                self.pushButton_24.setStyleSheet("color: black;\n"
                "")
                self.pushButton_24.setCheckable(False)
                self.pushButton_24.setObjectName("pushButton_24")
                self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_25.setGeometry(QtCore.QRect(740, 280, 121, 91))
                self.pushButton_25.setStyleSheet("color: green;\n"
                "")
                self.pushButton_25.setCheckable(False)
                self.pushButton_25.setAutoDefault(True)
                self.pushButton_25.setObjectName("pushButton_25")
                self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_26.setGeometry(QtCore.QRect(610, 480, 121, 91))
                self.pushButton_26.setStyleSheet("color: black;\n"
                "")
                self.pushButton_26.setCheckable(False)
                self.pushButton_26.setObjectName("pushButton_26")
                self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_27.setGeometry(QtCore.QRect(610, 180, 121, 91))
                self.pushButton_27.setStyleSheet("background-color: blue;\n"
                "color: white;\n"
                "")
                self.pushButton_27.setCheckable(False)
                self.pushButton_27.setAutoDefault(True)
                self.pushButton_27.setObjectName("pushButton_27")
                self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_28.setGeometry(QtCore.QRect(740, 480, 121, 91))
                self.pushButton_28.setStyleSheet("color: black;\n"
                "")
                self.pushButton_28.setCheckable(False)
                self.pushButton_28.setObjectName("pushButton_28")
                self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_29.setGeometry(QtCore.QRect(610, 280, 121, 91))
                self.pushButton_29.setStyleSheet("color: green;\n"
                "")
                self.pushButton_29.setCheckable(False)
                self.pushButton_29.setAutoDefault(True)
                self.pushButton_29.setObjectName("pushButton_29")
                self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_30.setGeometry(QtCore.QRect(610, 580, 121, 91))
                self.pushButton_30.setStyleSheet("color: black;\n"
                "")
                self.pushButton_30.setCheckable(False)
                self.pushButton_30.setObjectName("pushButton_30")
                self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_31.setGeometry(QtCore.QRect(1030, 180, 121, 91))
                self.pushButton_31.setStyleSheet("background-color: blue;\n"
                "color: white;\n"
                "")
                self.pushButton_31.setCheckable(False)
                self.pushButton_31.setAutoDefault(True)
                self.pushButton_31.setObjectName("pushButton_31")
                self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_32.setGeometry(QtCore.QRect(1030, 580, 121, 91))
                self.pushButton_32.setStyleSheet("color: black;\n"
                "")
                self.pushButton_32.setCheckable(False)
                self.pushButton_32.setObjectName("pushButton_32")
                self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_33.setGeometry(QtCore.QRect(900, 380, 121, 91))
                self.pushButton_33.setStyleSheet("color: black;\n"
                "")
                self.pushButton_33.setCheckable(False)
                self.pushButton_33.setObjectName("pushButton_33")
                self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_34.setGeometry(QtCore.QRect(1030, 380, 121, 91))
                self.pushButton_34.setStyleSheet("color: black;\n"
                "")
                self.pushButton_34.setCheckable(False)
                self.pushButton_34.setObjectName("pushButton_34")
                self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_35.setGeometry(QtCore.QRect(1030, 280, 121, 91))
                self.pushButton_35.setStyleSheet("color: green;\n"
                "")
                self.pushButton_35.setCheckable(False)
                self.pushButton_35.setAutoDefault(True)
                self.pushButton_35.setObjectName("pushButton_35")
                self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_36.setGeometry(QtCore.QRect(900, 480, 121, 91))
                self.pushButton_36.setStyleSheet("color: black;\n"
                "")
                self.pushButton_36.setCheckable(False)
                self.pushButton_36.setObjectName("pushButton_36")
                self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_37.setGeometry(QtCore.QRect(900, 180, 121, 91))
                self.pushButton_37.setStyleSheet("background-color: blue;\n"
                "color: white;\n"
                "")
                self.pushButton_37.setCheckable(False)
                self.pushButton_37.setAutoDefault(True)
                self.pushButton_37.setObjectName("pushButton_37")
                self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_38.setGeometry(QtCore.QRect(1030, 480, 121, 91))
                self.pushButton_38.setStyleSheet("color: black;\n"
                "")
                self.pushButton_38.setCheckable(False)
                self.pushButton_38.setObjectName("pushButton_38")
                self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_39.setGeometry(QtCore.QRect(900, 280, 121, 91))
                self.pushButton_39.setStyleSheet("color: green;\n"
                "")
                self.pushButton_39.setCheckable(False)
                self.pushButton_39.setAutoDefault(True)
                self.pushButton_39.setObjectName("pushButton_39")
                self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.buttonClickedWindow())
                self.pushButton_40.setGeometry(QtCore.QRect(900, 580, 121, 91))
                self.pushButton_40.setStyleSheet("color: black;\n"
                "")
                self.pushButton_40.setCheckable(False)
                self.pushButton_40.setObjectName("pushButton_40")
                self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_41.setGeometry(QtCore.QRect(170, 720, 70, 70))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(8)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.pushButton_41.setFont(font)
                self.pushButton_41.setStyleSheet("border-radius: 10px;\n"
                "font: 75 8pt \"MS Shell Dlg 2\";\n"
                "background-color: rgb(153, 210, 242);\n"
                "border: 1px solid black;")
                self.pushButton_41.setAutoRepeatDelay(300)
                self.pushButton_41.setAutoRepeatInterval(100)
                self.pushButton_41.setFlat(False)
                self.pushButton_41.setObjectName("pushButton_41")
                self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_42.setGeometry(QtCore.QRect(260, 720, 70, 70))
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(False)
                font.setWeight(50)
                self.pushButton_42.setFont(font)
                self.pushButton_42.setStyleSheet("border-radius: 10px;\n"
                "background-color: rgb(249, 210, 222);\n"
                "border: 1px solid black;")
                self.pushButton_42.setAutoRepeatDelay(300)
                self.pushButton_42.setAutoRepeatInterval(100)
                self.pushButton_42.setFlat(False)
                self.pushButton_42.setObjectName("pushButton_42")
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(750, 730, 311, 16))
                self.label_11.setObjectName("label_11")
                self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_43.setGeometry(QtCore.QRect(530, 720, 70, 70))
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(False)
                font.setWeight(50)
                self.pushButton_43.setFont(font)
                self.pushButton_43.setStyleSheet("border-radius: 10px;\n"
                "border: 3px solid blue;")
                self.pushButton_43.setAutoRepeatDelay(300)
                self.pushButton_43.setAutoRepeatInterval(100)
                self.pushButton_43.setFlat(False)
                self.pushButton_43.setObjectName("pushButton_43")
                self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_44.setGeometry(QtCore.QRect(620, 720, 70, 70))
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(False)
                font.setWeight(50)
                self.pushButton_44.setFont(font)
                self.pushButton_44.setStyleSheet("border-radius: 10px;\n"
                "background-color: rgb(211,211,211);\n"
                "border: 1px solid black;")
                self.pushButton_44.setAutoRepeatDelay(300)
                self.pushButton_44.setAutoRepeatInterval(100)
                self.pushButton_44.setFlat(False)
                self.pushButton_44.setObjectName("pushButton_44")
                self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_45.setGeometry(QtCore.QRect(350, 720, 70, 70))
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(False)
                font.setWeight(50)
                self.pushButton_45.setFont(font)
                self.pushButton_45.setStyleSheet("border-radius: 10px;\n"
                "background-color: rgb(255, 219, 169);\n"
                "border: 1px solid black;")
                self.pushButton_45.setAutoRepeatDelay(300)
                self.pushButton_45.setAutoRepeatInterval(100)
                self.pushButton_45.setFlat(False)
                self.pushButton_45.setObjectName("pushButton_45")
                self.label_12 = QtWidgets.QLabel(self.centralwidget)
                self.label_12.setGeometry(QtCore.QRect(720, 760, 386, 16))
                self.label_12.setObjectName("label_12")
                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(100, 740, 61, 31))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.label_10.setFont(font)
                self.label_10.setObjectName("label_10")

                self.boxLabel = QtWidgets.QLabel(self.centralwidget)
                self.boxLabel.setGeometry(QtCore.QRect(70, 710, 1050, 91))
                self.boxLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                "border: 1px solid black;\n"
                "border-radius: 7px;")

                self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_47.setGeometry(QtCore.QRect(440, 720, 70, 70))
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(False)
                font.setWeight(50)
                self.pushButton_47.setFont(font)
                self.pushButton_47.setStyleSheet("border-radius: 10px;\n"
                "background-color: rgb(179, 145, 181);\n"
                "border: 1px solid black;")
                self.pushButton_47.setAutoRepeatDelay(300)
                self.pushButton_47.setAutoRepeatInterval(100)
                self.pushButton_47.setFlat(False)
                self.pushButton_47.setObjectName("pushButton_47")
                self.congratulationsLbl = QtWidgets.QLabel(self.centralwidget)
                self.congratulationsLbl.setGeometry(QtCore.QRect(400, 810, 491, 71))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.congratulationsLbl.setFont(font)
                self.congratulationsLbl.setStyleSheet("color: rgb(153, 0, 153);")
                self.congratulationsLbl.setText("")
                self.congratulationsLbl.setObjectName("congratulationsLbl")
                self.usernameLbl = QtWidgets.QLabel(self.centralwidget)
                self.usernameLbl.setGeometry(QtCore.QRect(40, 50, 221, 31))
                font = QtGui.QFont()
                font.setFamily("Baskerville Old Face")
                font.setPointSize(14)
                self.usernameLbl.setFont(font)
                self.usernameLbl.setStyleSheet("color: black;")
                self.usernameLbl.setText("")
                self.usernameLbl.setObjectName("usernameLbl")
                self.inputBox = QtWidgets.QLineEdit(self.centralwidget)
                self.inputBox.setGeometry(QtCore.QRect(480, 50, 141, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.inputBox.setFont(font)
                self.inputBox.setObjectName("inputBox")
                self.enterBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.addUser())
                self.enterBtn.setGeometry(QtCore.QRect(630, 50, 71, 31))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(8)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.enterBtn.setFont(font)
                self.enterBtn.setStyleSheet("border-radius: 10px;\n"
                "color: rgb(255, 255, 255);\n"
                "font: 75 8pt \"MS Shell Dlg 2\";\n"
                "background-color: rgb(205, 92, 92);\n"
                "border: 1px solid black;")
                self.enterBtn.setObjectName("enterBtn")
                self.nameLbl = QtWidgets.QLabel(self.centralwidget)
                self.nameLbl.setGeometry(QtCore.QRect(400, 50, 71, 31))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.nameLbl.setFont(font)
                self.nameLbl.setStyleSheet("color: black;")
                self.nameLbl.setObjectName("nameLbl")

                #Upload button
                self.uploadButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.uploadButton_handler())
                self.uploadButton.setGeometry(QtCore.QRect(710, 50, 61, 31))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(8)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.uploadButton.setFont(font)
                self.uploadButton.setStyleSheet("border-radius: 10px;\n"
                "color: rgb(255, 255, 255);\n"
                "font: 75 8pt \"MS Shell Dlg 2\";\n"
                "background-color: green;\n"
                "border: 1px solid black;")
                self.uploadButton.setObjectName("UploadButton")
                #self.pushButton_46.raise_()
                self.label.raise_()
                self.pushButton.raise_()
                self.splitter.raise_()
                self.pushButton_2.raise_()
                self.pushButton_3.raise_()
                self.pushButton_4.raise_()
                self.pushButton_5.raise_()
                self.pushButton_6.raise_()
                self.pushButton_7.raise_()
                self.pushButton_8.raise_()
                self.pushButton_9.raise_()
                self.pushButton_10.raise_()
                self.pushButton_11.raise_()
                self.pushButton_12.raise_()
                self.pushButton_13.raise_()
                self.pushButton_14.raise_()
                self.pushButton_15.raise_()
                self.pushButton_16.raise_()
                self.pushButton_17.raise_()
                self.pushButton_18.raise_()
                self.pushButton_19.raise_()
                self.pushButton_20.raise_()
                self.pushButton_21.raise_()
                self.pushButton_22.raise_()
                self.pushButton_23.raise_()
                self.pushButton_24.raise_()
                self.pushButton_25.raise_()
                self.pushButton_26.raise_()
                self.pushButton_27.raise_()
                self.pushButton_28.raise_()
                self.pushButton_29.raise_()
                self.pushButton_30.raise_()
                self.pushButton_31.raise_()
                self.pushButton_32.raise_()
                self.pushButton_33.raise_()
                self.pushButton_34.raise_()
                self.pushButton_35.raise_()
                self.pushButton_36.raise_()
                self.pushButton_37.raise_()
                self.pushButton_38.raise_()
                self.pushButton_39.raise_()
                self.pushButton_40.raise_()
                self.pushButton_41.raise_()
                self.pushButton_42.raise_()
                self.label_11.raise_()
                self.pushButton_43.raise_()
                self.pushButton_44.raise_()
                self.pushButton_45.raise_()
                self.label_12.raise_()
                self.label_10.raise_()
                self.pushButton_47.raise_()
                self.congratulationsLbl.raise_()
                self.usernameLbl.raise_()
                self.inputBox.raise_()
                self.enterBtn.raise_()
                self.nameLbl.raise_()
                self.uploadButton.raise_()
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 26))
                self.menubar.setObjectName("menubar")
                self.menuTBd = QtWidgets.QMenu(self.menubar)
                self.menuTBd.setObjectName("menuTBd")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.menubar.addAction(self.menuTBd.menuAction())
                self.retranslateUi(MainWindow, "")
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #TBD - Add commens
        def buttonClickedWindow(self):
                buttonHandle = MainWindow.sender()
                b = buttonHandle.objectName()
                counter = -1

                self.openWindow()

                for i in buttonArray:
                        counter += 1
                        if b == i.objectName():
                                global buttonIndex
                                buttonIndex = counter
                                return counter

        # The method will process a ".txt" file into a two dimensional array format
        # Also the method won't add any empty lines to the general data list.
        # The method accepts a valid filename
        def processFile(self, fileName):
                name = []
                courseID = []
                credit = []
                color = []
                taken = []
                data = []
                try:
                        myFile = open(fileName, "r")
                        for line in myFile:
                                # Strip the whitespaces
                                text = line.strip()
                                if text == '':
                                        #print("Empty line") - When it finds a empty line it breaks out of the loop
                                        pass
                                else:
                                        x = ''.join(text)
                                        x = text.split()
                                        x = ''.join(x)
                                        y = x.split(',')
                                        #print(y)  # This line is for debugging
                                        # Add the data in respective arrays
                                        name.append(y[0])
                                        courseID.append(y[1])
                                        credit.append(y[2])
                                        color.append(y[3])
                                        taken.append(y[4])
                                        data.append(y[:])
                except FileNotFoundError as fnf_error:
                        print(fnf_error)
                finally:
                        myFile.close()
                return data

        # Function that accepts the color and the frame of the button
        # And the button in which updates the color
        def updateColor(color, frame, button):

                if color == "blue":
                        button.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(153, 210, 242);\n"
                                             "border: 1px solid black;")
                        if frame == "C":
                                button.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(153, 210, 242);\n"
                                                     "border: 3px solid blue;")
                elif color == "pink":
                        button.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(249, 210, 222);\n"
                                             "border: 1px solid black;")
                        if frame == "C":
                                button.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(249, 210, 222);\n"
                                                     "border: 3px solid blue;")
                elif color == "yellow":
                        button.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(255, 219, 169);\n"
                                             "border: 1px solid black;")
                        if frame == "C":
                                button.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(255, 219, 169);\n"
                                                     "border: 3px solid blue;")
                elif color == "purple":
                        button.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(179, 145, 181);\n"
                                             "border: 1px solid black;")
                        if frame == "C":
                                button.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(179, 145, 181);\n"
                                                     "border: 3px solid blue;")
                elif color == "C":
                        button.setStyleSheet("border-radius: 10px;\nborder: 3px solid blue;")

                elif color == "grey":
                        button.setStyleSheet("border-radius: 10px;\n"
                                                "background-color: rgb(211, 211, 211);\n"
                                                "border: 1px solid black;")
                        if frame == "C":
                                button.setStyleSheet("border-radius: 10px;\n"
                                                     "background-color: rgb(211, 211, 211);\n"
                                                     "border: 3px solid blue;")


        # Populate method takes the processed file and displays the data
        # to the main Window interface and populates the button titles,
        # colors, frames.
        def populate(self, arrayButton, path, translator):
                data = Ui_MainWindow.processFile(self, path)
                #print("Filename entered: {}".format(path))

                counter = 0
                # In case the text file does not have enough (40 lines of information)
                # Display whatever the file information has and empty the rest of the buttons
                for i in arrayButton:
                        arrayButton[counter].setText("")
                        arrayButton[counter].setStyleSheet("border-radius: 10px;\n"
                                             "background-color: rgb(211, 211, 211);\n"
                                             "border: 1px solid black;")
                        counter = counter + 1
                counter = 0
                # Populate the buttons with the information of the text file
                # Note: expectation is that the text file has at least 40 lines
                for i in data:
                        if counter == len(arrayButton) or counter == len(data):
                            break
                        else:
                                line = i[0] + "\n" + i[1] + "\n" + i[2] + " credit(s)"
                                #print("Counter", counter, end="\n")

                                arrayButton[counter].setText(translator("MainWindow", line))

                                # If there is is a frame for "C or better grade"
                                if i[4] == "C":
                                        Ui_MainWindow.updateColor(i[3], "C", arrayButton[counter])
                                else:
                                        Ui_MainWindow.updateColor(i[3], "NotC", arrayButton[counter])
                        counter = counter + 1

        # Upload button calls getOpenFileName() to retrieve the file path
        # Uses the path to re-translate the information into the window
        def uploadButton_handler(self):
                path = self.getOpenFileName()
                global fileName
                fileName = path
                print("in upload method filename: {}".format(fileName))
                self.retranslateUi(MainWindow, newPath=path)
                #self.usernameLbl.setText(name)

        # Uses QFileDialog to get a file name form the directory
        # Restricted to Text files and All files only
        # returns the file path
        def getOpenFileName(self):
                file_filter = 'All Files (*);;Text Files (*.txt)'
                response = QFileDialog.getOpenFileName(
                        caption='Please Select a Text File',
                        directory='Text file.txt',
                        filter=file_filter,
                        initialFilter='Text Files (*.txt)'
                )
                #print(response[0])
                return response[0]

        # The method adds the name of the user to the text file and generates a text file
        # Save the username as the last line of the text file
        # In case the upload button is called it displays the user name inserted
        def addUser(self):
                global name
                global splitname
                name = self.inputBox.text()
                splitname = name.split()

                self.usernameLbl.setText(name)
                self.inputBox.clear()
                global fileName

                if name != "":
                        filename = name + ".txt"

                        if len(splitname) == 2:
                                with open(fileName, 'r', encoding='utf-8') as f:
                                        data1 = f.readlines()

                                data1[40] = [f'{splitname[0]} {splitname[1]},0, 0, None, None']
                                with open(filename, 'w', encoding='utf-8') as f:
                                        for lines in data1:
                                                f.writelines(lines)
                                f.close()
                                # Use the new file created to make the new changes
                                fileName = filename
                                self.retranslateUi(MainWindow, newPath=fileName)

                        elif len(splitname) == 3:
                                with open(fileName, 'r', encoding='utf-8') as f:
                                        data1 = f.readlines()

                                data1[40] = [f'{splitname[0]} {splitname[1]}, {splitname[2]},0, None, None']
                                with open(filename, 'w', encoding='utf-8') as f:
                                        for lines in data1:
                                                f.writelines(lines)
                                f.close()
                                # Use the new file created to make the new changes
                                fileName = filename
                                self.retranslateUi(MainWindow, newPath=fileName)

                        else:
                                with open(fileName, 'r', encoding='utf-8') as f:
                                        data1 = f.readlines()
                                data1[40] = [f'{splitname[0]},0, 0, None, None']
                                with open(filename, 'w', encoding='utf-8') as f:
                                        for lines in data1:
                                                f.writelines(lines)
                                f.close()

                                # Use the new file created to make the new changes
                                fileName = filename
                                self.retranslateUi(MainWindow, newPath=fileName)
                else:
                        self.usernameLbl.setText("Please Try Again!")


        # TBD -- add comments
        # There is a label in the bottom of the Main window that will display
        # A congratulations message if the user has selected all buttons as taken
        def congratulations(self, path):
                path = path if path else "UpdatedCourseInfo.txt"
                data = self.processFile(path)
                self.congratulationsLbl.clear()
                #print(data)

                x = 0
                numberOfCredits = 0
                totalNumberOfCredits = 0
                for i in data:
                        if i[3] == "grey":
                                x += 1
                                #print(x)
                                numberOfCredits += int(i[2])
                                #print("Grey lines: {}".format(x))
                        #print(totalNumberOfCredits)
                        totalNumberOfCredits += int(i[2])

                #print(additionalCredits)
                numberOfCredits += additionalCredits

                labelText = str(numberOfCredits) + " of " + str(totalNumberOfCredits) + " credit(s) completed"
                if additionalCredits:
                        self.congratulationsLbl.clear()
                        self.congratulationsLbl.setText(labelText)
                else:
                        self.congratulationsLbl.setText(labelText)
                #self.retranslateUi(Ui_MainWindow, path)

                if x == 40:
                        labelText = "Congratulations!!!"
                        self.congratulationsLbl.setText(labelText)

        # Method to re-translate the MainWindow and looking for a new path
        # This method will call other methods as: populate to generate the interface
        def retranslateUi(self, MainWindow, newPath):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Interactive Flow-Chart"))
                self.label.setText(_translate("MainWindow", "Criminal Justice - Bachelor of Science Suggested Academic Plan"))
                self.pushButton.setText(_translate("MainWindow", "CRIMJ 100 (3 cr)"))
                self.label_2.setText(_translate("MainWindow", "Year 1"))
                self.label_3.setText(_translate("MainWindow", "Year 2"))
                self.label_4.setText(_translate("MainWindow", "Year 3"))
                self.label_5.setText(_translate("MainWindow", "Year 4"))
                global buttonArray
                buttonArray = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4,
                                    self.pushButton_5,
                                    self.pushButton_6, self.pushButton_7,
                                    self.pushButton_8, self.pushButton_9, self.pushButton_10, self.pushButton_11,
                                    self.pushButton_12, self.pushButton_13,
                                    self.pushButton_14, self.pushButton_15, self.pushButton_16, self.pushButton_17,
                                    self.pushButton_18, self.pushButton_19, self.pushButton_20,
                                    self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24,
                                    self.pushButton_25, self.pushButton_26, self.pushButton_27,
                                    self.pushButton_28, self.pushButton_29, self.pushButton_30, self.pushButton_31,
                                    self.pushButton_32, self.pushButton_33, self.pushButton_34,
                                    self.pushButton_35, self.pushButton_36, self.pushButton_37, self.pushButton_38,
                                    self.pushButton_39, self.pushButton_40]

                newPath = newPath if newPath else "CourseInfo.txt"

                global fileName

                # We do not want to change the generic file 'CourseInfo.txt'
                # Since we want to have a file to get back to in case we lose information
                # The program makes the changes in 'UpdatedCourseInfo.txt'

                # path of the given file - not being used - saved for debugging the file source
                fullPath = os.path.dirname(os.path.abspath("CourseInfo.txt"))

                # current working directory
                currentDirectory = os.path.abspath(os.getcwd())
                mainFile = currentDirectory + "/CourseInfo.txt"
                #print(mainFile)

                if newPath == "CourseInfo.txt" or newPath == mainFile:
                        newPath == "UpdatedCourseInfo.txt"
                        fileName = "UpdatedCourseInfo.txt"
                else:
                        fileName = newPath


                """import sched, time
                s = sched.scheduler(time.time, time.sleep)
                s.enter(6, 1, self.congratulations(newPath), (s,))
                s.run()
                """

                #Update the username on the version
                with open(newPath, 'r', encoding='utf-8') as f:
                        data2 = f.readlines()
                userLine = data2[40]
                nameAray = ''.join(userLine)
                nameAray = ''.join(nameAray)
                y = nameAray.split(',')
                lastname = y[1]

                if lastname == '0':
                        name = y[0]
                else:
                        name = y[0] + y[1]
                f.close()

                self.usernameLbl.setText(name)
                self.congratulations(newPath)

                Ui_MainWindow.populate(self, arrayButton=buttonArray, path = newPath, translator=_translate)

                self.pushButton_41.setText(_translate("MainWindow", "Core\n"
                "(In\n"
                " Major)"))
                self.pushButton_42.setText(_translate("MainWindow", "Gen.\n"
                "Ed."))
                self.label_11.setText(_translate("MainWindow", "*** PSU starting Fall 2019 - must earn a C or higher"))
                self.pushButton_43.setText(_translate("MainWindow", "C or \n"
                "Better\n"
                "Required"))
                self.pushButton_44.setText(_translate("MainWindow", "Taken"))
                self.pushButton_45.setText(_translate("MainWindow", "Elective"))
                self.label_12.setText(_translate("MainWindow", "General Education: Complete 6 Inter-Domain (\"N\") or 6 Linked units"))
                self.label_10.setText(_translate("MainWindow", "Legend"))
                self.pushButton_47.setText(_translate("MainWindow", "Major &\n"
                "Gen.\n"
                " Ed."))
                self.enterBtn.setText(_translate("MainWindow", "Save"))
                self.nameLbl.setText(_translate("MainWindow", "Name:"))
                self.uploadButton.setText(_translate("MainWindow", "Upload"))

# The second window User Interface
class Ui_SecondWindow(object):
        # Method to construct the second window whole structure
        def setupUi_2(self, MainWindow):
                # Reuse initial flags and negate the flag you want to unset
                # Negate the Maximize button
                MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(794, 601)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.courseCodeLbl = QtWidgets.QLabel(self.centralwidget)
                self.courseCodeLbl.setGeometry(QtCore.QRect(240, 140, 101, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.courseCodeLbl.setFont(font)
                self.courseCodeLbl.setObjectName("courseCodeLbl")
                self.changeCourseBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.changeCourse())
                self.changeCourseBtn.setGeometry(QtCore.QRect(390, 310, 75, 35))
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
                self.lineEdit.setGeometry(QtCore.QRect(360, 130, 141, 31))
                self.lineEdit.setStyleSheet("border: 1px solid black;")
                self.lineEdit.setObjectName("lineEdit")
                self.blueBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.UpdateColorBlue())
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
                self.pinkBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.UpdateColorPink())
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
                self.violetBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.UpdateColorViolet())
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
                self.yellowBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.UpdateColorYellow())
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
                self.takenBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.UpdateColorTaken())
                self.takenBtn.setGeometry(QtCore.QRect(580, 390, 70, 70))
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(False)
                font.setWeight(50)
                self.takenBtn.setFont(font)
                self.takenBtn.setStyleSheet("border-radius: 10px;\n"
                "background-color: rgb(211,211,211);\n"
                "border: 1px solid black;")
                self.takenBtn.setAutoRepeatDelay(300)
                self.takenBtn.setAutoRepeatInterval(100)
                self.takenBtn.setFlat(False)
                self.takenBtn.setObjectName("takenBtn")
                self.cnotcBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.UpdateCNotC())
                self.cnotcBtn.setGeometry(QtCore.QRect(490, 390, 70, 70))
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(False)
                font.setWeight(50)
                self.cnotcBtn.setFont(font)
                self.cnotcBtn.setStyleSheet("border-radius: 10px;\n"
                "border: 3px solid blue;")
                self.cnotcBtn.setAutoRepeatDelay(300)
                self.cnotcBtn.setAutoRepeatInterval(100)
                self.cnotcBtn.setFlat(False)
                self.cnotcBtn.setObjectName("cnotcBtn")
                self.courseIDLbl = QtWidgets.QLabel(self.centralwidget)
                self.courseIDLbl.setGeometry(QtCore.QRect(250, 200, 81, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.courseIDLbl.setFont(font)
                self.courseIDLbl.setObjectName("courseIDLbl")
                self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_2.setGeometry(QtCore.QRect(360, 190, 141, 31))
                self.lineEdit_2.setStyleSheet("border: 1px solid black;")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.numberOfCreditsLbl = QtWidgets.QLabel(self.centralwidget)
                self.numberOfCreditsLbl.setGeometry(QtCore.QRect(250, 260, 81, 21))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.numberOfCreditsLbl.setFont(font)
                self.numberOfCreditsLbl.setObjectName("numberOfCreditsLbl")
                self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit_3.setGeometry(QtCore.QRect(360, 250, 141, 31))
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
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(210, 50, 361, 31))
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(20)
                self.label.setFont(font)
                self.label.setMouseTracking(True)
                self.label.setStyleSheet("color: blue;")
                self.label.setMidLineWidth(1)
                self.label.setObjectName("label")
                #self.label.setVisible()
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
                self.menubar.setObjectName("menubar")
                self.menuChange_Your_Schedule = QtWidgets.QMenu(self.menubar)
                self.menuChange_Your_Schedule.setObjectName("menuChange_Your_Schedule")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.menubar.addAction(self.menuChange_Your_Schedule.menuAction())
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Change Course"))
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
                self.label.setText(_translate("MainWindow", "Update Course Information"))

        #Add comments
        def UpdateColorBlue(self):
                line = self.changeCourse()

                if line == None:
                        current_line = (buttonArray[buttonIndex].text())
                        words = current_line.split()
                        words.pop()
                        words.append('blue')
                        words.append('NotC')
                        new_line = ', '.join(words)
                else:
                        new_line = f"{line}, blue, NotC"

                f = open(fileName, 'r')
                lines = f.readlines()
                f.close()

                lines[buttonIndex] = f"{new_line}\n"

                w = open(fileName, 'w')
                for x in lines:
                        w.write(x)
                w.close()

                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"
                                                       "background-color: rgb(153, 210, 242);\n"
                                                       "border: 1px solid black;")
                global classColor
                classColor = "background-color: rgb(153, 210, 242);\n"

                global className
                className = f"{line}, blue, "

                return new_line

        #Add comments
        def UpdateColorPink(self):
                line = self.changeCourse()

                if line == None:
                        current_line = (buttonArray[buttonIndex].text())
                        words = current_line.split()
                        words.pop()
                        words.append('pink')
                        words.append('NotC')
                        new_line = ', '.join(words)
                else:
                        new_line = f"{line}, pink, NotC"

                f = open(fileName, 'r')
                lines = f.readlines()
                f.close()

                lines[buttonIndex] = f"{new_line}\n"

                w = open(fileName, 'w')
                for x in lines:
                        w.write(x)
                w.close()

                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"
                                                       "background-color: rgb(249, 210, 222);\n"
                                                       "border: 1px solid black;")

                global classColor
                classColor = "background-color: rgb(249, 210, 222);\n"
                global className
                className = f"{line}, pink, "

                return new_line

        #Add comments
        def UpdateColorYellow(self):
                line = self.changeCourse()

                if line == None:
                        current_line = (buttonArray[buttonIndex].text())
                        words = current_line.split()
                        words.pop()
                        words.append('yellow')
                        words.append('NotC')
                        new_line = ', '.join(words)
                else:
                        new_line = f"{line}, yellow, NotC"

                f = open(fileName, 'r')
                lines = f.readlines()
                f.close()

                lines[buttonIndex] = f"{new_line}\n"

                w = open(fileName, 'w')
                for x in lines:
                        w.write(x)
                w.close()

                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"
                                                       "background-color: rgb(255, 219, 169);\n"
                                                       "border: 1px solid black;")

                global classColor
                classColor = "background-color: rgb(255, 219, 169);\n"
                global className
                className = f"{line}, yellow, "

                return new_line

        #Add comments
        def UpdateColorViolet(self):
                line = self.changeCourse()

                if line == None:
                        current_line = (buttonArray[buttonIndex].text())
                        words = current_line.split()
                        words.pop()
                        words.append('purple')
                        words.append('NotC')
                        new_line = ', '.join(words)
                else:
                        new_line = f"{line}, purple, NotC"

                f = open(fileName, 'r')
                lines = f.readlines()
                f.close()

                lines[buttonIndex] = f"{new_line}\n"

                w = open(fileName, 'w')
                for x in lines:
                        w.write(x)
                w.close()

                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"
                                                       "background-color: rgb(179, 145, 181);\n"
                                                       "border: 1px solid black;")

                global classColor
                classColor = "background-color: rgb(179, 145, 181);\n"
                global className
                className = f"{line}, purple, "

                return new_line

        #Add comments
        def UpdateColorTaken(self):
                line = self.changeCourse()

                if line == None or line == "":
                        current_line = (buttonArray[buttonIndex].text())
                        words = current_line.split()
                        words.pop()
                        words.append('grey')
                        words.append('NotC')
                        new_line = ', '.join(words)
                        #print(new_line)
                else:
                        x = ''.join(line)
                        x = line.split()
                        x = ''.join(x)
                        y = x.split(',')
                        global additionalCredits
                        additionalCredits = int(y[2])
                        #print("Inside Taken: {}".format(additionalCredits))
                        #congratulationsLbl.clear()
                        #Ui_MainWindow.retranslateUi(MainWindow, "UpdatedCourseInfo.txt")
                        new_line = f"{line}, grey, NotC"

                #self.congratulations(path="UpdatedCourseInfo.txt")

                f = open(fileName, 'r')
                lines = f.readlines()
                f.close()

                lines[buttonIndex] = f"{new_line}\n"

                w = open(fileName, 'w')
                for x in lines:
                        w.write(x)
                w.close()

                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"
                                                       "background-color: rgb(211, 211, 211);\n"
                                                       "border: 1px solid black;")

                global classColor
                classColor = "background-color: rgb(211, 211, 211);\n"
                global className
                className = f"{line}, grey, "

                return new_line

        #Add comments
        def UpdateCNotC(self):
                f = open(fileName, 'r')
                lines = f.readlines()
                f.close()

                color = ''
                global frame
                global classColor

                if className == '':
                        if buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # blue
                                                                     "background-color: rgb(153, 210, 242);\n"
                                                                     "border: 1px solid black;"):
                                classColor = "background-color: rgb(153, 210, 242);\n"
                                color = 'blue'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"  # blue
                                                                     "background-color: rgb(153, 210, 242);\n"
                                                                     "border: 3px solid blue;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(249, 210, 222);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(249, 210, 222);\n"
                                color = 'pink'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"  # blue
                                                                       "background-color: rgb(249, 210, 222);\n"
                                                                       "border: 3px solid blue;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # yellow
                                                                       "background-color: rgb(255, 219, 169);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(255, 219, 169);\n"
                                color = 'yellow'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"  # yellow
                                                                       "background-color: rgb(255, 219, 169);\n"
                                                                       "border: 3px solid blue;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # purple
                                                                       "background-color: rgb(179, 145, 181);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(179, 145, 181);\n"
                                color = 'purple'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"  # purple
                                                                       "background-color: rgb(179, 145, 181);\n"
                                                                       "border: 3px solid blue;")


                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(211, 211, 211);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(211, 211, 211);\n"
                                color = 'grey'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"
                                                                       "background-color: rgb(211, 211, 211);\n"
                                                                       "border: 3px solid blue;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # blue
                                                                     "background-color: rgb(153, 210, 242);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(153, 210, 242);\n"
                                color = 'blue'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"  # blue
                                                                     "background-color: rgb(153, 210, 242);\n"
                                                                       "border: 1px solid black;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(249, 210, 222);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(249, 210, 222);\n"
                                color = 'pink'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"  # blue
                                                                       "background-color: rgb(249, 210, 222);\n"
                                                                       "border: 1px solid black;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # yellow
                                                                       "background-color: rgb(255, 219, 169);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(255, 219, 169);\n"
                                color = 'yellow'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"  # yellow
                                                                       "background-color: rgb(255, 219, 169);\n"
                                                                       "border: 1px solid black;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # purple
                                                                       "background-color: rgb(179, 145, 181);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(179, 145, 181);\n"
                                color = 'purple'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"  # purple
                                                                       "background-color: rgb(179, 145, 181);\n"
                                                                       "border: 1px solid black;")


                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(211, 211, 211);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(211, 211, 211);\n"
                                color = 'grey'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet("border-radius: 10px;\n"
                                                                       "background-color: rgb(211, 211, 211);\n"
                                                                       "border: 1px solid black;")

                        current_line = (buttonArray[buttonIndex].text())
                        words = current_line.split()
                        words.pop()
                        words.append(color)
                        words.append('C')
                        new_line = ', '.join(words)
                        updated_line = new_line

                else:
                        updated_line = className + 'C'
                        lines[buttonIndex] = f"{updated_line}\n"

                        if buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # blue
                                                                     "background-color: rgb(153, 210, 242);\n"
                                                                     "border: 1px solid black;"):
                                classColor = "background-color: rgb(153, 210, 242);\n"
                                color = 'blue'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet(f"border-radius: 10px;\n{classColor}border: 3px solid blue;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # blue
                                                                     "background-color: rgb(153, 210, 242);\n"
                                                                     "border: 3px solid blue;"):
                                classColor = "background-color: rgb(153, 210, 242);\n"
                                color = 'blue'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet(f"border-radius: 10px;\n{classColor}border: 1px solid black;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(249, 210, 222);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(249, 210, 222);\n"
                                color = 'pink'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet(
                                        f"border-radius: 10px;\n{classColor}border: 3px solid blue;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(249, 210, 222);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(249, 210, 222);\n"
                                color = 'pink'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet(
                                        f"border-radius: 10px;\n{classColor}border: 1px solid black;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # yellow
                                                                       "background-color: rgb(255, 219, 169);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(255, 219, 169);\n"
                                color = 'yellow'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet(
                                        f"border-radius: 10px;\n{classColor}border: 1px solid black;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # yellow
                                                                       "background-color: rgb(255, 219, 169);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(255, 219, 169);\n"
                                color = 'yellow'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet(
                                        f"border-radius: 10px;\n{classColor}border: 3px solid blue;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # purple
                                                                       "background-color: rgb(179, 145, 181);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(179, 145, 181);\n"
                                color = 'purple'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet(
                                        f"border-radius: 10px;\n{classColor}border: 3px solid blue;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # purple
                                                                       "background-color: rgb(179, 145, 181);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(179, 145, 181);\n"
                                color = 'purple'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet(
                                        f"border-radius: 10px;\n{classColor}border: 1px solid black;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(211, 211, 211);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(211, 211, 211);\n"
                                color = 'grey'
                                frame = 'C'
                                buttonArray[buttonIndex].setStyleSheet(
                                        f"border-radius: 10px;\n{classColor}border: 3px solid blue;")

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(211, 211, 211);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(211, 211, 211);\n"
                                color = 'grey'
                                frame = 'NotC'
                                buttonArray[buttonIndex].setStyleSheet(
                                        f"border-radius: 10px;\n{classColor}border: 1px solid black;")

                current_line = (buttonArray[buttonIndex].text())
                words = current_line.split()
                words.pop()
                new_line = ', '.join(words)

                lines[buttonIndex] = (f"{new_line}, {color}, {frame}\n")

                w = open(fileName, 'w')
                for x in lines:
                        w.write(x)
                w.close()

        #Add comments
        def changeCourse(self):
                self.errorLbl.clear()
                courseCode = self.lineEdit.text()
                courseID = self.lineEdit_2.text()
                numberOfCredits = self.lineEdit_3.text()

                courseCodeRegex = re.search("^\s*[A-Za-z␣\t\n\r\s]{3,13}\s*$", courseCode)
                #courseIDRegex = re.search("^\s*[0-9]{3,4}\s*$", courseID)
                courseIDRegex = re.search("^\s*[0-9]{3,4}(?:\'w'\'W')?\s*$", courseID) #(?:\'w'\'W')?
                numberOfCreditsRegex = re.search("^\s*[0-9]{1}\s*$", numberOfCredits)

                if not courseCodeRegex or not courseIDRegex or not numberOfCreditsRegex:
                        self.errorLbl.setText("Error")
                else:
                        courseCodeFinal = courseCode
                        courseIDFinal = courseID.replace(" ", ", ")
                        numberOfCreditsFinal = numberOfCredits.replace(" ", ", ")
                        myline = (courseCodeFinal, courseIDFinal, numberOfCreditsFinal)
                        line = ", ".join(myline)

                        #print("changeCourse file name: " + fileName)
                        f = open(fileName, 'r')
                        lines = f.readlines()
                        f.close()
                        global color
                        global frame

                        if buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # blue
                                                                     "background-color: rgb(153, 210, 242);\n"
                                                                     "border: 1px solid black;"):
                                classColor = "background-color: rgb(153, 210, 242);\n"
                                color = 'blue'
                                frame = 'NotC'

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # blue
                                                                       "background-color: rgb(153, 210, 242);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(153, 210, 242);\n"
                                color = 'blue'
                                frame = 'C'

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(249, 210, 222);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(249, 210, 222);\n"
                                color = 'pink'
                                frame = 'NotC'


                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(249, 210, 222);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(249, 210, 222);\n"
                                color = 'pink'
                                frame = 'C'


                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # yellow
                                                                       "background-color: rgb(255, 219, 169);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(255, 219, 169);\n"
                                color = 'yellow'
                                frame = 'C'

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # yellow
                                                                       "background-color: rgb(255, 219, 169);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(255, 219, 169);\n"
                                color = 'yellow'
                                frame = 'NotC'


                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # purple
                                                                       "background-color: rgb(179, 145, 181);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(179, 145, 181);\n"
                                color = 'purple'
                                frame = 'NotC'


                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"  # purple
                                                                       "background-color: rgb(179, 145, 181);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(179, 145, 181);\n"
                                color = 'purple'
                                frame = 'C'

                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(211, 211, 211);\n"
                                                                       "border: 1px solid black;"):
                                classColor = "background-color: rgb(211, 211, 211);\n"
                                color = 'grey'
                                frame = 'NotC'


                        elif buttonArray[buttonIndex].styleSheet() == ("border-radius: 10px;\n"
                                                                       "background-color: rgb(211, 211, 211);\n"
                                                                       "border: 3px solid blue;"):
                                classColor = "background-color: rgb(211, 211, 211);\n"
                                color = 'grey'
                                frame = 'C'


                        lines[buttonIndex] = (f"{line}, {color}, {frame}\n")

                        #print("changecourse filename {}".format(fileName))
                        w = open(fileName, 'w')
                        for x in lines:
                                w.write(x)
                        w.close()

                        buttonArray[buttonIndex].setText(f"{courseCodeFinal} \n {courseIDFinal} \n {numberOfCreditsFinal} credits")

                        return line

# Main method that instantiate the class and calls the methods step by step
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ## Implement method
        MainWindow.show()
        sys.exit(app.exec_())