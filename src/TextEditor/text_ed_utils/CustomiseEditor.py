import sys
from PyQt5 import QtWidgets, QtCore, QtGui

sys.path.append(".")
from ui.CustomiseEditorWidgetUI import Ui_Dialog

class TE_CustomiseEditorWidget(QtWidgets.QDialog, Ui_Dialog):
    
    output0 = QtCore.pyqtSignal(int)
    output1 = QtCore.pyqtSignal(int)
    
    def __init__(self, FontSize, IndentSize):
        super().__init__()
        self.setupUi(self)
        self.CE_FontSizeHSlider.setValue(FontSize)
        self.CE_FontSizeSpinBox.setValue(FontSize)
        self.CE_IndentSizeHSlider.setValue(IndentSize)
        self.CE_IndentSizeSpinBox.setValue(IndentSize)
        self.CE_ConnectSignals()
    
    def CE_ConnectSignals(self):
        self.CE_FontSizeHSlider.valueChanged.connect(self.CE_SyncEntity0SpinBox)
        self.CE_FontSizeSpinBox.valueChanged.connect(self.CE_SyncEntity0Slider)
        self.CE_IndentSizeHSlider.valueChanged.connect(self.CE_SyncEntity1SpinBox)
        self.CE_IndentSizeSpinBox.valueChanged.connect(self.CE_SyncEntity1Slider)
    
    @QtCore.pyqtSlot(int)
    def CE_SyncEntity0Slider(self, value):
        self.CE_FontSizeHSlider.setValue(value)
        self.CE_EmitSignal()
    
    @QtCore.pyqtSlot(int)
    def CE_SyncEntity0SpinBox(self, value):
        self.CE_FontSizeSpinBox.setValue(value)
        self.CE_EmitSignal()
    
    @QtCore.pyqtSlot(int)
    def CE_SyncEntity1Slider(self, value):
        self.CE_IndentSizeHSlider.setValue(value)
        self.CE_EmitSignal()
    
    @QtCore.pyqtSlot(int)
    def CE_SyncEntity1SpinBox(self, value):
        self.CE_IndentSizeSpinBox.setValue(value)
        self.CE_EmitSignal()
    
    def CE_EmitSignal(self):
        self.output0.emit(self.CE_FontSizeSpinBox.value())
        self.output1.emit(self.CE_IndentSizeSpinBox.value())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())