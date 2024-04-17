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
        direction = 1 if self._color is Color.BLACK else -1
        start_pos = 1 if self._color is Color.BLACK else self._board.BOARD_SIZE[1] - 2

        if dx == 0 and self._board.getCase(x2, y2) is None and (dy == direction or (y1 == start_pos and dy == 2 * direction and self.canMove((x1, y1 + direction)))):
            return True
        elif abs(dx) == 1 and dy == direction:
            case = self._board.getCase(x2, y2)
            if isinstance(case, Piece):
                return case.getColor() != self._color
            else:
                last_move = self._board.history()[-1] if len(self._board.history()) > 0 else None
                if last_move is not None:
                    piece, start, end = last_move
                    if isinstance(piece, Pawn) and  piece.getColor() != self._color and y1 == end[1] and abs(start[1] - end[1]) == 2 and abs(x1 - end[0]) == 1:
                        return True
        return False

    def getMoves(self) -> list[tuple[int, int]]:
        moves = []

        for x_shift in range(-1, 2, 1):
            for y_shift in range(-2, 3, 1):
                if self.canMove((self._position[0] + x_shift, self._position[1] + y_shift)):
                    moves.append((self._position[0] + x_shift, self._position[1] + y_shift))
        return moves

    def move(self, end: tuple[int, int]):
        if self.canMove(end):
            x1, y1 = self._position
            x2, y2 = end
            last_move = self._board.history()[-1] if len(self._board.history()) > 0 else None
            if last_move is not None:
                piece, start, end = last_move
                if isinstance(piece, Pawn) and piece.getColor() != self._color and y1 == end[1] and abs(start[1] - end[1]) == 2 and abs(x1 - end[0]) == 1:
                    self._board.setCase(end[0], end[1], None)

            self._board.setCase(self._position[0], self._position[1], None)
            self._board.setCase(x2, y2, self)


            self._position = (x2, y2)





