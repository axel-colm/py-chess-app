from .piece import Piece
from .color import Color
from ..board.board import Board, BoardException


class Queen(Piece):
    _VALUE = 9

    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        super().__init__(color, position)
        self._board = board

    def move(self, end: tuple[int, int]):
        pass

    def getMoves(self) -> list[tuple[int, int]]:
        pass

    def canMove(self, end: tuple[int, int]):
        pass