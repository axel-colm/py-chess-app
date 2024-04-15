from chess import Chess
from chess.pieces import Color
from chess.pieces.knight import Knight

board = Chess()
knights = Knight(board, Color.WHITE, (0, 0))
board.setCase(*knights.getPosition(), knights)
print(board.str())
print(knights.getMoves())