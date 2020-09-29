from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow, QShortcut, QSplitter, QWidget, QBoxLayout

from src.ui.devtool import DevTool
from src.ui.statusbar import StatusBar
from src.ui.toolbar import Toolbar
from src.ui.webview import WebView


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self._init_widget()

    def _init_widget(self):
        self.setWindowTitle("Kiwoomium")
        self.setGeometry(100, 100, 1440, 960)
        self.setMinimumSize(1024, 768)

        self.toolbar = Toolbar()
        self.statusbar = StatusBar()
        self.webview = WebView()

        self._init_toolbar()
        self._init_webview()
        self._init_devtool()
        self._init_shortcut()
        self._init_layout()

    def _init_layout(self):
        self.main_widget = QWidget()
        self.layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter()
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.addWidget(self.webview)
        self.splitter.addWidget(self.devtool)
        self.splitter.setSizes([65, 35])
        self.layout.addWidget(self.splitter)
        self.main_widget.setLayout(self.layout)

        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.main_widget)
        self.setStatusBar(self.statusbar)

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
        self.devtool.setVisible(not self.devtool.isVisible())
