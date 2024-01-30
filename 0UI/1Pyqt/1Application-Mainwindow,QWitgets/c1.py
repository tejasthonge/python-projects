# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication,QMainWindow
# import sys
# 
# def window():
#    app = QApplication(sys.argv)
# 
#    win = QMainWindow()
#    win.setGeometry(100,100,400,800)  #where the allimet or size as follow for setting the window 
#    # win.setGeometry(xpos,ypos,width,height)
# 
# 
#    win.setWindowTitle("This Window titele") 
# 
# 
#    #setting the lebal by using QtWidgets clacc
#    label = QtWidgets.QLabel(win)
#    label.setText("this is an labal ")
#    label.move(150,100)
# 
#    win.show()
#    sys.exit(app.exec_())
# 
# window()


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():


   app = QApplication(sys.argv)   #we pass the sys module argv
   win= QMainWindow()
   win.setGeometry(100,400,200,600)#x,y,w,h
   win.setWindowTitle("This is thonge")
   
   label = QtWidgets.QLabel(win)
   label.setText("Ram Ram ,")
   label.move(50,40)#x,y

   label2 = QtWidgets.QLabel(win) 
   label2.setText ("I'm Tejas Rajendra Thonge")
   label2.move(50,50) 

   win.show()

   sys.exit(app.exec_())

window()