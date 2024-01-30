from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():


   app = QApplication(sys.argv)   #we pass the sys module argv
   win= QMainWindow()
   win.setGeometry(100,400,400,600)#x,y,w,h
   win.setWindowTitle("This Windo Titele")
   
   label = QtWidgets.QLabel(win)
   label.setText("Ram Ram ,")
   label.move(50,40)#x,y

   label2 = QtWidgets.QLabel(win) 
   label2.setText ("I'm Tejas Rajendra Thonge")
   label2.move(50,50) 

   win.show() #if we not call this window will not showing

   sys.exit(app.exec_())

window()