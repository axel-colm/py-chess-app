from .qt_core import *


class MainWindow(QMainWindow):
    MINIMUM_SIZE = QSize(800, 600)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess")
        self.setMinimumSize(self.MINIMUM_SIZE)

