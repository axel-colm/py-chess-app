from .board.board import Board
from .pieces.color import Color
from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.pawn import Pawn
from .pieces.rook import Rook
from .pieces.knight import Knight


class Chess(Board):
    def __init__(self):
        super().__init__()

    def clear(self):
        for x in range(8):
            for y in range(8):
                self.setCase(x, y, None)

    def initialize(self):
        self.clear()

        for color in (Color.WHITE, Color.BLACK):
            for x in range(8):
                self.setCase(x, 1 if color == Color.WHITE else 6, Pawn(self, color, (x, 1 if color == Color.WHITE else 6)))

            for x, piece in enumerate((Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)):
                self.setCase(x, 0 if color == Color.WHITE else 7, piece(self, color, (x, 0 if color == Color.WHITE else 7)))








