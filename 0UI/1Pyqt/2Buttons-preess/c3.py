
#preesing the button chage the screen content 
#for that we must have use following class stricture


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys



class MyWindow(QMainWindow):
   
   def __init__(self):
      super(MyWindow, self).__init__()
      self.setGeometry(200,200,400,800)
      self.setWindowTitle("this is window title")
      self.initUI()
   def fun(self):
      #it call when clik the button
      self.lab1.setText("you ckiked button")
      self.lab1.move(150,50)
   def initUI(self):
      #what ui are you want show write heire
      self.lab1 = QtWidgets.QLabel(self)
      self.lab1.setText("Not cliked")
      self.lab1.move(170,50)

      self.b1 =QtWidgets.QPushButton(self)
      self.b1.setText("button ")
      self.b1.move(150,100)      
      self.b1.clicked.connect(self.fun)  #her we have to just pass the function name not call to them

def window():
   app = QApplication(sys.argv)
   win = MyWindow()
   win.show()
   sys.exit(app.exec_())

window()

