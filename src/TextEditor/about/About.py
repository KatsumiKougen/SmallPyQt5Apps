import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from ui.AboutDialogUI import Ui_Dialog

class TE_AboutDialog(QtWidgets.QDialog, Ui_Dialog):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
