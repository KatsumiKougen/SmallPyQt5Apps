# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TextEditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 568)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.StatusLayout = QtWidgets.QHBoxLayout()
        self.StatusLayout.setObjectName("StatusLayout")
        self.Status_TextEdModeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status_TextEdModeLabel.sizePolicy().hasHeightForWidth())
        self.Status_TextEdModeLabel.setSizePolicy(sizePolicy)
        self.Status_TextEdModeLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.Status_TextEdModeLabel.setObjectName("Status_TextEdModeLabel")
        self.StatusLayout.addWidget(self.Status_TextEdModeLabel)
        self.Status_VLine0 = QtWidgets.QFrame(self.centralwidget)
        self.Status_VLine0.setFrameShape(QtWidgets.QFrame.VLine)
        self.Status_VLine0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Status_VLine0.setObjectName("Status_VLine0")
        self.StatusLayout.addWidget(self.Status_VLine0)
        self.Status_FileNameLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status_FileNameLabel.sizePolicy().hasHeightForWidth())
        self.Status_FileNameLabel.setSizePolicy(sizePolicy)
        self.Status_FileNameLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.Status_FileNameLabel.setObjectName("Status_FileNameLabel")
        self.StatusLayout.addWidget(self.Status_FileNameLabel)
        self.Status_VLine1 = QtWidgets.QFrame(self.centralwidget)
        self.Status_VLine1.setFrameShape(QtWidgets.QFrame.VLine)
        self.Status_VLine1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Status_VLine1.setObjectName("Status_VLine1")
        self.StatusLayout.addWidget(self.Status_VLine1)
        self.Status_StatusLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status_StatusLabel.sizePolicy().hasHeightForWidth())
        self.Status_StatusLabel.setSizePolicy(sizePolicy)
        self.Status_StatusLabel.setObjectName("Status_StatusLabel")
        self.StatusLayout.addWidget(self.Status_StatusLabel)
        self.Status_LCDLayout = QtWidgets.QHBoxLayout()
        self.Status_LCDLayout.setObjectName("Status_LCDLayout")
        self.Status_LCDDisplay1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.Status_LCDDisplay1.setFrameShape(QtWidgets.QFrame.Box)
        self.Status_LCDDisplay1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Status_LCDDisplay1.setSmallDecimalPoint(False)
        self.Status_LCDDisplay1.setProperty("intValue", 1)
        self.Status_LCDDisplay1.setObjectName("Status_LCDDisplay1")
        self.Status_LCDLayout.addWidget(self.Status_LCDDisplay1)
        self.Status_LCDDisplay0 = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status_LCDDisplay0.sizePolicy().hasHeightForWidth())
        self.Status_LCDDisplay0.setSizePolicy(sizePolicy)
        self.Status_LCDDisplay0.setProperty("intValue", 1)
        self.Status_LCDDisplay0.setObjectName("Status_LCDDisplay0")
        self.Status_LCDLayout.addWidget(self.Status_LCDDisplay0)
        self.Status_LCDDisplay2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.Status_LCDDisplay2.setObjectName("Status_LCDDisplay2")
        self.Status_LCDLayout.addWidget(self.Status_LCDDisplay2)
        self.Status_LCDDisplay3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.Status_LCDDisplay3.setObjectName("Status_LCDDisplay3")
        self.Status_LCDLayout.addWidget(self.Status_LCDDisplay3)
        self.StatusLayout.addLayout(self.Status_LCDLayout)
        self.Status_VLine2 = QtWidgets.QFrame(self.centralwidget)
        self.Status_VLine2.setFrameShape(QtWidgets.QFrame.VLine)
        self.Status_VLine2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Status_VLine2.setObjectName("Status_VLine2")
        self.StatusLayout.addWidget(self.Status_VLine2)
        self.Status_LanguageLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status_LanguageLabel.sizePolicy().hasHeightForWidth())
        self.Status_LanguageLabel.setSizePolicy(sizePolicy)
        self.Status_LanguageLabel.setObjectName("Status_LanguageLabel")
        self.StatusLayout.addWidget(self.Status_LanguageLabel)
        self.Status_VLine3 = QtWidgets.QFrame(self.centralwidget)
        self.Status_VLine3.setFrameShape(QtWidgets.QFrame.VLine)
        self.Status_VLine3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Status_VLine3.setObjectName("Status_VLine3")
        self.StatusLayout.addWidget(self.Status_VLine3)
        self.Status_TimeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Status_TimeLabel.sizePolicy().hasHeightForWidth())
        self.Status_TimeLabel.setSizePolicy(sizePolicy)
        self.Status_TimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Status_TimeLabel.setObjectName("Status_TimeLabel")
        self.StatusLayout.addWidget(self.Status_TimeLabel)
        self.verticalLayout_2.addLayout(self.StatusLayout)
        self.TextEditorLayout = QtWidgets.QHBoxLayout()
        self.TextEditorLayout.setObjectName("TextEditorLayout")
        self.FileViewLayout = QtWidgets.QVBoxLayout()
        self.FileViewLayout.setContentsMargins(-1, -1, 0, -1)
        self.FileViewLayout.setObjectName("FileViewLayout")
        self.FileView_CurrentDirLabel = QtWidgets.QLabel(self.centralwidget)
        self.FileView_CurrentDirLabel.setTextFormat(QtCore.Qt.RichText)
        self.FileView_CurrentDirLabel.setObjectName("FileView_CurrentDirLabel")
        self.FileViewLayout.addWidget(self.FileView_CurrentDirLabel)
        self.FileView_CWDLayout = QtWidgets.QHBoxLayout()
        self.FileView_CWDLayout.setObjectName("FileView_CWDLayout")
        self.CWD_DirInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CWD_DirInput.sizePolicy().hasHeightForWidth())
        self.CWD_DirInput.setSizePolicy(sizePolicy)
        self.CWD_DirInput.setObjectName("CWD_DirInput")
        self.FileView_CWDLayout.addWidget(self.CWD_DirInput)
        self.CWD_Button = QtWidgets.QPushButton(self.centralwidget)
        self.CWD_Button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CWD_Button.sizePolicy().hasHeightForWidth())
        self.CWD_Button.setSizePolicy(sizePolicy)
        self.CWD_Button.setMinimumSize(QtCore.QSize(0, 0))
        self.CWD_Button.setSizeIncrement(QtCore.QSize(0, 0))
        self.CWD_Button.setBaseSize(QtCore.QSize(0, 0))
        self.CWD_Button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.CWD_Button.setObjectName("CWD_Button")
        self.FileView_CWDLayout.addWidget(self.CWD_Button)
        self.FileViewLayout.addLayout(self.FileView_CWDLayout)
        self.FileView_TableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileView_TableWidget.sizePolicy().hasHeightForWidth())
        self.FileView_TableWidget.setSizePolicy(sizePolicy)
        self.FileView_TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.FileView_TableWidget.setObjectName("FileView_TableWidget")
        self.FileView_TableWidget.setColumnCount(6)
        self.FileView_TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.FileView_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FileView_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.FileView_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.FileView_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.FileView_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Space Grotesk")
        font.setItalic(False)
        item.setFont(font)
        self.FileView_TableWidget.setHorizontalHeaderItem(5, item)
        self.FileView_TableWidget.horizontalHeader().setMinimumSectionSize(23)
        self.FileViewLayout.addWidget(self.FileView_TableWidget)
        self.TextEditorLayout.addLayout(self.FileViewLayout)
        self.TextEditor_VertLayout = QtWidgets.QVBoxLayout()
        self.TextEditor_VertLayout.setObjectName("TextEditor_VertLayout")
        self.TextEditor_MainWidget = TE_CustomPlainTextEdit(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(141, 210, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 22, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 170, 172, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 210, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 22, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.TextEditor_MainWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.TextEditor_MainWidget.setFont(font)
        self.TextEditor_MainWidget.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.TextEditor_MainWidget.setTabStopWidth(40)
        self.TextEditor_MainWidget.setObjectName("TextEditor_MainWidget")
        self.TextEditor_VertLayout.addWidget(self.TextEditor_MainWidget)
        self.TextEditor_MiscLayout = QtWidgets.QHBoxLayout()
        self.TextEditor_MiscLayout.setObjectName("TextEditor_MiscLayout")
        self.Misc_ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 249, 114))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 249, 114))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.Misc_ProgressBar.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Misc_ProgressBar.setFont(font)
        self.Misc_ProgressBar.setProperty("value", 0)
        self.Misc_ProgressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Misc_ProgressBar.setTextVisible(False)
        self.Misc_ProgressBar.setInvertedAppearance(False)
        self.Misc_ProgressBar.setObjectName("Misc_ProgressBar")
        self.TextEditor_MiscLayout.addWidget(self.Misc_ProgressBar)
        self.Misc_WordStarBlockLabel = QtWidgets.QLabel(self.centralwidget)
        self.Misc_WordStarBlockLabel.setObjectName("Misc_WordStarBlockLabel")
        self.TextEditor_MiscLayout.addWidget(self.Misc_WordStarBlockLabel)
        self.TextEditor_VertLayout.addLayout(self.TextEditor_MiscLayout)
        self.TextEditorLayout.addLayout(self.TextEditor_VertLayout)
        self.verticalLayout_2.addLayout(self.TextEditorLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWordStarBlocks = QtWidgets.QMenu(self.menuEdit)
        self.menuWordStarBlocks.setObjectName("menuWordStarBlocks")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSyntaxHighlighting = QtWidgets.QMenu(self.menuView)
        self.menuSyntaxHighlighting.setObjectName("menuSyntaxHighlighting")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuInsertBracket = QtWidgets.QMenu(self.menuTool)
        self.menuInsertBracket.setObjectName("menuInsertBracket")
        self.menu_Spawn_points = QtWidgets.QMenu(self.menuTool)
        self.menu_Spawn_points.setObjectName("menu_Spawn_points")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSH_PlainText = QtWidgets.QAction(MainWindow)
        self.actionSH_PlainText.setCheckable(True)
        self.actionSH_PlainText.setChecked(True)
        self.actionSH_PlainText.setObjectName("actionSH_PlainText")
        self.actionSH_Python = QtWidgets.QAction(MainWindow)
        self.actionSH_Python.setCheckable(True)
        self.actionSH_Python.setObjectName("actionSH_Python")
        self.actionSetFontSizeAndIndent = QtWidgets.QAction(MainWindow)
        self.actionSetFontSizeAndIndent.setObjectName("actionSetFontSizeAndIndent")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelectAll = QtWidgets.QAction(MainWindow)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionFindAndReplace = QtWidgets.QAction(MainWindow)
        self.actionFindAndReplace.setObjectName("actionFindAndReplace")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionToggleInsertOverwriteMode = QtWidgets.QAction(MainWindow)
        self.actionToggleInsertOverwriteMode.setObjectName("actionToggleInsertOverwriteMode")
        self.actionIB_RoundBracket = QtWidgets.QAction(MainWindow)
        self.actionIB_RoundBracket.setObjectName("actionIB_RoundBracket")
        self.actionIB_SquareBracket = QtWidgets.QAction(MainWindow)
        self.actionIB_SquareBracket.setObjectName("actionIB_SquareBracket")
        self.actionIB_CurlyBracket = QtWidgets.QAction(MainWindow)
        self.actionIB_CurlyBracket.setObjectName("actionIB_CurlyBracket")
        self.actionIB_AngleBracket = QtWidgets.QAction(MainWindow)
        self.actionIB_AngleBracket.setObjectName("actionIB_AngleBracket")
        self.actionIB_SingleQuote = QtWidgets.QAction(MainWindow)
        self.actionIB_SingleQuote.setObjectName("actionIB_SingleQuote")
        self.actionIB_DoubleQuote = QtWidgets.QAction(MainWindow)
        self.actionIB_DoubleQuote.setObjectName("actionIB_DoubleQuote")
        self.actionIB_Guillemet = QtWidgets.QAction(MainWindow)
        self.actionIB_Guillemet.setObjectName("actionIB_Guillemet")
        self.actionSP_AddSpawnPoint = QtWidgets.QAction(MainWindow)
        self.actionSP_AddSpawnPoint.setObjectName("actionSP_AddSpawnPoint")
        self.actionSP_ClearAllSpawnPoints = QtWidgets.QAction(MainWindow)
        self.actionSP_ClearAllSpawnPoints.setObjectName("actionSP_ClearAllSpawnPoints")
        self.actionSP_SpawnPoint0 = QtWidgets.QAction(MainWindow)
        self.actionSP_SpawnPoint0.setObjectName("actionSP_SpawnPoint0")
        self.actionSP_SpawnPoint1 = QtWidgets.QAction(MainWindow)
        self.actionSP_SpawnPoint1.setObjectName("actionSP_SpawnPoint1")
        self.actionSP_SpawnPoint2 = QtWidgets.QAction(MainWindow)
        self.actionSP_SpawnPoint2.setObjectName("actionSP_SpawnPoint2")
        self.actionSP_SpawnPoint3 = QtWidgets.QAction(MainWindow)
        self.actionSP_SpawnPoint3.setObjectName("actionSP_SpawnPoint3")
        self.actionSP_SpawnPoint4 = QtWidgets.QAction(MainWindow)
        self.actionSP_SpawnPoint4.setObjectName("actionSP_SpawnPoint4")
        self.actionSP_SpawnPoint5 = QtWidgets.QAction(MainWindow)
        self.actionSP_SpawnPoint5.setObjectName("actionSP_SpawnPoint5")
        self.actionSP_SpawnPoint6 = QtWidgets.QAction(MainWindow)
        self.actionSP_SpawnPoint6.setObjectName("actionSP_SpawnPoint6")
        self.actionSP_SpawnPoint7 = QtWidgets.QAction(MainWindow)
        self.actionSP_SpawnPoint7.setObjectName("actionSP_SpawnPoint7")
        self.actionDefine_a_Python_function = QtWidgets.QAction(MainWindow)
        self.actionDefine_a_Python_function.setObjectName("actionDefine_a_Python_function")
        self.actionDefineFunction = QtWidgets.QAction(MainWindow)
        self.actionDefineFunction.setObjectName("actionDefineFunction")
        self.actionDefineClass = QtWidgets.QAction(MainWindow)
        self.actionDefineClass.setObjectName("actionDefineClass")
        self.actionMark_begin = QtWidgets.QAction(MainWindow)
        self.actionMark_begin.setObjectName("actionMark_begin")
        self.actionMark_end = QtWidgets.QAction(MainWindow)
        self.actionMark_end.setObjectName("actionMark_end")
        self.actionWSB_MarkBegin = QtWidgets.QAction(MainWindow)
        self.actionWSB_MarkBegin.setObjectName("actionWSB_MarkBegin")
        self.actionWSB_MarkEnd = QtWidgets.QAction(MainWindow)
        self.actionWSB_MarkEnd.setObjectName("actionWSB_MarkEnd")
        self.actionWSB_Copy = QtWidgets.QAction(MainWindow)
        self.actionWSB_Copy.setObjectName("actionWSB_Copy")
        self.actionWSB_Move = QtWidgets.QAction(MainWindow)
        self.actionWSB_Move.setObjectName("actionWSB_Move")
        self.actionWSB_Delete = QtWidgets.QAction(MainWindow)
        self.actionWSB_Delete.setObjectName("actionWSB_Delete")
        self.actionIndent_more = QtWidgets.QAction(MainWindow)
        self.actionIndent_more.setObjectName("actionIndent_more")
        self.actionIndent_less = QtWidgets.QAction(MainWindow)
        self.actionIndent_less.setObjectName("actionIndent_less")
        self.actionIndentMore = QtWidgets.QAction(MainWindow)
        self.actionIndentMore.setObjectName("actionIndentMore")
        self.actionIndentLess = QtWidgets.QAction(MainWindow)
        self.actionIndentLess.setObjectName("actionIndentLess")
        self.actionWSB_ViewBlock = QtWidgets.QAction(MainWindow)
        self.actionWSB_ViewBlock.setObjectName("actionWSB_ViewBlock")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuWordStarBlocks.addAction(self.actionWSB_MarkBegin)
        self.menuWordStarBlocks.addAction(self.actionWSB_MarkEnd)
        self.menuWordStarBlocks.addAction(self.actionWSB_Copy)
        self.menuWordStarBlocks.addAction(self.actionWSB_Move)
        self.menuWordStarBlocks.addAction(self.actionWSB_Delete)
        self.menuWordStarBlocks.addSeparator()
        self.menuWordStarBlocks.addAction(self.actionWSB_ViewBlock)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addAction(self.actionFindAndReplace)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuWordStarBlocks.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionIndentMore)
        self.menuEdit.addAction(self.actionIndentLess)
        self.menuSyntaxHighlighting.addAction(self.actionSH_PlainText)
        self.menuSyntaxHighlighting.addSeparator()
        self.menuSyntaxHighlighting.addAction(self.actionSH_Python)
        self.menuView.addAction(self.menuSyntaxHighlighting.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionSetFontSizeAndIndent)
        self.menuInsertBracket.addAction(self.actionIB_RoundBracket)
        self.menuInsertBracket.addAction(self.actionIB_SquareBracket)
        self.menuInsertBracket.addAction(self.actionIB_CurlyBracket)
        self.menuInsertBracket.addAction(self.actionIB_AngleBracket)
        self.menuInsertBracket.addSeparator()
        self.menuInsertBracket.addAction(self.actionIB_SingleQuote)
        self.menuInsertBracket.addAction(self.actionIB_DoubleQuote)
        self.menuInsertBracket.addAction(self.actionIB_Guillemet)
        self.menu_Spawn_points.addAction(self.actionSP_AddSpawnPoint)
        self.menu_Spawn_points.addAction(self.actionSP_ClearAllSpawnPoints)
        self.menu_Spawn_points.addSeparator()
        self.menu_Spawn_points.addAction(self.actionSP_SpawnPoint0)
        self.menu_Spawn_points.addAction(self.actionSP_SpawnPoint1)
        self.menu_Spawn_points.addAction(self.actionSP_SpawnPoint2)
        self.menu_Spawn_points.addAction(self.actionSP_SpawnPoint3)
        self.menu_Spawn_points.addAction(self.actionSP_SpawnPoint4)
        self.menu_Spawn_points.addAction(self.actionSP_SpawnPoint5)
        self.menu_Spawn_points.addAction(self.actionSP_SpawnPoint6)
        self.menu_Spawn_points.addAction(self.actionSP_SpawnPoint7)
        self.menuTool.addAction(self.actionToggleInsertOverwriteMode)
        self.menuTool.addSeparator()
        self.menuTool.addAction(self.menuInsertBracket.menuAction())
        self.menuTool.addAction(self.menu_Spawn_points.menuAction())
        self.menuTool.addSeparator()
        self.menuTool.addAction(self.actionDefineFunction)
        self.menuTool.addAction(self.actionDefineClass)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionCut.triggered.connect(self.TextEditor_MainWidget.cut) # type: ignore
        self.actionCopy.triggered.connect(self.TextEditor_MainWidget.copy) # type: ignore
        self.actionPaste.triggered.connect(self.TextEditor_MainWidget.paste) # type: ignore
        self.actionSelectAll.triggered.connect(self.TextEditor_MainWidget.selectAll) # type: ignore
        self.actionUndo.triggered.connect(self.TextEditor_MainWidget.undo) # type: ignore
        self.actionRedo.triggered.connect(self.TextEditor_MainWidget.redo) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Status_TextEdModeLabel.setText(_translate("MainWindow", "`I`"))
        self.Status_FileNameLabel.setText(_translate("MainWindow", "File: **Untitled**"))
        self.Status_StatusLabel.setText(_translate("MainWindow", "Ln/Col/Char/Word"))
        self.Status_LanguageLabel.setText(_translate("MainWindow", "Brainslag"))
        self.Status_TimeLabel.setText(_translate("MainWindow", "00:00:00"))
        self.FileView_CurrentDirLabel.setText(_translate("MainWindow", "<html><head/><body><p>Current working directory</p></body></html>"))
        self.CWD_Button.setText(_translate("MainWindow", "Open"))
        item = self.FileView_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File"))
        item = self.FileView_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Extension"))
        item = self.FileView_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Is directory"))
        item = self.FileView_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Size"))
        item = self.FileView_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Owner"))
        item = self.FileView_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Owner ID"))
        self.Misc_ProgressBar.setFormat(_translate("MainWindow", "%m/%p"))
        self.Misc_WordStarBlockLabel.setText(_translate("MainWindow", "WordStar block at (None:None);(None:None)"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuWordStarBlocks.setTitle(_translate("MainWindow", "&WordStar blocks..."))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuSyntaxHighlighting.setTitle(_translate("MainWindow", "Synta&x highlighting"))
        self.menuTool.setTitle(_translate("MainWindow", "&Tool"))
        self.menuInsertBracket.setTitle(_translate("MainWindow", "Insert &bracket..."))
        self.menu_Spawn_points.setTitle(_translate("MainWindow", "&Spawn points"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionNew.setText(_translate("MainWindow", "&New"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save &as"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionSH_PlainText.setText(_translate("MainWindow", "Plain text"))
        self.actionSH_Python.setText(_translate("MainWindow", "Python"))
        self.actionSetFontSizeAndIndent.setText(_translate("MainWindow", "Set font size and i&ndent"))
        self.actionUndo.setText(_translate("MainWindow", "&Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "&Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionCut.setText(_translate("MainWindow", "Cu&t"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "&Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "&Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionDelete.setText(_translate("MainWindow", "&Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del"))
        self.actionSelectAll.setText(_translate("MainWindow", "Select &all"))
        self.actionSelectAll.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionFindAndReplace.setText(_translate("MainWindow", "&Find and replace..."))
        self.actionFindAndReplace.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionToggleInsertOverwriteMode.setText(_translate("MainWindow", "To&ggle insert/overwrite mode"))
        self.actionToggleInsertOverwriteMode.setShortcut(_translate("MainWindow", "Ins"))
        self.actionIB_RoundBracket.setText(_translate("MainWindow", "Round bracket ()"))
        self.actionIB_RoundBracket.setShortcut(_translate("MainWindow", "Ctrl+L, 9"))
        self.actionIB_SquareBracket.setText(_translate("MainWindow", "Square bracket []"))
        self.actionIB_SquareBracket.setShortcut(_translate("MainWindow", "Ctrl+L, ["))
        self.actionIB_CurlyBracket.setText(_translate("MainWindow", "Curly bracket {}"))
        self.actionIB_CurlyBracket.setShortcut(_translate("MainWindow", "Ctrl+L, {"))
        self.actionIB_AngleBracket.setText(_translate("MainWindow", "Angle bracket <>"))
        self.actionIB_AngleBracket.setShortcut(_translate("MainWindow", "Ctrl+L, ,"))
        self.actionIB_SingleQuote.setText(_translate("MainWindow", "Single quote \'\'"))
        self.actionIB_SingleQuote.setShortcut(_translate("MainWindow", "Ctrl+L, I"))
        self.actionIB_DoubleQuote.setText(_translate("MainWindow", "Double quote \"\""))
        self.actionIB_DoubleQuote.setShortcut(_translate("MainWindow", "Ctrl+L, O"))
        self.actionIB_Guillemet.setText(_translate("MainWindow", "Guillemet «»"))
        self.actionIB_Guillemet.setShortcut(_translate("MainWindow", "Ctrl+L, P"))
        self.actionSP_AddSpawnPoint.setText(_translate("MainWindow", "Add spawn &point"))
        self.actionSP_AddSpawnPoint.setShortcut(_translate("MainWindow", "Ctrl+M, A"))
        self.actionSP_ClearAllSpawnPoints.setText(_translate("MainWindow", "Clear &all spawn points"))
        self.actionSP_ClearAllSpawnPoints.setShortcut(_translate("MainWindow", "Ctrl+M, X"))
        self.actionSP_SpawnPoint0.setText(_translate("MainWindow", "Spawn point 0"))
        self.actionSP_SpawnPoint0.setShortcut(_translate("MainWindow", "Ctrl+M, 0"))
        self.actionSP_SpawnPoint1.setText(_translate("MainWindow", "Spawn point 1"))
        self.actionSP_SpawnPoint1.setShortcut(_translate("MainWindow", "Ctrl+M, 1"))
        self.actionSP_SpawnPoint2.setText(_translate("MainWindow", "Spawn point 2"))
        self.actionSP_SpawnPoint2.setShortcut(_translate("MainWindow", "Ctrl+M, 2"))
        self.actionSP_SpawnPoint3.setText(_translate("MainWindow", "Spawn point 3"))
        self.actionSP_SpawnPoint3.setShortcut(_translate("MainWindow", "Ctrl+M, 3"))
        self.actionSP_SpawnPoint4.setText(_translate("MainWindow", "Spawn point 4"))
        self.actionSP_SpawnPoint4.setShortcut(_translate("MainWindow", "Ctrl+M, 4"))
        self.actionSP_SpawnPoint5.setText(_translate("MainWindow", "Spawn point 5"))
        self.actionSP_SpawnPoint5.setShortcut(_translate("MainWindow", "Ctrl+M, 5"))
        self.actionSP_SpawnPoint6.setText(_translate("MainWindow", "Spawn point 6"))
        self.actionSP_SpawnPoint6.setShortcut(_translate("MainWindow", "Ctrl+M, 6"))
        self.actionSP_SpawnPoint7.setText(_translate("MainWindow", "Spawn point 7"))
        self.actionSP_SpawnPoint7.setShortcut(_translate("MainWindow", "Ctrl+M, 7"))
        self.actionDefine_a_Python_function.setText(_translate("MainWindow", "Define a Python function"))
        self.actionDefineFunction.setText(_translate("MainWindow", "Define a &function"))
        self.actionDefineClass.setText(_translate("MainWindow", "Define a &class"))
        self.actionMark_begin.setText(_translate("MainWindow", "Mark begin"))
        self.actionMark_end.setText(_translate("MainWindow", "Mark end"))
        self.actionWSB_MarkBegin.setText(_translate("MainWindow", "Mark begin position"))
        self.actionWSB_MarkBegin.setShortcut(_translate("MainWindow", "Ctrl+K, B"))
        self.actionWSB_MarkEnd.setText(_translate("MainWindow", "Mark end position"))
        self.actionWSB_MarkEnd.setShortcut(_translate("MainWindow", "Ctrl+K, K"))
        self.actionWSB_Copy.setText(_translate("MainWindow", "Copy block to cursor"))
        self.actionWSB_Copy.setShortcut(_translate("MainWindow", "Ctrl+K, C"))
        self.actionWSB_Move.setText(_translate("MainWindow", "Move block to cursor"))
        self.actionWSB_Move.setShortcut(_translate("MainWindow", "Ctrl+K, M"))
        self.actionWSB_Delete.setText(_translate("MainWindow", "Delete block"))
        self.actionWSB_Delete.setShortcut(_translate("MainWindow", "Ctrl+K, Y"))
        self.actionIndent_more.setText(_translate("MainWindow", "Indent more"))
        self.actionIndent_less.setText(_translate("MainWindow", "Indent less"))
        self.actionIndentMore.setText(_translate("MainWindow", "Indent &more"))
        self.actionIndentMore.setShortcut(_translate("MainWindow", "Ctrl+K, ,"))
        self.actionIndentLess.setText(_translate("MainWindow", "Indent &less"))
        self.actionIndentLess.setShortcut(_translate("MainWindow", "Ctrl+K, ."))
        self.actionWSB_ViewBlock.setText(_translate("MainWindow", "View block"))
        self.actionWSB_ViewBlock.setShortcut(_translate("MainWindow", "Ctrl+K, Shift+L"))
from highlighter.parenmatch import TE_CustomPlainTextEdit
