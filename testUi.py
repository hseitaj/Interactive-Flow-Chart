from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(358, 226)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 341, 201))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mylist = QtWidgets.QListWidget(self.widget)
        self.mylist.setObjectName("mylist")
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.mylist.addItem(item)
        self.horizontalLayout.addWidget(self.mylist)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add = QtWidgets.QPushButton(self.widget)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.edit = QtWidgets.QPushButton(self.widget)
        self.edit.setObjectName("edit")
        self.verticalLayout.addWidget(self.edit)
        self.remove = QtWidgets.QPushButton(self.widget)
        self.remove.setObjectName("remove")
        self.verticalLayout.addWidget(self.remove)
        self.up = QtWidgets.QPushButton(self.widget)
        self.up.setObjectName("up")
        self.verticalLayout.addWidget(self.up)
        self.down = QtWidgets.QPushButton(self.widget)
        self.down.setObjectName("down")
        self.verticalLayout.addWidget(self.down)
        self.sort = QtWidgets.QPushButton(self.widget)
        self.sort.setObjectName("sort")
        self.verticalLayout.addWidget(self.sort)
        self.closebtn = QtWidgets.QPushButton(self.widget)
        self.closebtn.setObjectName("closebtn")
        self.verticalLayout.addWidget(self.closebtn)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.mylist.isSortingEnabled()
        self.mylist.setSortingEnabled(False)
        item = self.mylist.item(0)
        item.setText(_translate("Dialog", "guawa"))
        item = self.mylist.item(1)
        item.setText(_translate("Dialog", "kivy"))
        item = self.mylist.item(2)
        item.setText(_translate("Dialog", "grapes"))
        item = self.mylist.item(3)
        item.setText(_translate("Dialog", "mausami"))
        item = self.mylist.item(4)
        item.setText(_translate("Dialog", "watermelon"))
        item = self.mylist.item(5)
        item.setText(_translate("Dialog", "apple"))
        item = self.mylist.item(6)
        item.setText(_translate("Dialog", "chikoo"))
        item = self.mylist.item(7)
        item.setText(_translate("Dialog", "kiwi "))
        item = self.mylist.item(8)
        item.setText(_translate("Dialog", "lemon"))
        item = self.mylist.item(9)
        item.setText(_translate("Dialog", "mango"))
        item = self.mylist.item(10)
        item.setText(_translate("Dialog", "orange"))
        item = self.mylist.item(11)
        item.setText(_translate("Dialog", "pineapple"))
        item = self.mylist.item(12)
        item.setText(_translate("Dialog", "banana"))
        self.mylist.setSortingEnabled(__sortingEnabled)
        self.add.setText(_translate("Dialog", "&Add"))
        self.edit.setText(_translate("Dialog", "&Edit"))
        self.remove.setText(_translate("Dialog", "&Remove"))
        self.up.setText(_translate("Dialog", "&Up"))
        self.down.setText(_translate("Dialog", "&Down"))
        self.sort.setText(_translate("Dialog", "&Sort"))
        self.closebtn.setText(_translate("Dialog", "&Close"))

from PyQt5 import QtWidgets, QtCore, QtGui
import sys, time
from PyQt5.QtCore import Qt
#import myDialog
#from myDialog import Ui_Dialog

class window(QtWidgets.QDialog):
    def __init__(self):
        super(window,self).__init__()

        #####SETTING BASE DIALOG####
        self.dialogClass=Ui_Dialog()
        self.dialogClass.setupUi(self)

        ####building singla and slots####
        self.build_connection()
        #################################


        self.show()

    def build_connection(self):
        self.dialogClass.add.clicked.connect(self.ask_input)
        self.dialogClass.edit.clicked.connect(self.edit_current)
        self.dialogClass.remove.clicked.connect(self.delete_current)
        self.dialogClass.closebtn.clicked.connect(self.close)
        self.dialogClass.down.clicked.connect(self.go_down)
        self.dialogClass.up.clicked.connect(self.go_up)
        self.dialogClass.sort.clicked.connect(self.sort_list)


    def ask_input(self):
        pass

    def sort_list(self):
        self.dialogClass.mylist.sortItems()

    def go_down(self):
        rowno=self.dialogClass.mylist.currentRow()
        val=self.dialogClass.mylist.takeItem(self.dialogClass.mylist.currentRow())
        if val:
            self.dialogClass.mylist.insertItem(rowno+1,val.text())
            self.dialogClass.mylist.setCurrentRow(rowno+1)

    def go_up(self):
        rowno=self.dialogClass.mylist.currentRow()
        val=self.dialogClass.mylist.takeItem(self.dialogClass.mylist.currentRow())
        if val:
            self.dialogClass.mylist.insertItem(rowno-1,val.text())
            self.dialogClass.mylist.setCurrentRow(rowno-1)

    def close_edit(self,item):
        try:
            val=self.dialogClass.mylist.item(self.dialogClass.mylist.currentRow())
            self.dialogClass.mylist.closePersistentEditor(val)
        except Exception as E:
            print(E)

    def edit_current(self):
        val=self.dialogClass.mylist.item(self.dialogClass.mylist.currentRow())
        try:
            self.dialogClass.mylist.openPersistentEditor(val)
            self.dialogClass.mylist.currentTextChanged.connect(self.close_edit)
        except Exception as E:
            print(E)
#        print(dir(val))

    def delete_current(self):
        val=self.dialogClass.mylist.takeItem(self.dialogClass.mylist.currentRow())
        if val:
            print(val.text())




app=QtWidgets.QApplication([])
ex=window()
sys.exit(app.exec_())

#time.sleep(5)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())