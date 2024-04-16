from .qt_core import *
from .widgets.board import BoardWidget
from ..board import Board


class MainWindow(QMainWindow):
    MINIMUM_SIZE = QSize(800, 600)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess")
        self.setMinimumSize(self.MINIMUM_SIZE)
        b = Board()
        self._board = BoardWidget(b)
        self.setCentralWidget(self._board)