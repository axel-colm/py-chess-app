from .piece import Piece
from .color import Color
from ..board.board import BoardException


class Bishop(Piece):

    _VALUE = 3

    def __init__(self, board, color: Color, position: tuple[int, int]):
        super().__init__(color, position)
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
        for x_shift in range(-1, 2, 2):
            for y_shift in range(-1, 2, 2):
                for i in range(1, 8):
                    x = self.getPosition()[0] + i * x_shift
                    y = self.getPosition()[1] + i * y_shift
                    if self._board.isInside(x, y):
                        piece = self._board.getCases(x, y)
                        if piece is None:
                            moves.append((x, y))
                        else:
                            if piece.getColor() != self.getColor():
                                moves.append((x, y))
                            break
                    else:
                        break
        return moves

    def canMove(self, end: tuple[int, int]):
        x1, y1 = self.getPosition()
        x2, y2 = end

        if abs(x1 - x2) == abs(y1 - y2):
            for i in range(1, abs(x1 - x2)):
                if self._board.getCases(x1 + i * (1 if x2 > x1 else -1), y1 + i * (1 if y2 > y1 else -1)) is not None:
                    return False
            return True
        return False

