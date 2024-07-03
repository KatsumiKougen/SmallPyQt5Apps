from PyQt5 import QtWidgets, QtCore, QtGui
from ui.CPG_MainUi import CPG_MainWindow
import sys

class Main:
    
    def __init__(self):
        self.App = QtWidgets.QApplication(sys.argv)
        self.MainWindow = CPG_MainWindow(800, 600, "The Colour Picker Game")
        self.MainWindow.show()
        sys.exit(self.App.exec())

if __name__ == "__main__":
    a = Main()