from PyQt5.QtCore import pyqtSignal, Qt, pyqtSlot, QSize
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QAction, QToolBar, QLineEdit


class Toolbar(QToolBar):
    back_button_clicked = pyqtSignal(name="backButtonClicked")
    forward_button_clicked = pyqtSignal(name="forwardButtonClicked")
    stop_reload_button_clicked = pyqtSignal(int, name="stopReloadButtonClicked")
    address_changed = pyqtSignal(str, name="addressChanged")

    def __init__(self):
        QToolBar.__init__(self)
        self.setMovable(False)
        self.toggleViewAction().setEnabled(False)
        self.setIconSize(QSize(24, 24))

        # 뒤로가기 버튼
        self.back_action = QAction(self)
        self.back_action.setShortcut(QKeySequence(Qt.Key_Back))
        self.back_action.setIcon(QIcon("assets/svg/left.svg"))
        self.addAction(self.back_action)
        self.back_action.triggered.connect(self.back_button_clicked)

        # 앞으로가기 버튼
        self.forward_action = QAction(self)
        self.forward_action.setShortcut(QKeySequence(Qt.Key_Forward))
        self.forward_action.setIcon(QIcon("assets/svg/right.svg"))
        self.addAction(self.forward_action)
        self.forward_action.triggered.connect(self.forward_button_clicked)

        # 새로고침 취소 액션
        self.stop_reload_action = QAction(self)
        self.stop_reload_action.setShortcut(QKeySequence(Qt.Key_F5))
        self.stop_reload_action.setIcon(QIcon("assets/svg/reload.svg"))
        self.stop_reload_action.setData(QWebEnginePage.Reload)
        self.addAction(self.stop_reload_action)
        self.stop_reload_action.triggered.connect(
            lambda: self.stop_reload_button_clicked.emit(
                QWebEnginePage.WebAction(self.stop_reload_action.data())))

        # 주소창
        self.le = QLineEdit()
        fav_action = QAction(self)
        self.le.addAction(fav_action, QLineEdit.LeadingPosition)
        self.le.setClearButtonEnabled(True)
        self.le.setContentsMargins(8, 8, 8, 8)
        self.addWidget(self.le)
        self.le.editingFinished.connect(
            lambda: self.address_changed.emit(self.le.text()))

    @pyqtSlot(bool, name="changeStopReload")
    def change_stop_reload(self, state):
        if state:
            self.stop_reload_action.setShortcut(QKeySequence(Qt.Key_F5))
            self.stop_reload_action.setIcon(QIcon("assets/svg/reload.svg"))
            self.stop_reload_action.setData(QWebEnginePage.Reload)
        else:
            self.stop_reload_action.setShortcut(QKeySequence(Qt.Key_Escape))
            self.stop_reload_action.setIcon(QIcon("assets/svg/close.svg"))
            self.stop_reload_action.setData(QWebEnginePage.Stop)
