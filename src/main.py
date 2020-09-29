import sys

from PyQt5.QtWidgets import QApplication

from src.ui.window import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    exit(app.exec())
