from PyQt5 import QtWidgets, QtCore, QtGui
from ui.TextEditorUI import Ui_MainWindow
from highlighter.highlighter import *
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
        self.TE_ShowDirectory()
        
        self.TE_SyntaxHlActionGroup = QtWidgets.QActionGroup(self)
        self.TE_SyntaxHlActionGroup.addAction(self.actionSH_PlainText)
        self.TE_SyntaxHlActionGroup.addAction(self.actionSH_Python)
        self.TE_SyntaxHlActionGroup.setExclusive(True)
        
        self.TE_SetIndentationSpace(4)
        self.highlighter = TE_Highlighter(TE_HighlightStyle.Python, self.TextEditor_MainWidget.document())
    
    def TE_DisplayTitle(self, workspace: Union[str, bool]):
        self.setWindowTitle(self._TE_AppVariables.WindowTitle.replace("$file", f"{workspace[0]}{'*' if not workspace[1] else ''}"))
    
    # Functions for displaying time (HH:MM:SS)
    
    def TE_DisplayTime(self, arg):
        self.Status_TimeLabel.setText(arg)
    
    def TE_UpdateTimeInBackground(self):
        self._updater = TE_TimeUpdate()
        self._updater.time.connect(self.TE_DisplayTime)
        self._updater.start()
    
    # Functions for working with directories
    
    def TE_ShowDirectory(self, directory: str = QtCore.QDir.current()):
        self.CWD_DirInput.setText(directory.dirName())
        self.FileView_TableWidget.clearContents()
        FileList = directory.entryInfoList()
        for idx, file in enumerate(FileList):
            self.FileView_TableWidget.insertRow(idx)
            self.FileView_TableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(file.fileName()))
            self.FileView_TableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(file.completeSuffix()))
            self.FileView_TableWidget.setItem(idx, 2, QtWidgets.QTableWidgetItem("✔️" if file.isDir() else "❌"))
            self.FileView_TableWidget.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(file.size())))
            self.FileView_TableWidget.setItem(idx, 4, QtWidgets.QTableWidgetItem(file.owner()))
            self.FileView_TableWidget.setItem(idx, 5, QtWidgets.QTableWidgetItem(str(file.ownerId())))
    
    # Functions for plain text widget
    
    def TE_SetIndentationSpace(self, width: int):
        Font = self.TextEditor_MainWidget.font()
        FontMetrics = QtGui.QFontMetricsF(Font)
        WhitespaceWidth = FontMetrics.width(" ")
        self.TextEditor_MainWidget.setTabStopDistance(WhitespaceWidth*width)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
