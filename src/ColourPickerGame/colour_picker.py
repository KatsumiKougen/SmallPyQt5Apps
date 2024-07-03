from PyQt5 import QtWidgets, QtCore, QtGui
from ui.CPG_ColourPickerUi import Ui_CPG_CP_IncompleteWidget
import sys

class CPG_ColourPickerWidget(Ui_CPG_CP_IncompleteWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._CPG_CP_BuildUi(self.CPG_CP_ColourRect)
    
    def _CPG_CP_BuildUi(self, widget: QtWidgets.QLabel):
        WidgetWidth, WidgetHeight = widget.width(), widget.height()
        self.CPG_CP_ColourRectPixmap = QtGui.QPixmap(WidgetWidth, WidgetHeight)
        widget.setPixmap(self.CPG_CP_ColourRectPixmap)
        self.CPG_CP_ColourRectPainter = QtGui.QPainter(widget.pixmap())
        self.CPG_CP_ColourRectPen = QtGui.QPen()
        self.CPG_CP_ColourRectPainter.setPen(CPG_CP_ColourRectPen)
        
        for x in range(WidgetWidth):
            for y in range(WidgetHeight):
                CurrentColour = QtGui.QColor.fromHsv(x*360//WidgetWidth, y*255//WidgetHeight, 255)
                self.CPG_CP_ColourRectPen.setColor(CurrentColour)
                self.CPG_CP_ColourRectPainter.setPen(CPG_CP_ColourRectPen)
                self.CPG_CP_ColourRectPainter.drawPoint(x, y)
        self.CPG_CP_ColourRectPainter.end()

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    Window = CPG_ColourPickerWidget()
    sys.exit(App.exec())