from chess import Chess
from chess.pieces import Color
from chess.pieces.bishop import Bishop
from chess.pieces.pawn import Pawn

board = Chess()
p = Bishop(board, Color.WHITE, (3, 3))
p2 = Pawn(board, Color.BLACK, (5, 5))
board.setCase(*p.getPosition(), p)
board.setCase(*p2.getPosition(), p2)
moves = p.getMoves()
print(moves)
for x in range(8):
    for y in range(8):
        case = board.getCases(x, y)
        if case is None and (x, y) in moves:
            print("x", end="\t")
        elif case is not None:
            print(case.__class__.__name__[:2] + case.getColor().name[0].lower(), end="\t")
        else:
            print(".", end="\t")

    print()