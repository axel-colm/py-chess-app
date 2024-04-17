from .piece import Piece
from .color import Color
from ..board.board import BoardException, Board


class Bishop(Piece):

    _VALUE = 3

    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        Piece.__init__(self, color, position)
        self._board = board

    def move(self, end: tuple[int, int]):
        if self.canMove(end):
            self._board.setCase(end[0], end[1], self)
            self._board.setCase(self.getPosition()[0], self.getPosition()[1], None)
            self._position = end
        else:
            raise BoardException(3)

    def getMoves(self) -> list[tuple[int, int]]:
        moves = []
        x, y = self.getPosition()
        for i in range(1, max(self._board.BOARD_SIZE)):
            if self.canMove((x + i, y + i)):
                moves.append((x + i, y + i))
            if self.canMove((x + i, y - i)):
                moves.append((x + i, y - i))
            if self.canMove((x - i, y + i)):
                moves.append((x - i, y + i))
            if self.canMove((x - i, y - i)):
                moves.append((x - i, y - i))
        return moves

    def canMove(self, end: tuple[int, int]):
        x1, y1 = self.getPosition()
        x2, y2 = end
        if not self._board.isInside(x2, y2):
            return False

        dx, dy = x2 - x1, y2 - y1
        if abs(dx) == abs(dy):
            for i in range(1, abs(dx)):
                x = x1 + i * (dx // abs(dx))
                y = y1 + i * (dy // abs(dy))
                if self._board.getCase(x, y) is not None:
                    return False
            case = self._board.getCase(x2, y2)
            return (case is None or case.getColor() != self.getColor()) and not self._board.willBeCheck((x1, y1), end)
        return False

