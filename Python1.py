


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 657)
        Dialog.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(106, 255, 98);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(253, 255, 103);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 360, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 520, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 119, 133);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(280, 30, 151, 101))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(280, 200, 151, 101))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(280, 360, 151, 101))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(280, 520, 151, 101))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")

        self.pushButton_4.clicked.connect(self.setupUi)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Django"))
        self.pushButton_2.setText(_translate("Dialog", "PyGame"))
        self.pushButton_3.setText(_translate("Dialog", "PyQt5"))
        self.pushButton_4.setText(_translate("Dialog", "Cv2"))
        self.plainTextEdit.setPlaceholderText(_translate("Dialog", "Это сайт на котором можно сделать всё, сайт для продажи корма, кейсы в ксго, даже переделать авито."))
        self.plainTextEdit_2.setPlaceholderText(_translate("Dialog", "Это  игра созданная на Python. В ней есть 2 героя - Тётя зина, Паук. Тётя Зина Нашла его у себя в комнате, захотела пришлёпнуть его, пистолетом."))
        self.plainTextEdit_3.setPlaceholderText(_translate("Dialog", "Это калькулятор. Если не можешь решить задачу по математике, он тебе поможет, либо ты не сделаешь домашнее задание."))
        self.plainTextEdit_4.setPlaceholderText(_translate("Dialog", "        Сдесь нужна камера!!! При улыбке на камеру, улыбка выделяется, в противоположном случае, обвода не будет."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
