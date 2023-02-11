from dataclasses import dataclass
from PyQt5 import QtWidgets, QtCore, QtGui
from TextEditorUI import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    @dataclass
    class _AppVariables:
        WindowTitle: str = "The text editor - Untitled"
        
        TextEdInsertMode: str = "`INSERT`"
        TextEdOverwriteMode: str = "`OVERWRITE`"
        FileStatusLabel: str = "File: **$file**"
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle(self._AppVariables.WindowTitle)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())