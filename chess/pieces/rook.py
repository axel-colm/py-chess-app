from .piece import Piece
from .color import Color
from ..board import Board
from ..board.board import BoardException


class Rook(Piece):
    _VALUE = 5

    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        super().__init__(color, position)
        self._board = board

    def move(self, end: tuple[int, int]):
        if self.canMove(end):
            self._board.setCase(self.getPosition()[0], self.getPosition()[1], None)
            self._board.setCase(end[0], end[1], self)
            self._position = end
        else:
            raise BoardException(3)

    def getMoves(self) -> list[tuple[int, int]]:
        moves = []
        x, y = self.getPosition()
        for i in range(8):
            if i != x and self.canMove((i, y)):
                moves.append((i, y))
            if i != y and self.canMove((x, i)):
                moves.append((x, i))
        return moves

    def canMove(self, end: tuple[int, int]):
        x1, y1 = self.getPosition()
        x2, y2 = end

        if x1 == x2:
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                if self._board.getCases(x1, y) is not None:
                    return False
            return True
        elif y1 == y2:
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                if self._board.getCases(x, y1) is not None:
                    return False
            return True
