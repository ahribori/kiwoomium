from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog, QGridLayout


class DevTool(QDialog):
    def __init__(self, webview):
        QDialog.__init__(self)
        self.webview = webview
        self._init_devtool()
        self.setWindowTitle("DevTool")
        self.resize(600, 800)
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.layout.addWidget(self.devtool)

    def _init_devtool(self):
        self.devtool = QWebEngineView()
        self.devtool.setPage(self.devtool.page())
        self.webview.page().setDevToolsPage(self.devtool.page())

    def activate(self):
        self.setVisible(True)
        self.devtool.setVisible(True)

    def deactivate(self):
        self.setVisible(False)
        self.devtool.setVisible(False)
