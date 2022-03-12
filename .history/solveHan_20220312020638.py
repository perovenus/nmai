from typing import Sized
from generation import *
from drawdomino import *

def isLegal(check_board, x0,x1):
    if  check_board[x0][x1] :
        return False
    check_board[x0][x1] = True
    return True

def solveHan(cas):
    board = Board(cas, 3) # 3 là số lớn nhất trên bàn cờ
    board.drawboard()
    path = []
    res =[]
    res = DFS(board, path, 0 ,0)
    if len(res) == (board.Size + 1)* board.Size / 2:
        print("Da tim dc dg di")
        for v in res:
            drawdomino(cas, v[0], v[1])
    else:
        print("Ko tim dc dg di")
        for v in res:
            drawdomino(cas, v[0], v[1])
def isValid(n, x , y):
    if 0<= x < n  and 0<= y < n + 1:
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
        first = board.Cells[x][y].value
        if isValid(board.Size, x + move[0], y + move[1]):
            second = board.Cells[x + move[0]][y + move[1]].value
            if isLegal(board.checkboard, first, second):
                Edges.append(move)
            else:
                continue
        else:
            continue
    return Edges

def DFS(board, path, x, y):
    print(len(path))
    if  len(path) == (board.Size + 1)* board.Size / 2:
        return path
    # di chuyen sang hang moi hoac cot moi
    if isValid(board.Size, x, y):
        if board.checkcell[x][y]:
            print(len(board.Cells))
            if x < len(board.Cells):
                return DFS(board, path,  x + 1, y)
            else:
                if y + 1 < len(board) + 1:
                    return DFS(board, path,  0, y + 1)
                return path
        board.checkcell[x][y] = True
    else:
        return path
    Edges = Get_Edges(board, x ,y)
    # print(Edges)
    # print(f'second {x}:{y}')
    for edge in Edges:
        path.append([board.Cells[x][y], board.Cells[x + edge[0]][y+ edge[1]]])
        result =  DFS(board, path, x + 1, y)
        if result:
            if len(result) == (board.Size + 1)* board.Size / 2:
                return result
        else:
            return path
        path.pop()