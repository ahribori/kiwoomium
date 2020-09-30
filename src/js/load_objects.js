new QWebChannel(qt.webChannelTransport, function (channel) {
    for (const [key, value] of Object.entries(channel.objects)) {
        window[key] = value
    }
    var event = document.createEvent("CustomEvent");
    event.initCustomEvent("onLoad.kiwoom", true, true, window.kiwoomium);
    document.dispatchEvent(event);
});