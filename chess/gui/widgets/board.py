from ..qt_core import *
from ...board import Board


class BoardWidget(QtWidgets.QWidget):
    _colors_black = "#769656"
    _colors_white = "#eeeed2"

    def __init__(self, board: Board):
        super().__init__()
        self._board = board

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)

        self.drawBoard(painter)
        self.drawPieces(painter)

    def drawBoard(self, painter):
        size = min(self.width(), self.height())
        square_size = size / max(self._board.BOARD_SIZE)

        for x in range(self._board.BOARD_SIZE[0]):
            for y in range(self._board.BOARD_SIZE[1]):
                color = self._colors_black if (x + y) % 2 == 0 else self._colors_white
                painter.fillRect(x * square_size, y * square_size, square_size, square_size, QtGui.QColor(color))

    def drawPieces(self, painter):
        pass

