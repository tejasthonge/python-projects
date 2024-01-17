import sys

from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

class HelloC2W(QWidget):
   def __init__(self):
      super().__init__()
      self.init_ui()
      
   def init_ui(self):
         #Create the button

         hello_button = QPushButton("Say Hello", self)
         hello_button.setStyleSheet("background-color:white;  width:300px; height:30px; color:black; margin-top:100px;")

         #nee to import
         shadow =QGraphicsDropShad
         owEffect()
         shadow.setColor(
            QColor(0,0,0,150)  #setting the shadow color and opaccity
         )

         shadow.setBlurRadius(10)
         hello_button.setGraphicsEffect(shadow)

         #call to the button

         hello_button.clicked.connect(self.say_hellow)

         #create the label to displying  the massage
         self.massage_label = QLabel(self)

      #setup the layout
         layout = QVBoxLayout()
         layout.addWidget(hello_button)
         layout.addWidget(self.massage_label)

         #set the  layout for the main window
         self.setLayout(layout)

         #set up the main window

         self.setWindowTitle("Hellow ,core2web")
         self.setGeometry(500,500,500,500)

   def say_hellow(self):
         self.massage_label.setText("jay shree Ram Core@2Web")
         self.massage_label.setStyleSheet("color:red;font-size:20px;margin-left:150px")  

if __name__ == '__main__':
   app =QApplication(sys.argv)
   window =  HelloC2W()
   window.show()
   sys.exit(app.exec_())