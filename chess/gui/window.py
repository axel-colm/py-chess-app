from .qt_core import *
from .widgets.board import BoardWidget
from .widgets.menu.menu import MenuWidget
from ..board import Board


class MainWindow(QtWidgets.QMainWindow):
    MINIMUM_SIZE = QtCore.QSize(800, 600)
    _bg_color = "#44475a"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess")
        self.setMinimumSize(self.MINIMUM_SIZE)

        self._board = Board()

        self.setup_ui()


    def setup_ui(self):
        self._central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self._central_widget)
        self._central_widget.installEventFilter(self)

        self._layout = QtWidgets.QHBoxLayout()
        self._layout.setContentsMargins(2, 2, 2, 2)
        self._central_widget.setLayout(self._layout)

        self._menu = MenuWidget()
        self._menu.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        self._layout.addWidget(self._menu)

        self._content_widget = QtWidgets.QWidget()
        self._content_widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self._content_layout = QtWidgets.QVBoxLayout()
        self._content_layout.setContentsMargins(2, 2, 2, 2)
        self._content_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._content_widget.setLayout(self._content_layout)
        self._layout.addWidget(self._content_widget)

        self._board_widget = BoardWidget(self._board)
        self._board_widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self._content_layout.addWidget(self._board_widget)





    def eventFilter(self, watched, event):
        if watched == self._central_widget and event.type() == QtCore.QEvent.Type.Paint:
            self._paint_background()
        return super().eventFilter(watched, event)

    def _paint_background(self):
        painter = QtGui.QPainter(self._central_widget)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)

        painter.setPen(QtCore.Qt.PenStyle.NoPen)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(self._bg_color)))
        painter.drawRect(self.rect())




