from .piece import Piece
from .color import Color
from ..board.board import Board, BoardException


class King(Piece):
    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        Piece.__init__(self, color, position)
        self._board = board
        self._value = 100

    def move(self, end: tuple[int, int]):
        if self.canMove(end):
            self._board.setCase(self.getPosition()[0], self.getPosition()[1], None)
            self._board.setCase(end[0], end[1], self)
            self._position = end
        else:
            raise BoardException(3)

    def getMoves(self) -> list[tuple[int, int]]:
        x, y = self.getPosition()
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.canMove((x + i, y + j)):
                    moves.append((x + i, y + j))
        return moves

    def canMove(self, end: tuple[int, int]):
        x1, y1 = self.getPosition()
        x2, y2 = end
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            return True
        return False