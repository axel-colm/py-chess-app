from .core.functions import Function
from .qt_core import *
from .widgets.board import BoardWidget
from .. import Chess
from ..board import Board
from ..pieces.color import Color
from ..player import Player


class MainWindow(QtWidgets.QMainWindow):
    MINIMUM_SIZE = QtCore.QSize(800, 600)

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

        self._layout = QtWidgets.QHBoxLayout()
        self._layout.setContentsMargins(2, 2, 2, 2)
        self._central_widget.setLayout(self._layout)

        self._content_widget = QtWidgets.QStackedWidget()
        self._content_widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self._layout.addWidget(self._content_widget)

        self._board_widget = BoardWidget(self._board)
        self._board_widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self._board_widget.clicked.connect(self._button_clicked)
        self._board_widget.released.connect(self._button_released)
        self._content_widget.addWidget(self._board_widget)

        # <editor-fold desc="Start view">
        self._start_view = QtWidgets.QWidget()
        self._content_widget.addWidget(self._start_view)

        self._start_view_layout = QtWidgets.QVBoxLayout()
        self._start_view_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._start_view.setLayout(self._start_view_layout)

        self._new_game_button = QtWidgets.QPushButton("New game")
        self._new_game_button.setFixedSize(200, 50)
        self._new_game_button.released.connect(self._new_game)

        self._load_game_button = QtWidgets.QPushButton("Load game")
        self._load_game_button.setFixedSize(200, 50)
        self._load_game_button.released.connect(self._load_game)

        self._start_view_layout.addWidget(self._new_game_button)
        self._start_view_layout.addWidget(self._load_game_button)
        # </editor-fold>

        # <editor-fold desc="Choose type game">
        self._choose_game_type = QtWidgets.QWidget()
        self._content_widget.addWidget(self._choose_game_type)

        self._choose_game_back_button = QtWidgets.QPushButton()
        self._choose_game_back_button.setObjectName("back_button_choose")
        self._choose_game_back_button.setParent(self._choose_game_type)
        self._choose_game_back_button.setIcon(QtGui.QIcon(Function.icon_path("angle-left.svg")))
        self._choose_game_back_button.setIconSize(QtCore.QSize(30, 30))
        self._choose_game_back_button.setGeometry(0, 0, 50, 50)
        self._choose_game_back_button.setStyleSheet("background-color: transparent; border: none;")
        self._choose_game_back_button.released.connect(lambda x=self._choose_game_back_button: self._button_released(x))

        self._choose_game_type_layout = QtWidgets.QVBoxLayout()
        self._choose_game_type_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._choose_game_type.setLayout(self._choose_game_type_layout)

        self._choose_game_type_label = QtWidgets.QLabel("Choose your adversary:")
        self._choose_game_type_layout.addWidget(self._choose_game_type_label)

        self._choose_game_type_human = QtWidgets.QPushButton("Player vs Player")
        self._choose_game_type_human.setFixedSize(200, 50)
        self._choose_game_type_human.setObjectName("choose_game_type_human")
        self._choose_game_type_human.released.connect(lambda x=self._choose_game_type_human: self._button_released(x))

        self._choose_game_type_ai = QtWidgets.QPushButton("Player vs AI")
        self._choose_game_type_ai.setFixedSize(200, 50)
        self._choose_game_type_ai.setObjectName("choose_game_type_ai")
        self._choose_game_type_ai.released.connect(lambda x=self._choose_game_type_ai: self._button_released(x))

        self._choose_game_type_layout.addWidget(self._choose_game_type_human)
        self._choose_game_type_layout.addWidget(self._choose_game_type_ai)

        # </editor-fold>

    def _new_game(self):
        self._content_widget.setCurrentWidget(self._choose_game_type)

    def _choose_ai(self):
        self._stop_game()  # Temporary

    def _start_game(self, ai=False):
        p1 = Player(self._board, Color.WHITE)
        p2 = Player(self._board, Color.BLACK)
        self._board.initialize(p1, p2)
        self._content_widget.setCurrentWidget(self._board_widget)

    def _stop_game(self):
        self._content_widget.setCurrentWidget(self._start_view)

    def _load_game(self):
        pass

    def _button_released(self, btn: QtWidgets.QWidget):
        if btn.objectName() == "back_button":
            dialog = QtWidgets.QMessageBox(self)
            dialog.setWindowTitle("Quit game")
            dialog.setText("Do you want to quit the game?")
            dialog.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            dialog.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
            if dialog.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                self._stop_game()
        elif btn.objectName() == "back_button_choose":
            self._content_widget.setCurrentWidget(self._start_view)
        elif btn.objectName() == "choose_game_type_human":
            self._start_game()
        elif btn.objectName() == "choose_game_type_ai":
            self._choose_ai()


    def _button_clicked(self, btn):
        pass




