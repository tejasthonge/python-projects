

import sys
import os
from PyQt5 import QtCore,QtCui,QtWidgets
from PyQt5.QtCore import QGraphicsDropShadowEffect ,QTabWidget ,QVBoxLayout,QWidget, QApplication,QDesktopWidget
from PyQt5.QtGui import  QColor,QIcon
from PythonInfo import C2W_PythonInfo

#from pyi import C2W_PythonInfo

class C2W_Home(object):

   layout1 = None
   count = 0

   WidgetTemp = 0
   def c2w_openLink(self,event):
      #Open the link in the default web browser
      QtGui.QDestopServices.openUrl(QtCore.QUrl("https://core2web.in/"))

   def setupUi(self ,Widget):
      self.c2w_WidgetTemp = Widget

      desktop = QDesktopWidget()

      #get the primary screen(monito)
      primary_sreen = desktop.screenGeometry(desktop.primaryScreen())

      #Retrieve the width of the monitor
      monitor_width = primary_sreen.width()
      monitor_height = primary_sreen.width()

      Widget.setObjectName("Widget")
      Widget.resize(monitor_width,monitor_height)

      self.c2w_widget = QtWidgets.QWidget(Widget)
      self.c2w_widget = QtWidgets.QWidget(Widget)
      self.c2w_widget = QtWidgets.setStyleSheet('backgroun : #01E1D')
      self.c2w_widget = QtWidgets.setObjectName("imageLab")
      