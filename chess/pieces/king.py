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

    def isCheck(self):
        for x in range(self._board.BOARD_SIZE[0]):
            for y in range(self._board.BOARD_SIZE[1]):
                piece = self._board.getCase(x, y)
                if isinstance(piece, Piece) and piece.getColor() != self.getColor():
                    if piece.canMove(self.getPosition()):
                        return True
        return False

    def canMove(self, end: tuple[int, int]):
        x1, y1 = self.getPosition()
        x2, y2 = end
        if not self._board.isInside(x2, y2):
            return False
        case = self._board.getCase(x2, y2)
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 if case is None or case.getColor() != self.getColor() else False:
            return True
        return False