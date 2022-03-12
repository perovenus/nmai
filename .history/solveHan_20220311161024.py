from generation import *
from drawdomino import *
def legalmove(x_pos, y_pos, board, cas):
    # to left
    drawdomino(cas, board.Cells[x_pos][y_pos],board.Cells[x_pos][y_pos])
    # to right
    # up to
    # down to
    # is legal
def move_forward():
    pass
def move_backward():
    pass
def solveHan(cas):
    board = Board(cas, 3) # 3 là số lớn nhất trên bàn cờ
    board.drawboard()
    legalmove(0, 0, board, cas)
