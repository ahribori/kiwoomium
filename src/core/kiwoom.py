from PyQt5.QtCore import QObject, pyqtSlot


class Kiwoom(QObject):
    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot(str, name="printText")
    def printText(self, text):
        print(text)
