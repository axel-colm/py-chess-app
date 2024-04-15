from abc import ABC
from ..pieces.piece import Piece


class BoardException(Exception):
    errors = {
        1: "Position out of board",
        2: "No piece at this position",
        3: "Invalid move"
    }

    def __init__(self, error_code: int, **kwargs):
        self._code = error_code

    def __str__(self):
        return f"BoardException {self._code}: {self.errors[self._code]}"


class Board(ABC):
    BOARD_SIZE = (8, 8)
    _board: list[list[Piece | None]]

    def __init__(self):
        self._board = [[None for _ in range(self.BOARD_SIZE[0])] for _ in range(self.BOARD_SIZE[1])]

    def getCases(self, x: int, y: int) -> Piece | None:
        if not self.isInside(x, y):
            raise BoardException(1)
        return self._board[x][y]

    def isInside(self, x: int, y: int) -> bool:
        return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]

    def getBoard(self):
        return self._board

    def setCase(self, x: int, y: int, piece: Piece | None):
        self._board[x][y] = piece

    def move(self, start: tuple[int, int], end: tuple[int, int]):
        piece = self.getCases(start[0], start[1])
        if piece is None:
            raise BoardException(2)
        if piece.canMove(end):
            piece.move(end)
            return
        raise BoardException(3)

    def str(self):
        str_board = ""
        for row in self._board:
            for piece in row:
                if piece is None:
                    str_board += "."
                else:
                    name = piece.__class__.__name__[:2]
                    if name == "Kn":
                        name = "N"
                    color = piece.getColor().name[0].lower()
                    str_board += f"{name[0]}{color}"
                str_board += "\t"
            str_board += "\n"
        return str_board



