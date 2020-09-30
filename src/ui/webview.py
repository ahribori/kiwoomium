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
            self._load_qwebchannel()

    # 웹뷰와 메인프로세스간의 통신을 위해 채널을 만들기 위해 cwebchannel.js를 브라우저에서 실행시킨다.
    def _load_qwebchannel(self):
        qwebchannel_js = QFile('src/js/qwebchannel.min.js')
        if qwebchannel_js.open(QIODevice.ReadOnly):
            content = qwebchannel_js.readAll()
            qwebchannel_js.close()
            self.page().runJavaScript(content.data().decode())
        self._set_web_channel()

    # 브라우저에서 실행가능한 인터페이스를 만든다.
    def _set_web_channel(self):
        channel = QWebChannel(self.page())
        self.page().setWebChannel(channel)
        self.kiwoom = Kiwoom(self)
        channel.registerObject('kiwoom', self.kiwoom)
        self._load_objects()

    # 브라우저에서 채널이 연결되면 채널 인터페이스를 window 객체에 바인딩한다.
    def _load_objects(self):
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
