from .piece import Piece
from .color import Color
from ..board import Board


class Rook(Piece):
    _VALUE = 5

    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        super().__init__(color, position)
        self._board = board

    def move(self, end: tuple[int, int]):
        pass

    def getMoves(self) -> list[tuple[int, int]]:
        pass

    def canMove(self, end: tuple[int, int]):
        pass
