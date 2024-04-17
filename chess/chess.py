from .board.board import Board
from .pieces.color import Color
from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.pawn import Pawn
from .pieces.rook import Rook
from .pieces.knight import Knight
from .player import Player


class Chess(Board):
    _player1: Player | None = None
    _player2: Player | None = None

    def __init__(self):
        super().__init__()
        self._moves_history = []

    def clear(self):
        for x in range(8):
            for y in range(8):
                self.setCase(x, y, None)

    def getPlayer(self, color: Color) -> "Player":
        if self._player1.getColor() == color:
            return self._player1
        elif self._player2.getColor() == color:
            return self._player2
        raise ValueError("Color not found")

    def getTurnPlayer(self) -> "Player":
        return self.getPlayer(self._turn)

    def initialize(self, player1: Player, player2: Player):
        self.clear()
        self._moves_history = []

        if player1.getColor() == player2.getColor():
            raise ValueError("Both players have the same color")

        self._player1 = player1
        self._player2 = player2

        for color in (Color.WHITE, Color.BLACK):
            for x in range(8):
                self.setCase(x, 1 if color == Color.BLACK else 6, Pawn(self, color, (x, 1 if color == Color.BLACK else 6)))

            for x, piece in enumerate((Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)):
                self.setCase(x, 0 if color == Color.BLACK else 7, piece(self, color, (x, 0 if color == Color.BLACK else 7)))

        self._turn = Color.WHITE












