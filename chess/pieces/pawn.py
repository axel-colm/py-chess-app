from .piece import Piece
from .color import Color
from ..board import Board


class Pawn(Piece):

    def __init__(self, board: Board, color: Color, position: tuple[int, int]):
        super().__init__(color, position)
        self._VALUE = 1
        self._board = board

    def canMove(self, end: tuple[int, int]):
        x1, y1 = self.getPosition()
        x2, y2 = end
        if not self._board.isInside(x2, y2):
            return False

        dx, dy = x2 - x1, y2 - y1
        direction = 1 if self._color is Color.WHITE else -1
        start_pos = 1 if self._color is Color.WHITE else self._board.BOARD_SIZE[1] - 2

        if dx == 0 and self._board.getCases(x2, y2) is None and (dy == direction or (y1 == start_pos and dy == 2 * direction and self.canMove((x1, y1 + direction)))):
            return True
        elif abs(dx) == 1 and dy == direction:
            case = self._board.getCases(x2, y2)
            case2 = self._board.getCases(x2, y2 - direction) if self._board.isInside(x2, y2 - direction) else None
            if isinstance(case, Piece):
                return case.getColor() != self._color
            else:
                return isinstance(case2, Pawn) and case2.getColor() != self._color and dy == start_pos

        return False

    def getMoves(self) -> list[tuple[int, int]]:
        moves = []

        for x_shift in range(-1, 2, 1):
            for y_shift in range(-1, 3, 1):
                if self.canMove((self._position[0] + x_shift, self._position[1] + y_shift)):
                    moves.append((self._position[0] + x_shift, self._position[1] + y_shift))
        return moves

    def move(self, end: tuple[int, int]):
        if self.canMove(end):
            self._board.setCase(self._position[0], self._position[1], None)
            self._board.setCase(end[0], end[1], self)
            self._position = end





