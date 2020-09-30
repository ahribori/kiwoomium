new QWebChannel(qt.webChannelTransport, function (channel) {
    window.kiwoomium = {
        ...channel.objects
    }
    var event = document.createEvent("CustomEvent");
    event.initCustomEvent("onLoad.kiwoom", true, true, window.kiwoomium);
    document.dispatchEvent(event);
});