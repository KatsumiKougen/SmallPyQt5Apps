import sys, os
from PyQt5 import QtWidgets, QtCore, QtGui

from ui.AboutDialogUI import Ui_Dialog

class TE_AboutDialog(QtWidgets.QDialog, Ui_Dialog):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        FanartPixmap = QtGui.QPixmap(f"{os.getcwd()}/img/bunny_suit_reimu.jpg")
        FanartPixmap = FanartPixmap.scaledToWidth(200, mode=QtCore.Qt.SmoothTransformation)
        self.AboutDialog_Image.setPixmap(FanartPixmap)
        self.resize(FanartPixmap.width(), FanartPixmap.height())
