from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings


class WebView(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        settings = self.settings()
        settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.DnsPrefetchEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
        settings.setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled, True)
        settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
