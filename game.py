import numpy as np

class Game:
    def __init__(self):
        cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        rows = range(0,8)
        self.chessboard = []
        for col in cols:
            for row in rows:
                self.chessboard.append({"col": col, "row": row})
a = Game()
print(a.chessboard)
