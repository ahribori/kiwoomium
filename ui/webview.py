from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebView(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
