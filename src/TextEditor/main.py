from PyQt5 import QtWidgets, QtCore, QtGui
from TextEditorUI import Ui_MainWindow
import sys, time
from typing import Union
from datetime import datetime

class TE_TimeUpdate(QtCore.QThread):
    
    time = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            cur = datetime.now().strftime("%H:%M:%S")
            self.time.emit(cur)
            time.sleep(.5)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    class _TE_AppVariables:
    
        WindowTitle: str = "The text editor - $file"
        
        TextEdInsertMode: str = "`I`"
        TextEdOverwriteMode: str = "`O`"
        FileStatusLabel: str = "File: **$file**"
        
        CurrentWorkspaceName: list[Union[str, bool]] = [
            ["Untitled", False]
        ]
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.TE_DisplayTitle(self._TE_AppVariables.CurrentWorkspaceName[0])
        self.TE_UpdateTimeInBackground()
        self.TE_ShowDirectory("a")
    
    def TE_DisplayTitle(self, workspace: Union[str, bool]):
        self.setWindowTitle(self._TE_AppVariables.WindowTitle.replace("$file", f"{workspace[0]}{'*' if not workspace[1] else ''}"))
    
    def TE_DisplayTime(self, arg):
        self.Status_TimeLabel.setText(arg)
    
    def TE_UpdateTimeInBackground(self):
        self._updater = TE_TimeUpdate()
        self._updater.time.connect(self.TE_DisplayTime)
        self._updater.start()
    
    def TE_ShowDirectory(self, directory: str):
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["file"])
        self.FileView_TreeView.setModel(model)
        
        parent = QtGui.QStandardItem("Traveller")
        child0 = QtGui.QStandardItem("Aether")
        child1 = QtGui.QStandardItem("Lumine")
        parent.appendRow([child0, child1])
        model.appendRow(parent)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
