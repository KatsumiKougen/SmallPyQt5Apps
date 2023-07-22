# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(660, 293)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AboutDialog_MainHLayout = QtWidgets.QHBoxLayout()
        self.AboutDialog_MainHLayout.setObjectName("AboutDialog_MainHLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.AboutDialog_MainHLayout.addItem(spacerItem)
        self.AboutDialog_ImageVLayout = QtWidgets.QVBoxLayout()
        self.AboutDialog_ImageVLayout.setObjectName("AboutDialog_ImageVLayout")
        self.AboutDialog_Image = QtWidgets.QLabel(Dialog)
        self.AboutDialog_Image.setScaledContents(True)
        self.AboutDialog_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.AboutDialog_Image.setWordWrap(False)
        self.AboutDialog_Image.setObjectName("AboutDialog_Image")
        self.AboutDialog_ImageVLayout.addWidget(self.AboutDialog_Image)
        self.AboutDialog_ImageCreditLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AboutDialog_ImageCreditLabel.sizePolicy().hasHeightForWidth())
        self.AboutDialog_ImageCreditLabel.setSizePolicy(sizePolicy)
        self.AboutDialog_ImageCreditLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.AboutDialog_ImageCreditLabel.setObjectName("AboutDialog_ImageCreditLabel")
        self.AboutDialog_ImageVLayout.addWidget(self.AboutDialog_ImageCreditLabel)
        self.AboutDialog_MainHLayout.addLayout(self.AboutDialog_ImageVLayout)
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.AboutDialog_MainHLayout.addItem(spacerItem1)
        self.AboutDialog_IntroductionLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AboutDialog_IntroductionLabel.sizePolicy().hasHeightForWidth())
        self.AboutDialog_IntroductionLabel.setSizePolicy(sizePolicy)
        self.AboutDialog_IntroductionLabel.setTextFormat(QtCore.Qt.RichText)
        self.AboutDialog_IntroductionLabel.setWordWrap(True)
        self.AboutDialog_IntroductionLabel.setObjectName("AboutDialog_IntroductionLabel")
        self.AboutDialog_MainHLayout.addWidget(self.AboutDialog_IntroductionLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.AboutDialog_MainHLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.AboutDialog_MainHLayout)
        self.AboutDialog_CloseButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AboutDialog_CloseButton.sizePolicy().hasHeightForWidth())
        self.AboutDialog_CloseButton.setSizePolicy(sizePolicy)
        self.AboutDialog_CloseButton.setObjectName("AboutDialog_CloseButton")
        self.verticalLayout.addWidget(self.AboutDialog_CloseButton)

        self.retranslateUi(Dialog)
        self.AboutDialog_CloseButton.clicked.connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.AboutDialog_Image.setText(_translate("Dialog", "Image"))
        self.AboutDialog_ImageCreditLabel.setText(_translate("Dialog", "Art by **darktrident** @ pixiv"))
        self.AboutDialog_IntroductionLabel.setText(_translate("Dialog", "<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">The text editor</span></h1><p>Written by Katsumi (<a href=\"https://twitter.com/realKatsumi_vn\"><span style=\" text-decoration: underline; color:#0000ff;\">twitter.com/realKatsumi_vn</span></a>)</p><p>This program is not meant to be an actual text editor — it is made for demonstration purposes only.</p><hr/><p>Copyright 2023</p></body></html>"))
        self.AboutDialog_CloseButton.setText(_translate("Dialog", "Close"))
