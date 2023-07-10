from PyQt5 import QtWidgets, QtCore, QtGui
from ui.TextEditorUI import Ui_MainWindow
from text_ed_utils.CustomiseEditor import TE_CustomiseEditorDialog
from text_ed_utils.ViewBlock import TE_ViewBlockDialog
from highlighter.highlighter import *
import sys, time, re, os
from typing import Union
from datetime import datetime

match os.name:
    case "posix": # UNIX or Linux-based OS
        TE_DirectorySeparator = "/"
    case "nt": # Windows
        TE_DirectorySeparator = "\\"

class TE_TimeUpdate(QtCore.QThread):
    
    time = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            cur = datetime.now().strftime("%H:%M:%S")
            self.time.emit(cur)
            time.sleep(.001)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    class _TE_AppVariables:
        
        WindowTitle: str = "The text editor - $file" if os.name == "posix" else "The text editor ~ Windows Edition - $file"
        
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
        
        # BlockPosition = [[line, col, raw], [line, col, raw]]
        BlockPosition = [[None, None, 0], [None, None, 0]]
        BlockContent = None
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.TE_DisplayTitle()
        self.TE_UpdateTimeInBackground()
        self.TE_SetMenuBar()
        self.TE_SetLCDWidgets()
        self.TE_ConnectSignals()
        self.TE_ShowWSBlockStatus()
        
        self.TE_SetIndentationSpace(4)
        self.TE_SetSyntaxHighlighting(TE_HighlightStyle.PlainText)
        self.highlighter = None
    
    def TE_ConnectSignals(self):
        
        def ConnectTextChangedSignal():
            self.TextEditor_MainWidget.textChanged.connect(self.TE_UpdateLCD)
            self.TextEditor_MainWidget.textChanged.connect(self.TE_DisplayTitle)
        
        def ConnectCursorPosChangedSignal():
            self.TextEditor_MainWidget.cursorPositionChanged.connect(self.TE_UpdateLCD)
            self.TextEditor_MainWidget.cursorPositionChanged.connect(self.TE_UpdateProgressBar)
        
        ConnectTextChangedSignal()
        ConnectCursorPosChangedSignal()
    
    # Functions for main window
    
    def TE_DisplayTitle(self):
        CurrentFileName = self._TE_AppVariables.CurrentWorkspaceName
        self.setWindowTitle(self._TE_AppVariables.WindowTitle.replace("$file", f"{CurrentFileName}{'*' if not self.TE_FileSaved() else ''}"))
    
    def closeEvent(self, event):
        if not self.TE_FileSaved():
            CurrentFileName = self._TE_AppVariables.CurrentWorkspaceName
            MessageBox = QtWidgets.QMessageBox()
            MessageBox.setTextFormat(QtCore.Qt.MarkdownText)
            MessageBox.setWindowTitle("Exiting the text editor so soon?")
            MessageBox.setText(f"**{CurrentFileName}** is modified.")
            MessageBox.setInformativeText(
                f"Are you sure you want to exit?\n"
                f"All unsaved changes to {CurrentFileName} will be lost!\n"
                "\n"
                "Please! *sniff* Please stay... it's just that I've never met someone like you...\n"
                "I want to hang out with you... for a little while..."
            )
            MessageBox.setStandardButtons(QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Close | QtWidgets.QMessageBox.Cancel)
            MessageBox.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = MessageBox.exec()
            match ret:
                case QtWidgets.QMessageBox.Close:
                    event.accept()
                case _:
                    event.ignore()
    
    # Functions for extra dialogs
    
    def TE_OpenCustomiseEditorDialog(self):
        self._TE_CEDialog = TE_CustomiseEditorDialog(
            self._TE_AppVariables.CurrentFontSize,
            self._TE_AppVariables.CurrentIndentationSpace
        )
        self._TE_CEDialog.output0.connect(self.TE_SetFontSize)
        self._TE_CEDialog.output1.connect(self.TE_SetIndentationSpace)
        self._TE_CEDialog.show()
    
    def TE_OpenViewBlockDialog(self):
        self._TE_VBDialog = TE_ViewBlockDialog(self._TE_AppVariables.BlockContent)
        self._TE_VBDialog.show()
    
    def TE_OpenSaveFileDialog(self, mode: int = 0):
        CurrentBuffer = self._TE_AppVariables.DocumentBuffer
        if not os.path.isfile(self._TE_AppVariables.CurrentWorkspaceName):
            SaveFileName = QtWidgets.QFileDialog.getSaveFileName(
                parent=self,
                caption="Save...",
                directory=self._TE_AppVariables.CurrentWorkspaceName,
                filter="All file formats (*.*);;Text file (*.txt);;Markdown document (*.md);;Python source code (*.py, *.py3, *.pyw, *.pyd)"
            )
            if SaveFileName != ("", ""):
                with open(SaveFileName[0], "w") as fo:
                    fo.write(CurrentBuffer["active"])
                self._TE_AppVariables.DocumentBuffer["saved"] = CurrentBuffer["active"]
                self._TE_AppVariables.CurrentWorkspaceName = SaveFileName[0].split(TE_DirectorySeparator)[-1]
                self.TE_DisplayTitle()
        else:
            CurrentFileName = self._TE_AppVariables.CurrentWorkspaceName
            with open(CurrentFileName, "w") as fo:
                fo.write(CurrentBuffer["active"])
            self._TE_AppVariables.DocumentBuffer["saved"] = CurrentBuffer["active"]
            self.TE_DisplayTitle()
    
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
        
        def SetAction_OpenAndSave():
            self.actionSave.triggered.connect(self.TE_OpenSaveFileDialog)
        
        def SetAction_OpenCustomiseEditorWidget():
            self.actionSetFontSizeAndIndent.triggered.connect(self.TE_OpenCustomiseEditorDialog)
        
        def SetAction_OverwriteMode():
            self.actionToggleInsertOverwriteMode.triggered.connect(self.TE_ToggleOverwrite)
        
        def SetAction_SyntaxHighlighting():
            self.TE_SyntaxHlActionGroup = QtWidgets.QActionGroup(self)
            self.actionSH_PlainText.triggered.connect(lambda: self.TE_SetSyntaxHighlighting(TE_HighlightStyle.PlainText))
            self.actionSH_Python.triggered.connect(lambda: self.TE_SetSyntaxHighlighting(TE_HighlightStyle.Python))
            self.TE_SyntaxHlActionGroup.addAction(self.actionSH_PlainText)
            self.TE_SyntaxHlActionGroup.addAction(self.actionSH_Python)
            self.TE_SyntaxHlActionGroup.setExclusive(True)
        
        def SetAction_WordStarBlock():
            self.actionWSB_MarkBegin.triggered.connect(self.TE_MarkWSBegin)
            self.actionWSB_MarkEnd.triggered.connect(self.TE_MarkWSEnd)
            self.actionWSB_ViewBlock.triggered.connect(self.TE_OpenViewBlockDialog)
            self.actionWSB_Copy.triggered.connect(self.TE_CopyWSBlock)
            self.actionWSB_Move.triggered.connect(self.TE_MoveWSBlock)
            self.actionWSB_Delete.triggered.connect(self.TE_DeleteWSBlock)
        
        SetAction_OpenAndSave()
        SetAction_OpenCustomiseEditorWidget()
        SetAction_OverwriteMode()
        SetAction_SyntaxHighlighting()
        SetAction_WordStarBlock()
    
    # Functions for file handling
    
    def TE_FileSaved(self) -> bool:
        return self._TE_AppVariables.DocumentBuffer["active"] == self._TE_AppVariables.DocumentBuffer["saved"] and os.path.isfile(self._TE_AppVariables.CurrentWorkspaceName)
    
    # Functions for plain text widget
    
    def TE_GetDocumentStatus(self):
        cursor = self.TextEditor_MainWidget.textCursor()
        y, x = cursor.blockNumber() + 1, cursor.positionInBlock() + 1
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
    
    def TE_ToggleOverwrite(self):
        if self.TextEditor_MainWidget.overwriteMode():
            self.TextEditor_MainWidget.setOverwriteMode(False)
            self.Status_TextEdModeLabel.setText(self._TE_AppVariables.TextEdInsertMode)
        else:
            self.TextEditor_MainWidget.setOverwriteMode(True)
            self.Status_TextEdModeLabel.setText(self._TE_AppVariables.TextEdOverwriteMode)
    
    def TE_UpdateProgressBar(self):
        DocumentLength = len(self.TextEditor_MainWidget.toPlainText())
        CursorPosition = self.TextEditor_MainWidget.textCursor().position()
        self.Misc_ProgressBar.setMaximum(DocumentLength)
        self.Misc_ProgressBar.setValue(CursorPosition)
    
    # Function for working with WordStar blocks
    
    def TE_WSBlockExists(self) -> bool:
        return [None, None, 0] not in self._TE_AppVariables.BlockPosition
    
    def TE_ShowWSBlockStatus(self):
        position = self._TE_AppVariables.BlockPosition
        if self.TE_WSBlockExists():
            self.Misc_WordStarBlockLabel.setText(f"WordStar block at ({position[0][0]}:{position[0][1]});({position[1][0]}:{position[1][1]})")
        else:
            self.Misc_WordStarBlockLabel.setText("No block")
    
    def TE_MarkWSBegin(self):
        NewBeginPosition = [
            self.TextEditor_MainWidget.textCursor().blockNumber(),
            self.TextEditor_MainWidget.textCursor().positionInBlock(),
            self.TextEditor_MainWidget.textCursor().position(),
        ]
        self._TE_AppVariables.BlockPosition[0] = NewBeginPosition
        BeginPosition, EndPosition = self._TE_AppVariables.BlockPosition[0], self._TE_AppVariables.BlockPosition[1]
        if BeginPosition[2] > EndPosition[2] and self.TE_WSBlockExists():
            self._TE_AppVariables.BlockPosition = [EndPosition, BeginPosition]
        if self.TE_WSBlockExists():
            self._TE_AppVariables.BlockContent = self.TextEditor_MainWidget.toPlainText()[self._TE_AppVariables.BlockPosition[0][2]:self._TE_AppVariables.BlockPosition[1][2]]
        self.TE_ShowWSBlockStatus()
    
    def TE_MarkWSEnd(self):
        NewEndPosition = [
            self.TextEditor_MainWidget.textCursor().blockNumber(),
            self.TextEditor_MainWidget.textCursor().positionInBlock(),
            self.TextEditor_MainWidget.textCursor().position(),
        ]
        self._TE_AppVariables.BlockPosition[1] = NewEndPosition
        BeginPosition, EndPosition = self._TE_AppVariables.BlockPosition[0], self._TE_AppVariables.BlockPosition[1]
        if BeginPosition[2] > EndPosition[2] and self.TE_WSBlockExists():
            self._TE_AppVariables.BlockPosition = [EndPosition, BeginPosition]
        if self.TE_WSBlockExists():
            self._TE_AppVariables.BlockContent = self.TextEditor_MainWidget.toPlainText()[self._TE_AppVariables.BlockPosition[0][2]:self._TE_AppVariables.BlockPosition[1][2]]
        self.TE_ShowWSBlockStatus()
    
    def TE_CopyWSBlock(self):
        self.TextEditor_MainWidget.insertPlainText(self._TE_AppVariables.BlockContent)
    
    def TE_MoveWSBlock(self):
        CurrentCursorPos = self.TextEditor_MainWidget.textCursor().position()
        InitialBlockPos = self._TE_AppVariables.BlockPosition[0][2]
        FinalBlockPos = self._TE_AppVariables.BlockPosition[1][2]
        self.TE_CopyWSBlock()
        if InitialBlockPos < CurrentCursorPos:
            Cursor = self.TextEditor_MainWidget.textCursor()
            Cursor.setPosition(InitialBlockPos)
            for i in self._TE_AppVariables.BlockContent:
                Cursor.deleteChar()
            Cursor.setPosition(CurrentCursorPos)
            self.TextEditor_MainWidget.setTextCursor(Cursor)
        elif InitialBlockPos > CurrentCursorPos:
            BlockLen = len(self._TE_AppVariables.BlockContent)
            Cursor = self.TextEditor_MainWidget.textCursor()
            Cursor.setPosition(FinalBlockPos+BlockLen)
            for i in self._TE_AppVariables.BlockContent:
                Cursor.deletePreviousChar()
            Cursor.setPosition(CurrentCursorPos+BlockLen)
            self.TextEditor_MainWidget.setTextCursor(Cursor)
    
    def TE_DeleteWSBlock(self):
        CurrentCursorPos = self.TextEditor_MainWidget.textCursor().position()
        InitialBlockPos = self._TE_AppVariables.BlockPosition[0][2]
        if InitialBlockPos < CurrentCursorPos:
            BlockLen = len(self._TE_AppVariables.BlockContent)
            Cursor = self.TextEditor_MainWidget.textCursor()
            Cursor.setPosition(InitialBlockPos)
            for i in self._TE_AppVariables.BlockContent:
                Cursor.deleteChar()
            Cursor.setPosition(CurrentCursorPos-BlockLen)
            self.TextEditor_MainWidget.setTextCursor(Cursor)
        elif InitialBlockPos > CurrentCursorPos:
            BlockLen = len(self._TE_AppVariables.BlockContent)
            Cursor = self.TextEditor_MainWidget.textCursor()
            Cursor.setPosition(InitialBlockPos)
            for i in self._TE_AppVariables.BlockContent:
                Cursor.deleteChar()
            Cursor.setPosition(CurrentCursorPos)
            self.TextEditor_MainWidget.setTextCursor(Cursor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
