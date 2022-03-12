from generation import *
from drawdomino import *

def isLegal(check_board, x0,x1):
    if  check_board[x0][x1] :
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
def isValid(n, x , y):
    if 0<= x < n  and 0<= y < n:
        return True
    return False
def Get_Edges(board, x, y):
    moves = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0]
    ]
    Edges = []
    for move in moves:
        first = board.Cells[x][y]
        if isValid(board.Size, x + move[0], y + move[1]):
            second = board.Cells[x + move[0]][y + move[1]]
            if isLegal(board.checkboard, first, second):
                Edges.append(move)
            else:
                continue
        else:
            continue
    return Edges

def DFS(board, path, x, y):
    if  len(path) == board.Size:
        return path
    Ed