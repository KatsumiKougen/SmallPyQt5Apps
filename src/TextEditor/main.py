from PyQt5 import QtWidgets, QtCore, QtGui
from ui.TextEditorUI import Ui_MainWindow
from highlighter.highlighter import *
import sys, time, re
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
        
        CurrentWorkspaceName: Union[str, bool] = ["Untitled", False]
        
        DocumentBuffer: dict[str, str] = {
            "saved": None,
            "modified": None
        }
        
        DocumentStatus: dict[str, int] = {
            "line": 1,
            "column": 1,
            "char": 0,
            "word": 0
        }
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.TE_DisplayTitle(self._TE_AppVariables.CurrentWorkspaceName)
        self.TE_UpdateTimeInBackground()
        self.TE_ShowDirectory()
        
        self.TE_SyntaxHlActionGroup = QtWidgets.QActionGroup(self)
        self.TE_SetMenuBar()
        
        self.TE_SetLCDWidgets()
        
        self.TE_SetIndentationSpace(4)
        self.highlighter = None
        self.TE_SetSyntaxHighlighting(TE_HighlightStyle.PlainText)
        self.TextEditor_MainWidget.textChanged.connect(self.TE_UpdateLCD)
    
    def TE_DisplayTitle(self, workspace: Union[str, bool]):
        self.setWindowTitle(self._TE_AppVariables.WindowTitle.replace("$file", f"{workspace[0]}{'*' if not workspace[1] else ''}"))
    
    # Functions for displaying time (HH:MM:SS)
    
    def TE_DisplayTime(self, arg):
        self.Status_TimeLabel.setText(arg)
    
    def TE_UpdateTimeInBackground(self):
        self._updater = TE_TimeUpdate()
        self._updater.time.connect(self.TE_DisplayTime)
        self._updater.start()
    
    # Function for manipulating LCD widgets
    
    def TE_SetLCDWidgets(self):
        self.Status_LCDDisplay0.setStyleSheet("QLCDNumber {background: black; color: #1438db;}")
        self.Status_LCDDisplay1.setStyleSheet("QLCDNumber {background: black; color: #2f90eb;}")
        self.Status_LCDDisplay2.setStyleSheet("QLCDNumber {background: black; color: #79baf7;}")
        self.Status_LCDDisplay3.setStyleSheet("QLCDNumber {background: black; color: #dcf1f7;}")
    
    def TE_UpdateLCD(self):
        self.TE_GetDocumentStatus()
        self.Status_LCDDisplay0.display(self._TE_AppVariables.DocumentStatus["line"])
        self.Status_LCDDisplay1.display(self._TE_AppVariables.DocumentStatus["column"])
        self.Status_LCDDisplay2.display(self._TE_AppVariables.DocumentStatus["char"])
        self.Status_LCDDisplay3.display(self._TE_AppVariables.DocumentStatus["word"])
    
    # Functions for menu bar commands
    
    def TE_SetMenuBar(self):
        
        def SetAction_SyntaxHighlighting():
            self.actionSH_PlainText.triggered.connect(lambda: self.TE_SetSyntaxHighlighting(TE_HighlightStyle.PlainText))
            self.actionSH_Python.triggered.connect(lambda: self.TE_SetSyntaxHighlighting(TE_HighlightStyle.Python))
            self.TE_SyntaxHlActionGroup.addAction(self.actionSH_PlainText)
            self.TE_SyntaxHlActionGroup.addAction(self.actionSH_Python)
            self.TE_SyntaxHlActionGroup.setExclusive(True)
        
        SetAction_SyntaxHighlighting()
    
    # Functions for working with directories
    
    def TE_ShowDirectory(self, directory: str = QtCore.QDir.current()):
        self.CWD_DirInput.setText(directory.dirName())
        self.FileView_TableWidget.clearContents()
        FileList = directory.entryInfoList()
        for idx, file in enumerate(FileList):
            self.FileView_TableWidget.insertRow(idx)
            self.FileView_TableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(file.fileName()))
            self.FileView_TableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(file.completeSuffix()))
            self.FileView_TableWidget.setItem(idx, 2, QtWidgets.QTableWidgetItem("Yes" if file.isDir() else "No"))
            self.FileView_TableWidget.setItem(idx, 3, QtWidgets.QTableWidgetItem(str(file.size())))
            self.FileView_TableWidget.setItem(idx, 4, QtWidgets.QTableWidgetItem(file.owner()))
            self.FileView_TableWidget.setItem(idx, 5, QtWidgets.QTableWidgetItem(str(file.ownerId())))
    
    # Functions for plain text widget
    
    def TE_GetDocumentStatus(self):
        cursor = self.TextEditor_MainWidget.textCursor()
        y, x = cursor.blockNumber() + 1, cursor.position() + 1
        self._TE_AppVariables.DocumentStatus["line"] = y
        self._TE_AppVariables.DocumentStatus["column"] = x
        self._TE_AppVariables.DocumentStatus["char"] = len(self.TextEditor_MainWidget.toPlainText())
        self._TE_AppVariables.DocumentStatus["word"] = len(re.split("\\s", self.TextEditor_MainWidget.toPlainText()))
    
    def TE_SetIndentationSpace(self, width: int):
        Font = self.TextEditor_MainWidget.font()
        FontMetrics = QtGui.QFontMetricsF(Font)
        WhitespaceWidth = FontMetrics.width(" ")
        self.TextEditor_MainWidget.setTabStopDistance(WhitespaceWidth*width)
    
    def TE_SetSyntaxHighlighting(self, arg: int):
        self.highlighter = TE_Highlighter(arg, self.TextEditor_MainWidget.document())
        self.TE_SetSyntaxHighlightingText(arg)
    
    def TE_SetSyntaxHighlightingText(self, arg: int):
        match arg:
            case TE_HighlightStyle.PlainText:
                self.Status_LanguageLabel.setText("Plain text")
            case TE_HighlightStyle.Python:
                self.Status_LanguageLabel.setText("Python")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())