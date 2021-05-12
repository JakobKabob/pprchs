import numpy as np

class P: 
    def __init__(self, x, y):
        self.x, self.y = x, y

class Ki: 
    def __init__(self, x, y):
        self.x, self.y = x, y

class Q: 
    def __init__(self, x, y):
        self.x, self.y = x, y

class R: 
    def __init__(self, x, y):
        self.x, self.y = x, y

class B: 
    def __init__(self, x, y):
        self.x, self.y = x, y

class Kn: 
    def __init__(self, x, y):
        self.x, self.y = x, y


black = [R(8,8),Kn(7,8),B(6,8),Kn(5,8),Q(4,8),B(3,8),Kn(2,8),R(1,8),
        P(8,7),P(7,7),P(6,7),P(5,7),P(4,7),P(3,7),P(2,7),P(1,7)] 

white = [R(8,1),Kn(7,1),B(6,1),Kn(5,1),Q(4,1),B(3,1),Kn(2,1),R(1,1),
        P(8,2),P(7,2),P(6,2),P(5,2),P(4,2),P(3,2),P(2,2),P(1,2)] 

def display_chesspieces():
    board = np.zeros((8,8), 'U1')
    for piece in black:
        board[piece.x-1][piece.y-1] = type(piece).__name__
    for piece in white:
        board[piece.x-1][piece.y-1] = type(piece).__name__
    return board


