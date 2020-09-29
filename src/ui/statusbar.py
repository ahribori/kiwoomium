from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QStatusBar, QProgressBar


class StatusBar(QStatusBar):
    def __init__(self):
        QStatusBar.__init__(self)
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumSize(200, 20)
        self.addWidget(self.progress_bar)

    @pyqtSlot(int, name="setProgressValue")
    def set_progress_value(self, v):
        self.progress_bar.setValue(v)
