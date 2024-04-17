from .board import Board
from .pieces.color import Color


class Player(object):
    _color: Color

    def __init__(self, board: Board, color: Color, name: str = None, profile_picture: str = None):
        self._color = color
        self._board = board
        if name is None:
            self._name = f"Player {color.name}"
        self._name = name
        self._profile_picture = profile_picture

    def getName(self):
        return self._name

    def getProfilePicture(self):
        return self._profile_picture

    def getColor(self) -> Color:
        return self._color

    def isMyTurn(self):
        return self._board.turnColor() == self.getColor()

    def move(self, start: tuple[int, int], end: tuple[int, int]):
        if self.isMyTurn():
            case = self._board.getCase(start[0], start[1])
            if case is not None and case.getColor() == self.getColor():
                self._board.move(start, end)
                return True
        return False

    def __str__(self):
        return f"Player {self._color.name}"
