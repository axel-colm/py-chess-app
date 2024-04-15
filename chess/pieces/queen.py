from .rook import Rook
from .bishop import Bishop
from .color import Color
from ..board.board import Board, BoardException


class Queen(Rook, Bishop):

    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        Rook.__init__(self, board, color, position)
        Bishop.__init__(self, board, color, position)
        self._VALUE = 9

    def move(self, end: tuple[int, int]):
        if self.canMove(end):
            self._board.setCase(self.getPosition()[0], self.getPosition()[1], None)
            self._board.setCase(end[0], end[1], self)
            self._position = end
        else:
            raise BoardException(3)

    def getMoves(self) -> list[tuple[int, int]]:
        moves = Rook.getMoves(self)
        moves.extend(Bishop.getMoves(self))
        return moves

    def canMove(self, end: tuple[int, int]):
        return Rook.canMove(self, end) or Bishop.canMove(self, end)