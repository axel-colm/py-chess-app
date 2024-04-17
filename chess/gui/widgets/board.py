from ..core.functions import Function
from ..qt_core import *
from ... import Chess
from ...pieces.piece import Piece


class BoardWidget(QtWidgets.QWidget):
    released = QtCore.Signal(object)
    clicked = QtCore.Signal(object)

    BUTTON_SIZE = 50
    BACK_ICON = Function.icon_path("angle-left.svg")
    _colors_black = "#769656"
    _colors_white = "#eeeed2"

    _case_selected: tuple[int, int] | None = None
    movePiece = QtCore.Signal(tuple[int, int], tuple[int, int])

    def __init__(self, board: Chess):
        super().__init__()
        self._board = board

        self.back_button = QtWidgets.QPushButton()
        self.back_button.setParent(self)
        self.back_button.setObjectName("back_button")
        self.back_button.setIcon(QtGui.QIcon(self.BACK_ICON))
        self.back_button.setIconSize(QtCore.QSizeF(self.BUTTON_SIZE * 0.7, self.BUTTON_SIZE * 0.7).toSize())
        self.back_button.setGeometry(0, 0, self.BUTTON_SIZE, self.BUTTON_SIZE)
        self.back_button.released.connect(lambda x=self.back_button: self.released.emit(x))
        self.back_button.setStyleSheet("background-color: transparent; border: none;")

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        pixmap = QtGui.QPixmap(self.size())
        pixmap.fill(QtCore.Qt.GlobalColor.transparent)

        p = QtGui.QPainter(pixmap)
        p.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        p.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        self.drawBoard(p)
        self.drawPieces(p)
        p.end()

        painter.drawPixmap(0, 0, pixmap)

    def drawBoard(self, painter):
        size = min(self.width() - self.BUTTON_SIZE, self.height())
        square_size = size / max(self._board.BOARD_SIZE)

        left = (self.width() - size) / 2
        top = (self.height() - size) / 2
        for x in range(self._board.BOARD_SIZE[0]):
            for y in range(self._board.BOARD_SIZE[1]):
                color = self._colors_black if (x + y) % 2 == 0 else self._colors_white
                painter.setPen(QtCore.Qt.PenStyle.NoPen)
                painter.setBrush(QtGui.QBrush(QtGui.QColor(color)))
                painter.drawRect(
                    x * square_size + left,
                    y * square_size + top,
                    square_size,
                    square_size
                )

        # Draw numbers and letters
        for y in range(self._board.BOARD_SIZE[1]):
            color = self._colors_white if y % 2 == 0 else self._colors_black
            inv_color = self._colors_black if y % 2 == 0 else self._colors_white
            painter.setPen(QtGui.QPen(QtGui.QColor(color)))
            painter.drawText(
                left + 2,
                y * square_size + top + 2,
                20,
                20,
                QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft,
                str(self._board.BOARD_SIZE[1] - y)
            )
            # Dessine les nombres mais dans l'autre sens donc à l'envers
            painter.setTransform(QtGui.QTransform().rotate(180))
            painter.setPen(QtGui.QPen(QtGui.QColor(inv_color)))
            painter.setTransform(QtGui.QTransform())

        for x in range(self._board.BOARD_SIZE[0]):
            color = self._colors_black if x % 2 == 0 else self._colors_white
            inv_color = self._colors_white if x % 2 == 0 else self._colors_black
            painter.setPen(QtGui.QPen(QtGui.QColor(color)))
            painter.drawText(
                left + x * square_size + square_size - 24,
                top + size - 20,
                20,
                20,
                QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignRight,
                chr(65 + x)
            )
            painter.setTransform(QtGui.QTransform())


        # Draw case selected
        if self._case_selected is not None:
            x, y = self._case_selected
            color = QtGui.QColor("#f0f000")
            color.setAlpha(100)
            painter.setPen(QtCore.Qt.PenStyle.NoPen)
            painter.setBrush(QtGui.QBrush(color))
            painter.drawRect(
                left + x * square_size,
                top + y * square_size,
                square_size,
                square_size
            )

            piece = self._board.getCase(x, y)
            if isinstance(piece, Piece):
                for move in piece.getMoves():
                    x, y = move
                    color = QtGui.QColor("#00f000")
                    color.setAlpha(100)
                    painter.setPen(QtCore.Qt.PenStyle.NoPen)
                    painter.setBrush(QtGui.QBrush(color))
                    painter.drawRect(
                        left + x * square_size,
                        top + y * square_size,
                        square_size,
                        square_size
                    )

    def drawPieces(self, painter):
        size = min(self.width(), self.height())
        square_size = size / max(self._board.BOARD_SIZE)

        left = (self.width() - size) / 2
        top = (self.height() - size) / 2
        for x in range(self._board.BOARD_SIZE[0]):
            for y in range(self._board.BOARD_SIZE[1]):
                piece = self._board.getCase(x, y)
                if piece is not None:
                    color = piece.getColor().name[0].lower()
                    name = piece.__class__.__name__[:2].upper()

                    icon_path = Function.icon_path(f"{color}{name}.svg")
                    icon = QtGui.QIcon(icon_path)
                    size = square_size * 0.9

                    painter.drawPixmap(
                        left + x * square_size + (square_size - size) / 2,
                        top + y * square_size + (square_size - size) / 2,
                        size,
                        size,
                        icon.pixmap(size, size)
                    )

    def mouseReleaseEvent(self, event):
        size = min(self.width(), self.height())
        square_size = size / max(self._board.BOARD_SIZE)

        left = (self.width() - size) / 2
        top = (self.height() - size) / 2

        x = int((event.x() - left) // square_size)
        y = int((event.y() - top) // square_size)

        if not self._board.isInside(x, y):
            return

        if self._case_selected is not None:
            piece = self._board.getCase(self._case_selected[0], self._case_selected[1])
            if isinstance(piece, Piece) and piece.canMove((x, y)) :
                if piece.getColor() == self._board.turnColor():
                    # self.movePiece.emit(self._case_selected, (x, y))
                    self._board.move(self._case_selected, (x, y))
                    self._case_selected = None
                    self.update()
                return

        if self._board.getCase(x, y) is not None:
            if self._case_selected == (x, y):
                self._case_selected = None
            else:
                self._case_selected = (x, y)
        else:
            self._case_selected = None
        self.update()
