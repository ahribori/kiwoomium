from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow, QShortcut

from ui.devtool import DevTool
from ui.statusbar import StatusBar
from ui.toolbar import Toolbar
from ui.webview import WebView


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self._init_widget()

    def _init_widget(self):
        self.setWindowTitle("Kiwoomium")
        self.setGeometry(100, 100, 1024, 768)
        self.setMinimumSize(1024, 768)

        self.toolbar = Toolbar()
        self.statusbar = StatusBar()
        self.webview = WebView()

        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.webview)
        self.setStatusBar(self.statusbar)

        self._init_toolbar()
        self._init_webview()
        self._init_devtool()
        self._init_shortcut()

    def _init_webview(self):
        self.webview.setUrl(QUrl("https://www.qt.io"))
        self.webview.loadProgress.connect(
            lambda progress: self.toolbar.changeStopReload(bool(0 <= progress >= 100)))
        self.webview.loadProgress.connect(self.statusbar.setProgressValue)

    def _init_devtool(self):
        self.devtool = DevTool(self.webview)

    def _init_toolbar(self):
        self.toolbar.backButtonClicked.connect(self.webview.back)
        self.toolbar.forwardButtonClicked.connect(self.webview.forward)
        self.toolbar.stopReloadButtonClicked.connect(
            lambda v: self.webview.triggerPageAction(v))
        self.toolbar.addressChanged.connect(lambda v: self.webview.setUrl(QUrl(v)))

    def _init_shortcut(self):
        self.shortcut = {}
        self.shortcut['F12'] = QShortcut(self)
        self.shortcut['F12'].setContext(Qt.ApplicationShortcut)
        self.shortcut['F12'].setKey(Qt.Key_F12)
        self.shortcut['F12'].activated.connect(self._toggle_devtool)

    def _toggle_devtool(self):
        is_enabled = self.devtool.isVisible()

        if not is_enabled:
            pos = self.pos()
            size = self.size()
            margin = 30
            width = 700
            height = size.height()
            x = pos.x() + size.width() + margin
            y = pos.y() + margin
            self.devtool.setGeometry(x, y, width, height)
            self.devtool.activate()
        else:
            self.devtool.deactivate()
