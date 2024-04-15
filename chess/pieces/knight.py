from ..board import Board
from .piece import Piece
from .color import Color


class Knight(Piece):
    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        super().__init__(color, position)
        self._board = board
        self._VALUE = 3

    def move(self, end: tuple[int, int]):
        pass

    def getMoves(self) -> list[tuple[int, int]]:
        pass

    def canMove(self, end: tuple[int, int]):
        pass