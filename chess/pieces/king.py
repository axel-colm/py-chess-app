from .piece import Piece
from .color import Color
from ..board.board import Board, BoardException


class King(Piece):
    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        Piece.__init__(self, color, position)
        self._board = board
        self._value = 100

    def move(self, end: tuple[int, int]):
        pass

    def getMoves(self) -> list[tuple[int, int]]:
        pass

    def canMove(self, end: tuple[int, int]):
        pass