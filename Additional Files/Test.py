import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
"""
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def changeCouse(self):
        d = 0
        linecounter = 0
        input = self.lineEdit.text()
        f = open('CourseInfo.txt', 'r')
        w = open('UpdatedCourseInfo.txt', 'w')
        data = f.readlines()
        updated_line = input.replace(' ', ', ')
        data[0] = f"{updated_line} \n"
        w.writelines(data)
        f.close()
        w.close()
        return updated_line

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.changeCouse())
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        text = self.changeCouse()
        #self.statusBar().showMessage(sender.text() + ' was pressed')
        self.btn1.setText(text)
        print(text)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()"""

"""app = QApplication(sys.argv)
qBtn1 = QPushButton("Click me")
qBtn1.show()

def onBtn1Clicked():
  print("Method 1")
  qBtn1.clicked.disconnect()
  qBtn1.setText("Click me again")
  qBtn1.clicked.connect(onBtn1ClickedAgain)

def onBtn1ClickedAgain():
  print("Method 2")
  qBtn1.clicked.disconnect()
  qBtn1.setText("Click me")
  qBtn1.clicked.connect(onBtn1Clicked)

qBtn1.clicked.connect(onBtn1Clicked)
sys.exit(app.exec_())"""

import sys
from PyQt5.QtWidgets import *
from functools import partial
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 400, 200)
        self.initUI()

    def initUI(self):
        self.button1 = QPushButton(self)
        self.button1.setGeometry(40, 40, 100, 50)
        self.button1.setText("Button 1")
        self.button1.clicked.connect(partial(self.clicked_btn, 'Button 1'))

        self.button2 = QPushButton(self)
        self.button2.setGeometry(150, 40, 100, 50)
        self.button2.setText("Button 2")
        self.button2.clicked.connect(partial(self.clicked_btn, 'Button 2'))

        self.show()

    def clicked_btn(self, value):
        #print(f'{value} clicked')
        sender = self.sender()
        print(f'Sender says: {sender.text()} was clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
