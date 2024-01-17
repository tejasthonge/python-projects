import sys
from PyQt5.QtWidgets import QAppliction,QWidget
from Home import C2W_Home;

class Widget(QWidget,C2W_Home):
   def __init__(self):
      super().__init__(parent)
      self.c2w_ui = C2W_Home()
      self.c2w_ui.setupUi(self)

if __name__== '___main__':
   app = QAppliction(sys.argv)
   Widget = Widget()
   sys.exit(app.exec_())
   



