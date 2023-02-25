from PyQt5 import QtWidgets, QtCore, QtGui
from ui.TextEditorUI import Ui_MainWindow
from text_ed_utils.CustomiseEditor import TE_CustomiseEditorWidget
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
        
        CurrentWorkspaceName: str = "Untitled"
        
        DocumentBuffer: dict[str, str] = {
            "saved": "",
            "active": ""
        }
        
        DocumentStatus: dict[str, int] = {
            "line": 1,
            "column": 1,
            "char": 0,
            "word": 0
        }
        
        CurrentFontSize = 11
        CurrentIndentationSpace = 4
        
        # BlockPosition = [[line, col], [line, col]]
        BlockPosition = [[None, None], [None, None]]
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.TE_DisplayTitle()
        self.TE_UpdateTimeInBackground()
        self.TE_ShowDirectory()
        self.TE_SetMenuBar()
        self.TE_SetLCDWidgets()
        self.TE_ConnectSignals()
        
        self.TE_SetIndentationSpace(4)
        self.TE_SetSyntaxHighlighting(TE_HighlightStyle.PlainText)
        self.highlighter = None
    
    def TE_ConnectSignals(self):
        
        def ConnectTextChangedSignal():
            self.TextEditor_MainWidget.textChanged.connect(self.TE_UpdateLCD)
            self.TextEditor_MainWidget.cursorPositionChanged.connect(self.TE_UpdateLCD)
            self.TextEditor_MainWidget.cursorPositionChanged.connect(self.TE_UpdateProgressBar)
        
        ConnectTextChangedSignal()
    
    # Functions for main window
    
    def TE_DisplayTitle(self):
        filename = self._TE_AppVariables.CurrentWorkspaceName
        self.setWindowTitle(self._TE_AppVariables.WindowTitle.replace("$file", f"{filename}{'*' if not self.TE_FileSaved() else ''}"))
    
    def closeEvent(self, event):
        if not self.TE_FileSaved():
            filename = self._TE_AppVariables.CurrentWorkspaceName
            MessageBox = QtWidgets.QMessageBox()
            MessageBox.setTextFormat(QtCore.Qt.MarkdownText)
            MessageBox.setWindowTitle("Exiting the text editor so soon?")
            MessageBox.setText(f"**{filename}** is modified.")
            MessageBox.setInformativeText(f"Are you sure you want to exit?\nAll unsaved changes to {filename} will be lost!\n\nPlease! *sniff* Please stay... it's just that I've never met someone like you...\nI want to hang out with you... for a little while...")
            MessageBox.setStandardButtons(QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Close | QtWidgets.QMessageBox.Cancel)
            MessageBox.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = MessageBox.exec()
            match ret:
                case QtWidgets.QMessageBox.Close:
                    event.accept()
                case _:
                    event.ignore()
    
    def TE_OpenCustomiseEditorWidget(self):
        self._TE_CEWidget = TE_CustomiseEditorWidget(
            self._TE_AppVariables.CurrentFontSize,
            self._TE_AppVariables.CurrentIndentationSpace
        )
        self._TE_CEWidget.output0.connect(self.TE_SetFontSize)
        self._TE_CEWidget.output1.connect(self.TE_SetIndentationSpace)
        self._TE_CEWidget.show()
    
    # Functions for displaying time (HH:MM:SS)
    
    def TE_DisplayTime(self, arg):
        self.Status_TimeLabel.setText(arg)
    
    def TE_UpdateTimeInBackground(self):
        self._TE_TimeThread = TE_TimeUpdate()
        self._TE_TimeThread.time.connect(self.TE_DisplayTime)
        self._TE_TimeThread.start()
    
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
        
        def SetAction_WordStarBlock():
            self.actionWSB_MarkBegin.triggered.connect(self.TE_MarkWSBegin)
            self.actionWSB_MarkEnd.triggered.connect(self.TE_MarkWSEnd)
        
        def SetAction_OpenCustomiseEditorWidget():
            self.actionSetFontSizeAndIndent.triggered.connect(self.TE_OpenCustomiseEditorWidget)
        
        def SetAction_SyntaxHighlighting():
            self.TE_SyntaxHlActionGroup = QtWidgets.QActionGroup(self)
            self.actionSH_PlainText.triggered.connect(lambda: self.TE_SetSyntaxHighlighting(TE_HighlightStyle.PlainText))
            self.actionSH_Python.triggered.connect(lambda: self.TE_SetSyntaxHighlighting(TE_HighlightStyle.Python))
            self.TE_SyntaxHlActionGroup.addAction(self.actionSH_PlainText)
            self.TE_SyntaxHlActionGroup.addAction(self.actionSH_Python)
            self.TE_SyntaxHlActionGroup.setExclusive(True)
        
        SetAction_OpenCustomiseEditorWidget()
        SetAction_SyntaxHighlighting()
        SetAction_WordStarBlock()
    
    # Functions for file handling
    
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
    
    def TE_FileSaved(self) -> bool:
        return self._TE_AppVariables.DocumentBuffer["active"] == self._TE_AppVariables.DocumentBuffer["saved"]
    
    # Functions for plain text widget
    
    def TE_GetDocumentStatus(self):
        cursor = self.TextEditor_MainWidget.textCursor()
        y, x = cursor.blockNumber() + 1, cursor.position() + 1
        self._TE_AppVariables.DocumentStatus["line"] = x
        self._TE_AppVariables.DocumentStatus["column"] = y
        self._TE_AppVariables.DocumentStatus["char"] = len(self.TextEditor_MainWidget.toPlainText())
        self._TE_AppVariables.DocumentStatus["word"] = len(re.split("\\s+", self.TextEditor_MainWidget.toPlainText().strip()))
        
        self._TE_AppVariables.DocumentBuffer["active"] = self.TextEditor_MainWidget.toPlainText()
    
    def TE_SetFontSize(self, point: int):
        self.TextEditor_MainWidget.setFont(QtGui.QFont("Monospace", point))
        self._TE_AppVariables.CurrentFontSize = point
    
    def TE_SetIndentationSpace(self, width: int):
        Font = self.TextEditor_MainWidget.font()
        FontMetrics = QtGui.QFontMetricsF(Font)
        WhitespaceWidth = FontMetrics.width(" ")
        self.TextEditor_MainWidget.setTabStopDistance(WhitespaceWidth*width)
        self._TE_AppVariables.CurrentIndentationSpace = width
    
    def TE_SetSyntaxHighlighting(self, arg: int):
        self.highlighter = TE_Highlighter(arg, self.TextEditor_MainWidget.document())
        self.TE_SetSyntaxHighlightingText(arg)
    
    def TE_SetSyntaxHighlightingText(self, arg: int):
        match arg:
            case TE_HighlightStyle.PlainText:
                self.Status_LanguageLabel.setText("Plain text")
            case TE_HighlightStyle.Python:
                self.Status_LanguageLabel.setText("Python")
    
    def TE_UpdateProgressBar(self):
        DocumentLength = len(self.TextEditor_MainWidget.toPlainText())
        CursorPosition = self.TextEditor_MainWidget.textCursor().position()
        self.Misc_ProgressBar.setMaximum(DocumentLength)
        self.Misc_ProgressBar.setValue(CursorPosition)
    
    # Function for working with WordStar blocks
    
    def TE_ShowWSBlockStatus(self):
        position = self._TE_AppVariables.BlockPosition
        self.Misc_WordStarBlockLabel.setText(f"WordStar block at ({position[0][0]}:{position[0][1]});({position[1][0]}:{position[1][1]})")
    
    def TE_MarkWSBegin(self):
        CurrentPosition = [self.TextEditor_MainWidget.textCursor().blockNumber(), self.TextEditor_MainWidget.textCursor().position()]
        self._TE_AppVariables.BlockPosition[0] = CurrentPosition
        self.TE_ShowWSBlockStatus()
    
    def TE_MarkWSEnd(self):
        CurrentPosition = [self.TextEditor_MainWidget.textCursor().blockNumber(), self.TextEditor_MainWidget.textCursor().position()]
        self._TE_AppVariables.BlockPosition[1] = CurrentPosition
        self.TE_ShowWSBlockStatus()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())