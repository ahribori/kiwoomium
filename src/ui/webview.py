from PyQt5.QtCore import QFile, pyqtSlot, QIODevice
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

from src.core.kiwoom import Kiwoom


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
        self.loadFinished.connect(self._on_load_finished)

    @pyqtSlot(bool)
    def _on_load_finished(self, ok):
        if ok:
            self._execute_javascript()

    def _execute_javascript(self):
        qwebchannel_js = QFile('src/js/qwebchannel.min.js')
        if qwebchannel_js.open(QIODevice.ReadOnly):
            content = qwebchannel_js.readAll()
            qwebchannel_js.close()
            self.page().runJavaScript(content.data().decode())
        if self.page().webChannel() is None:
            self._set_web_channel()

    def _set_web_channel(self):
        channel = QWebChannel(self.page())
        self.page().setWebChannel(channel)
        self.kiwoom = Kiwoom()
        channel.registerObject('kiwoom', self.kiwoom)
        self.load_objects()

    def load_objects(self):
        load_objects_js = QFile('src/js/load_objects.js')
        if load_objects_js.open(QIODevice.ReadOnly):
            content = load_objects_js.readAll()
            load_objects_js.close()
            self.page().runJavaScript(content.data().decode())

    # webview의 document에 이벤트를 발생함.
    def emit(self, type, payload):
        self.page().runJavaScript("""
        var event = document.createEvent("CustomEvent");
        event.initCustomEvent("{type}", true, true, {payload} );
        document.dispatchEvent(event);
        """.format(type=type, payload=payload))
