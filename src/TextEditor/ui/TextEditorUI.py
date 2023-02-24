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
        MainWindow.resize(723, 510)
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
        self.TextEditorLayout.addWidget(self.TextEditor_MainWidget)
        self.verticalLayout_2.addLayout(self.TextEditorLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSyntaxHighlighting = QtWidgets.QMenu(self.menuView)
        self.menuSyntaxHighlighting.setObjectName("menuSyntaxHighlighting")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
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
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuSyntaxHighlighting.addAction(self.actionSH_PlainText)
        self.menuSyntaxHighlighting.addSeparator()
        self.menuSyntaxHighlighting.addAction(self.actionSH_Python)
        self.menuView.addAction(self.menuSyntaxHighlighting.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
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
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuSyntaxHighlighting.setTitle(_translate("MainWindow", "Synta&x highlighting"))
        self.menuTool.setTitle(_translate("MainWindow", "&Tool"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionNew.setText(_translate("MainWindow", "&New"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save &as"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionSH_PlainText.setText(_translate("MainWindow", "Plain text"))
        self.actionSH_Python.setText(_translate("MainWindow", "Python"))
from highlighter.parenmatch import TE_CustomPlainTextEdit
