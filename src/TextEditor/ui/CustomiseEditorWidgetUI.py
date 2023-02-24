# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/CustomiseEditorWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 82)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.CE_FontSizeSpinBox = QtWidgets.QSpinBox(Form)
        self.CE_FontSizeSpinBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CE_FontSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.CE_FontSizeSpinBox.setSizePolicy(sizePolicy)
        self.CE_FontSizeSpinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.CE_FontSizeSpinBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.CE_FontSizeSpinBox.setBaseSize(QtCore.QSize(0, 0))
        self.CE_FontSizeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.CE_FontSizeSpinBox.setMinimum(8)
        self.CE_FontSizeSpinBox.setMaximum(72)
        self.CE_FontSizeSpinBox.setObjectName("CE_FontSizeSpinBox")
        self.gridLayout.addWidget(self.CE_FontSizeSpinBox, 0, 1, 1, 1)
        self.CE_FontSizeHSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CE_FontSizeHSlider.sizePolicy().hasHeightForWidth())
        self.CE_FontSizeHSlider.setSizePolicy(sizePolicy)
        self.CE_FontSizeHSlider.setOrientation(QtCore.Qt.Horizontal)
        self.CE_FontSizeHSlider.setObjectName("CE_FontSizeHSlider")
        self.gridLayout.addWidget(self.CE_FontSizeHSlider, 0, 2, 1, 1)
        self.CE_FontSizeLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CE_FontSizeLabel.sizePolicy().hasHeightForWidth())
        self.CE_FontSizeLabel.setSizePolicy(sizePolicy)
        self.CE_FontSizeLabel.setObjectName("CE_FontSizeLabel")
        self.gridLayout.addWidget(self.CE_FontSizeLabel, 0, 0, 1, 1)
        self.CE_IndentSizeLabel = QtWidgets.QLabel(Form)
        self.CE_IndentSizeLabel.setObjectName("CE_IndentSizeLabel")
        self.gridLayout.addWidget(self.CE_IndentSizeLabel, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CE_FontSizeSpinBox.setSuffix(_translate("Form", " pt"))
        self.CE_FontSizeLabel.setText(_translate("Form", "Font size"))
        self.CE_IndentSizeLabel.setText(_translate("Form", "Indent size"))
        self.spinBox.setSuffix(_translate("Form", " spaces"))
