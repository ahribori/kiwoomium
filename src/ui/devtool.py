from PyQt5.QtWebEngineWidgets import QWebEngineView


class DevTool(QWebEngineView):
    def __init__(self, webview):
        QWebEngineView.__init__(self)
        self._init_devtool(webview)

    def _init_devtool(self, webview):
        self.setPage(self.page())
        webview.page().setDevToolsPage(self.page())
