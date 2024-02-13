import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from .createacc import CreateAcc  # Update the import statement
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCCtT2AIwDywDG4b6-WUSftVk-_G9yt2K0",
    "authDomain": "authdemo-b309c.firebaseapp.com",
    "projectId": "authdemo-b309c",
    "storageBucket": "authdemo-b309c.appspot.com",
    "messagingSenderId": "666875513320",
    "appId": "1:666875513320:web:9b7a1525169bbb06eefc5d",
    "measurementId": "G-WZ4BZL6HP5"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.invalid.setVisible(False)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
        except:
            self.invalid.setVisible(True)

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)
