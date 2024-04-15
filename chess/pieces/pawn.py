from .piece import Piece
from .color import Color
from ..board import Board


class Pawn(Piece):

    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        super().__init__(color, position)
        self._VALUE = 1
        self._board = board







