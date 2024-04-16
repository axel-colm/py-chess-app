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

        left = (self.width() - size) / 2
        top = (self.height() - size) / 2
        for x in range(self._board.BOARD_SIZE[0]):
            for y in range(self._board.BOARD_SIZE[1]):
                color = self._colors_black if (x + y) % 2 == 0 else self._colors_white
                painter.setBrush(QtGui.QBrush(QtGui.QColor(color)))
                painter.drawRect(
                    x * square_size + left,
                    y * square_size + top,
                    square_size,
                    square_size
                )

        # Draw numbers and letters

        for y in range(self._board.BOARD_SIZE[0]):
            color = self._colors_white if y % 2 == 0 else self._colors_black
            painter.setPen(QtGui.QPen(QtGui.QColor(color)))
            painter.drawText(
                left + 2,
                y * square_size + top + 2,
                20,
                20,
                QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft,
                str(y + 1)
            )

        for x in range(self._board.BOARD_SIZE[1]):
            color = self._colors_black if x % 2 == 0 else self._colors_white
            painter.setPen(QtGui.QPen(QtGui.QColor(color)))
            painter.drawText(
                left + x * square_size + square_size - 24,
                top + size - 20,
                20,
                20,
                QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignRight,
                chr(ord("a") + x)
            )

    def drawPieces(self, painter):
        pass

