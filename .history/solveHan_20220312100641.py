from typing import Sized
from generation import *
from drawdomino import *


def solveHan(cas):
    board = Board(cas, 3) # 3 là số lớn nhất trên bàn cờ
    board.drawboard()
    path = []
    res =[]
    res = DFS(board, path, 0 ,0)
    if res:
        print("Da tim dc dg di")
        for i  in path:
            drawdomino(cas, i[0], i[1])
    else:
        print("Ko tim dc dg di")
        for i  in path:
            drawdomino(cas, i[0], i[1])
def isLegal(check_board, x0,x1):
    if  check_board[x0][x1] :
        return False
    check_board[x0][x1] = True
    return True
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
    Edges = Get_Edges(board, x ,y)
    for edge in Edges:
        result =  DFS(board, path, x + 1, y, edge)
        if len(result) == (board.Size + 1)* (board.Size + 2) / 2:
            return path
        path.pop()
    