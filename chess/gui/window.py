from .qt_core import *
from .widgets.board import BoardWidget
from .widgets.menu.menu import MenuWidget
from .. import Chess
from ..board import Board
from ..pieces.color import Color
from ..player import Player


class MainWindow(QtWidgets.QMainWindow):
    MINIMUM_SIZE = QtCore.QSize(800, 600)
    _bg_color = "#44475a"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess")
        self.setMinimumSize(self.MINIMUM_SIZE)

        self._board = Chess()

        self.setup_ui()

        self._stop_game()

    def setup_ui(self):
        self._central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self._central_widget)
        self._central_widget.installEventFilter(self)

        self._layout = QtWidgets.QHBoxLayout()
        self._layout.setContentsMargins(2, 2, 2, 2)
        self._central_widget.setLayout(self._layout)

        self._menu = MenuWidget()
        self._menu.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        # self._layout.addWidget(self._menu)

        self._content_widget = QtWidgets.QStackedWidget()
        self._content_widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self._layout.addWidget(self._content_widget)

        self._board_widget = BoardWidget(self._board)
        self._board_widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self._content_widget.addWidget(self._board_widget)

        self._start_view = QtWidgets.QWidget()
        self._content_widget.addWidget(self._start_view)

        self._start_view_layout = QtWidgets.QVBoxLayout()
        self._start_view_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._start_view.setLayout(self._start_view_layout)

        self._start_view_button = QtWidgets.QPushButton("Play")
        self._start_view_button.setFixedSize(200, 50)
        self._start_view_button.clicked.connect(self._start_game)
        self._start_view_layout.addWidget(self._start_view_button)

    def _start_game(self):
        p1 = Player(self._board, Color.WHITE)
        p2 = Player(self._board, Color.BLACK)
        self._board.initialize(p1, p2)
        self._content_widget.setCurrentWidget(self._board_widget)

    def _stop_game(self):
        self._content_widget.setCurrentWidget(self._start_view)


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




