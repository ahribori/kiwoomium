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

    # webview의 document에 이벤트를 발생함.
    def emit(self, type, payload):
        self.page().runJavaScript("""
        var event = document.createEvent("CustomEvent");
        event.initCustomEvent("{type}", true, true, {payload} );
        document.dispatchEvent(event);
        """.format(type=type, payload=payload))
