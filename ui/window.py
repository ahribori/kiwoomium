from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow

from ui.statusbar import StatusBar
from ui.toolbar import Toolbar
from ui.webview import WebView


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self._init_widget()

    def _init_widget(self):
        self.setWindowTitle("Kiwoomium")
        self.setMinimumSize(1024, 768)

        self.toolbar = Toolbar()
        self.statusbar = StatusBar()
        self.webview = WebView()
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.webview)

        self.webview.setUrl(QUrl("https://www.qt.io"))
        self.webview.loadProgress.connect(
            lambda progress: self.toolbar.changeStopReload(bool(0 <= progress >= 100)))
        self.webview.loadProgress.connect(self.statusbar.setProgressValue)
        self.toolbar.backButtonClicked.connect(self.webview.back)
        self.toolbar.forwardButtonClicked.connect(self.webview.forward)
        self.toolbar.stopReloadButtonClicked.connect(
            lambda v: self.webview.triggerPageAction(v))
        self.toolbar.addressChanged.connect(lambda v: self.webview.setUrl(QUrl(v)))
        self.setStatusBar(self.statusbar)
