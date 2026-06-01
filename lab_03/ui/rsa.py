# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(340, 20, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(40, 70, 120, 30))
        self.btn_gen_keys.setObjectName("btn_gen_keys")

        self.label_plain = QtWidgets.QLabel(self.centralwidget)
        self.label_plain.setGeometry(QtCore.QRect(40, 120, 100, 20))
        self.label_plain.setObjectName("label_plain")
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(40, 145, 820, 100))
        self.txt_plain_text.setObjectName("txt_plain_text")

        self.label_cipher = QtWidgets.QLabel(self.centralwidget)
        self.label_cipher.setGeometry(QtCore.QRect(40, 260, 100, 20))
        self.label_cipher.setObjectName("label_cipher")
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(40, 285, 820, 100))
        self.txt_cipher_text.setObjectName("txt_cipher_text")

        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(40, 400, 120, 30))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(180, 400, 120, 30))
        self.btn_decrypt.setObjectName("btn_decrypt")

        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(40, 450, 150, 20))
        self.label_info.setObjectName("label_info")
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(40, 475, 820, 100))
        self.txt_info.setObjectName("txt_info")

        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(40, 590, 120, 30))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(180, 590, 120, 30))
        self.btn_verify.setObjectName("btn_verify")

        self.label_signature = QtWidgets.QLabel(self.centralwidget)
        self.label_signature.setGeometry(QtCore.QRect(320, 590, 120, 30))
        self.label_signature.setObjectName("label_signature")
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(450, 590, 410, 30))
        self.txt_sign.setObjectName("txt_sign")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA Cipher"))
        self.label_title.setText(_translate("MainWindow", "RSA Cipher"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
        self.label_plain.setText(_translate("MainWindow", "Plaintext"))
        self.label_cipher.setText(_translate("MainWindow", "Ciphertext"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label_info.setText(_translate("MainWindow", "Message to sign / verify"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.label_signature.setText(_translate("MainWindow", "Signature"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
