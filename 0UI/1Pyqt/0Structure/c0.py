from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys



class MyWindow(QMainWindow):
   
   def __init__(self):
      super(MyWindow, self).__init__()
      self.setGeometry(200,200,400,800)
      self.setWindowTitle("this is window title")
      self.initUI()

   def initUI(self):
      #what ui are you want show write heire
      self.lab1 = QtWidgets.QLabel(self)
      self.lab1.setText("this labal")
      self.lab1.move(150,50)

      

def window():
   app = QApplication(sys.argv)
   win = MyWindow()
   win.show()
   sys.exit(app.exec_())

window()

