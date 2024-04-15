from .pieces.color import Color


class Player(object):
    _color: Color

    def __init__(self, color: Color):
        self._color = color

    def getColor(self) -> Color:
        return self._color

    def __str__(self):
        return f"Player {self._color.name}"