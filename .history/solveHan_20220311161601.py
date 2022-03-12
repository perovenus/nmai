from generation import *
from drawdomino import *
def legalmove(x_pos, y_pos, board, cas):
    # to left
    if 
    drawdomino(cas, board.Cells[x_pos][y_pos],board.Cells[x_pos][y_pos - 1])
    # to right
    drawdomino(cas, board.Cells[x_pos][y_pos],board.Cells[x_pos][y_pos + 1])
    # up to
    drawdomino(cas, board.Cells[x_pos][y_pos],board.Cells[x_pos-1][y_pos])
    # down to
    drawdomino(cas, board.Cells[x_pos + 1][y_pos],board.Cells[x_pos][y_pos])
    # is legal
def move_forward():
    pass
def move_backward():
    pass
def solveHan(cas):
    board = Board(cas, 3) # 3 là số lớn nhất trên bàn cờ
    board.drawboard()
    legalmove(0, 1, board, cas)
