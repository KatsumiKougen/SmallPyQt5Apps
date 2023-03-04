import sys
from PyQt5 import QtWidgets, QtCore, QtGui

sys.path.append(".")
from ui.ViewBlockUI import Ui_Dialog

class TE_ViewBlockDialog(QtWidgets.QDialog, Ui_Dialog):
    
    def __init__(self, text: str):
        super().__init__()
        self.setupUi(self)
        self.VB_BlockWidget.clear()
        self.VB_BlockWidget.setPlainText(text)
