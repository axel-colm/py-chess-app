from .color import Color
from abc import ABC, abstractmethod


class Piece(ABC):
    _position: tuple
    _color: Color
    _VALUE: int

    def __init__(self, color: Color, position: tuple[int, int]):
        self._color = color
        self._position = position

    def getColor(self):
        return self._color

    def getValue(self):
        return self._VALUE

    def getPosition(self):
        return self._position

    @abstractmethod
    def move(self, end: tuple[int, int]):
        pass

    @abstractmethod
    def getMoves(self) -> list[tuple[int, int]]:
        pass

    @abstractmethod
    def canMove(self, end: tuple[int, int]):
        pass


