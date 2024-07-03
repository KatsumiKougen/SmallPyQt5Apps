from PyQt5 import QtWidgets, QtCore, QtGui
from ui.CPG_MainUi import Ui_MainWindow
import sys

class CPG_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    Window = CPG_MainWindow()
    Window.show()
    sys.exit(App.exec())