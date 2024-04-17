from .piece import Piece
from .color import Color
from ..board import Board
from ..board.board import BoardException


class Rook(Piece):
    _VALUE = 5

    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        Piece.__init__(self, color, position)
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
        if not self._board.isInside(x2, y2):
            return False

        case = self._board.getCase(x2, y2)

        if x1 == x2:
            for i in range(min(y1, y2) + 1, max(y1, y2)):
                if self._board.getCase(x1, i) is not None:
                    return False
            return (case is None or case.getColor() != self.getColor()) and not self._board.willBeCheck((x1, y1), end)
        elif y1 == y2:
            for i in range(min(x1, x2) + 1, max(x1, x2)):
                if self._board.getCase(i, y1) is not None:
                    return False
            return (case is None or case.getColor() != self.getColor()) and not self._board.willBeCheck((x1, y1), end)
