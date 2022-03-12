from generation import *
from drawdomino import *
def legalmove(x_pos, y_pos, board, cas):
    # to left
    moves = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0]
    ]
    drawdomino(cas, board.Cells[x_pos][y_pos],board.Cells[x_pos][y_pos - 1])
    # to right
    drawdomino(cas, board.Cells[x_pos][y_pos],board.Cells[x_pos][y_pos + 1])
    # up to
    drawdomino(cas, board.Cells[x_pos][y_pos],board.Cells[x_pos - 1][y_pos])
    # down to
    drawdomino(cas, board.Cells[x_pos][y_pos],board.Cells[x_pos + 1][y_pos])
    # is legal
def isLegal(check_board, x0,x1):
    if  check_board[x0][x1] or x0 < 0 or x0 > len(check_board[0]):
        return False
    check_board[x0][x1] = True
    return True


def move_forward():
    pass
def move_backward():
    pass
def solveHan(cas):
    board = Board(cas, 3) # 3 là số lớn nhất trên bàn cờ
    board.drawboard()
    legalmove(0, 1, board, cas)
def Get_Edges(check_board, x, y):
    moves = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0]
    ]
    Edges = []
    for move in moves:
        if isLegal(check_board, x + move[0], y + move[1]):
            Edges.append(move)

def DFS(path , n):
    if  len(path) == n:
        return path
    