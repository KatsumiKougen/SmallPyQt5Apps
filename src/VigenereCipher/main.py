from PyQt5 import QtWidgets, QtCore, QtGui, uic
import sys, itertools, pyperclip
import VigenereCipher as VC

class MainWindow(QtWidgets.QMainWindow):

    class _AppVariables:
        CustomWindowTitles = [
            "Katsumi's Vigenère cipher encoder/decoder",
            "Don't get hooked... stay off the hook!",
            "SOMEBODY HELP ME, I'M STUCK IN THIS THING FOR DAYS"
        ]
        CryptogramMode = 0
        # encode: 0, decode: 1
        CipherVariation = 0
        # Normal Vigenère: 0
        # Vigenère-RC4 (8-bits): 1
        # Vigenère-RC4 (4-bits): 2

    def __init__(self):
        super().__init__()
        uic.loadUi("VigenereCipher.ui", self)
        self.setWindowTitle(self._AppVariables.CustomWindowTitles[0])
        self.InitWindow()
        self._ButtonBuffer = []
    
    def InitWindow(self):
        self.UserInputEdit.setPlaceholderText("Soos later forced McGucket to watch all 900 hours of \"Neon Crisis Mechabot Boy: Revelations\"")
        self.KeywordInputEdit.setPlaceholderText("shacktron")
        self.OutputSection.setPlaceholderText("Kvou vtkse xvreow DqTmjkgd mf knljh cve 900 ychjz oh \"Xxfb Pjpskc Fvqusiov Lhp: Frnllcdbfbf\"")

        self.ModeSelectGroup = QtWidgets.QButtonGroup()
        self.VgOptionSelectGroup = QtWidgets.QButtonGroup()
        self.ModeSelectGroup.addButton(self.EncodeModeRadio, 1)
        self.ModeSelectGroup.addButton(self.DecodeModeRadio, 2)
        self.VgOptionSelectGroup.addButton(self.VgVariant0OptionRadio, 1)
        self.VgOptionSelectGroup.addButton(self.VgVariant1OptionRadio, 2)
        self.VgOptionSelectGroup.addButton(self.VgVariant2OptionRadio, 3)
        self.EncodeModeRadio.setChecked(True)
        self.VgVariant0OptionRadio.setChecked(True)
        
        self.UserInputEdit.textChanged.connect(self.ShowTextOnOutput)
        self.KeywordInputEdit.textChanged.connect(self.ShowTextOnOutput)
        self.ModeSelectGroup.buttonClicked.connect(self.SwitchCryptogramMode)
        self.ModeSelectGroup.buttonClicked.connect(self.ShowTextOnOutput)
        self.VgOptionSelectGroup.buttonClicked.connect(self.SwitchCipherVariant)
        self.VgOptionSelectGroup.buttonClicked.connect(self.ShowTextOnOutput)
        self.CopyButton.clicked.connect(self.CopyOutput)
        self.SaveButton.clicked.connect(self.OpenSaveFileDialog)
    
    def ShowTextOnOutput(self):
        match self._AppVariables.CipherVariation:
            case 0:
                InputText = self.UserInputEdit.toPlainText()
                Keyword = self.KeywordInputEdit.toPlainText()
                self.OutputSection.clear()
                match self._AppVariables.CryptogramMode:
                    case 0:
                        if Keyword == "":
                            self.OutputSection.insertPlainText(InputText)
                        else:
                            self.OutputSection.insertPlainText(VC.VgVariant0(Keyword).encode(InputText))
                    case 1:
                        if Keyword == "":
                            self.OutputSection.insertPlainText(InputText)
                        else:
                            self.OutputSection.insertPlainText(VC.VgVariant0(Keyword).decode(InputText))
            case 1:
                InputText = self.UserInputEdit.toPlainText()
                Keyword = self.KeywordInputEdit.toPlainText()
                self.OutputSection.clear()
                match self._AppVariables.CryptogramMode:
                    case 0:
                        if Keyword == "":
                            self.OutputSection.insertPlainText(InputText)
                        else:
                            self.OutputSection.insertPlainText(VC.VgVariant1(Keyword).encode(InputText))
                    case 1:
                        if Keyword == "":
                            self.OutputSection.insertPlainText(InputText)
                        else:
                            self.OutputSection.insertPlainText(VC.VgVariant1(Keyword).decode(InputText))
            case 2:
                self.OutputSection.clear()
                self.OutputSection.insertPlainText("Mode 2 output not available - TBA...")
    
    def SwitchCipherVariant(self, arg):
        match self.VgOptionSelectGroup.id(arg):
            case 1:
                self._AppVariables.CipherVariation = 0
            case 2:
                self._AppVariables.CipherVariation = 1
            case 3:
                self._AppVariables.CipherVariation = 2
    
    def SwitchCryptogramMode(self, arg):
        match self.ModeSelectGroup.id(arg):
            case 1:
                self._AppVariables.CryptogramMode = 0
                self._ButtonBuffer.append(0)
            case 2:
                self._AppVariables.CryptogramMode = 1
                self._ButtonBuffer.append(1)
        if len(self._ButtonBuffer) > 256:
            self._ButtonBuffer = []
        match self._ButtonBuffer[-10:]:
            case [0, 0, 1, 0, 1, 1, 0, 0, 0, 1]:
                self.setWindowTitle(self._AppVariables.CustomWindowTitles[1])
            case [1, 1, 1, 0, 1, 0, 0, 1, 0, 0]:
                self.setWindowTitle(self._AppVariables.CustomWindowTitles[2])
            case [1, 0, 1, 0, 0, 1, 1, 1, 0, 1]:
                self.CreditsLabel1.setText("You think you are safe, goofball? I can see you holding your mouse.")
            case [1, 1, 0, 0, 1, 0, 0, 0, 1, 1]:
                xor = lambda a: chr(ord(a)^84)
                msg = "\x1d t='t:; t#<5 t= t'119'z^\x1d2t= t75 7<1't-;!xt= s88t0;t ;t-;!zzzt <1t#5-t= t0=0t ;t91z^\x00!&:t;22t <='t$&;3&59t&=3< t:;#z^\x1d2t-;!t<15&t';91 <=:3zzzt <5 t915:'t= s't<15&0t-;!z"
                self.UserInputEdit.clear()
                self.UserInputEdit.insertPlainText("".join(map(xor, msg)))
            case _:
                self.setWindowTitle(self._AppVariables.CustomWindowTitles[0])
                self.CreditsLabel1.setText("Copyright 2023")
    
    def CopyOutput(self, arg):
        pyperclip.copy(self.OutputSection.toPlainText())
    
    def OpenSaveFileDialog(self, arg):
        match self._AppVariables.CipherVariation:
            case 0:
                SaveFile = QtWidgets.QFileDialog.getSaveFileName(
                    self,
                    caption = "Save file as...",
                    directory = f"{self.KeywordInputEdit.toPlainText()}.txt"
                )
                with open(SaveFile[0], "w") as fo:
                    fo.write(self.OutputSection.toPlainText())
            case 1:
                SaveFile = QtWidgets.QFileDialog.getSaveFileName(
                    self,
                    caption = "Save file as...",
                    directory = f"{self.KeywordInputEdit.toPlainText()}"
                )
                with open(SaveFile[0], "wb") as fo:
                    InputText = self.UserInputEdit.toPlainText()
                    Keyword = self.KeywordInputEdit.toPlainText()
                    match self._AppVariables.CryptogramMode:
                        case 0:
                            fo.write(VC.VgVariant1(Keyword).encode(InputText), readable=False)
                        case 1:
                            fo.write(VC.VgVariant1(Keyword).decode(InputText), readable=False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
