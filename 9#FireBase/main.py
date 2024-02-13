# main.py
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase
from login import Login  # Update the import statement

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
auth = firebase.auth()

class CreateAccDialog(QDialog):  # Rename the class to avoid conflicts
    def __init__(self):
        super(CreateAccDialog, self).__init__()
        loadUi("createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.invalid.setVisible(False)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            try:
                auth.create_user_with_email_and_password(email, password)
                login = Login()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            except:
                self.invalid.setVisible(True)

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
