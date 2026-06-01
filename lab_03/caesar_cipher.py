import sys
from string import ascii_uppercase
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.encrypt)
        self.ui.btn_decrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        plaintext = self.ui.txt_plain_text.toPlainText().strip()
        key_text = self.ui.txt_key.toPlainText().strip()
        if not plaintext:
            self.show_error('Please enter plaintext to encrypt.')
            return
        try:
            key = int(key_text)
        except ValueError:
            self.show_error('Key must be an integer.')
            return

        cipher_text = self.caesar_encrypt(plaintext, key)
        self.ui.txt_cipher_text.setPlainText(cipher_text)

    def decrypt(self):
        cipher_text = self.ui.txt_cipher_text.toPlainText().strip()
        key_text = self.ui.txt_key.toPlainText().strip()
        if not cipher_text:
            self.show_error('Please enter ciphertext to decrypt.')
            return
        try:
            key = int(key_text)
        except ValueError:
            self.show_error('Key must be an integer.')
            return

        plaintext = self.caesar_decrypt(cipher_text, key)
        self.ui.txt_plain_text.setPlainText(plaintext)

    def caesar_encrypt(self, text: str, key: int) -> str:
        result = []
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                base = ascii_uppercase if is_upper else ascii_uppercase.lower()
                index = base.index(char)
                shifted = base[(index + key) % 26]
                result.append(shifted)
            else:
                result.append(char)
        return ''.join(result)

    def caesar_decrypt(self, text: str, key: int) -> str:
        return self.caesar_encrypt(text, -key)

    def show_error(self, message: str):
        QMessageBox.warning(self, 'Input error', message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())