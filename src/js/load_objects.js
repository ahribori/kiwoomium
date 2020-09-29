new QWebChannel(qt.webChannelTransport, function (channel) {
    window.kiwoomium = {
        ...channel.objects
    }
});