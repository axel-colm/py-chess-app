from ..board import Board
from .piece import Piece
from .color import Color


class Knight(Piece):
    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        super().__init__(color, position)
        self._board = board
        self._VALUE = 3

    def move(self, end: tuple[int, int]):
        if self.canMove(end):
            self._board.setCase(self._position[0], self._position[1], None)
            self._board.setCase(end[0], end[1], self)
            self._position = end

    def getMoves(self) -> list[tuple[int, int]]:
        x, y = self.getPosition()
        moves = [(x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2), (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1)]
        return [move for move in moves if self.canMove(move)]

    def canMove(self, end: tuple[int, int]):
        x1, y1 = self.getPosition()
        x2, y2 = end
        if not self._board.isInside(x2, y2):
            return False

        dx, dy = x2 - x1, y2 - y1
        if (dx, dy) in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            case = self._board.getCases(x2, y2)
            return case is None or case.getColor() != self._color
        return False
