#how to click the button



from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication ,QMainWindow
import sys

def fun():
   print("Button is clicked") #it print on terminal not on screent

   


def window ():

   app = QApplication(sys.argv)
   
   win =QMainWindow()
   win.setGeometry(100,200,400,800)


   #button:

   b1 = QtWidgets.QPushButton(win)
   b1.setText("this is is button")
   b1.move(100,100)

   b1.clicked.connect(fun)


   win.show()
   sys.exit(app.exec_())

window()