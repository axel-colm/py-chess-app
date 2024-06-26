from abc import ABC, abstractmethod

from ..pieces.color import Color
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
    _moves_history: list[tuple[Piece, tuple[int, int], tuple[int, int]]]
    _turn: Color | None

    def __init__(self):
        self._board = [[None for _ in range(self.BOARD_SIZE[0])] for _ in range(self.BOARD_SIZE[1])]
        self._turn = None

    @abstractmethod
    def initialize(self, p1, p2):
        pass

    @abstractmethod
    def getPlayer(self, color: Color) -> "Player":
        pass

    @abstractmethod
    def getTurnPlayer(self) -> "Player":
        pass

    def turnColor(self) -> Color | None:
        return self._turn

    def getCase(self, x: int, y: int) -> Piece | None:
        if not self.isInside(x, y):
            raise BoardException(1)
        return self._board[x][y]

    def isInside(self, x: int, y: int) -> bool:
        return 0 <= x < self.BOARD_SIZE[0] and 0 <= y < self.BOARD_SIZE[1]

    def isCheck(self, color: Color) -> bool:
        king = None
        for x in range(self.BOARD_SIZE[0]):
            for y in range(self.BOARD_SIZE[1]):
                piece = self.getCase(x, y)
                if isinstance(piece, Piece) and piece.getColor() == color and piece.__class__.__name__ == "King":
                    king = piece
                    break
        if king is None:
            raise BoardException(2)
        for x in range(self.BOARD_SIZE[0]):
            for y in range(self.BOARD_SIZE[1]):
                piece = self.getCase(x, y)
                if isinstance(piece, Piece) and piece.getColor() != color:
                    if piece.canMove(king.getPosition()):
                        return True
        return False

    def willBeCheck(self, start: tuple[int, int], end: tuple[int, int]) -> bool:
        case1 = self.getCase(start[0], start[1])
        case2 = self.getCase(end[0], end[1])
        self._board[start[0]][start[1]] = None
        self._board[end[0]][end[1]] = case1
        is_check = self.isCheck(case1.getColor())
        self._board[start[0]][start[1]] = case1
        self._board[end[0]][end[1]] = case2
        return is_check

    def getBoard(self):
        return self._board

    def setCase(self, x: int, y: int, piece: Piece | None):
        self._board[x][y] = piece

    def move(self, start: tuple[int, int], end: tuple[int, int]):
        piece = self.getCase(start[0], start[1])
        if piece is None:
            raise BoardException(2)
        if piece.canMove(end):
            piece.move(end)
            self._moves_history.append((piece, start, end))
            self._turn = Color.WHITE if self._turn == Color.BLACK else Color.BLACK
            return

        raise BoardException(3)

    def history(self):
        return self._moves_history

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



