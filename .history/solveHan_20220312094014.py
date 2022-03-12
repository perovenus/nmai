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
    if  len(path) == (board.Size + 1)* (board.Size + 2 / 2:
        return path
    if isValid(board.Size, x, y): # neu nhu o hien tai la hop le  
        if board.checkcell[x][y]: #kiem tra xem o do da thuoc domino nao chua
            return DFS(board, path, x + 1, y) # di chuyen sang o tiep theo
    else: # neu nhu vi tri hien tai ko lop le => 2TH => di het 1 hang or di het ban co r
        if x >= board.Size  : # di chuyen sang cot moi
            if y <  board.Size + 1: # chua di het ban co
                return DFS(board, path, 0, y + 1) 
            return False
    Edges = Get_Edges(board, x ,y)
    for edge in Edges:
        x_pos = x + edge[0]
        y_pos = y + edge[1]
        path.append([board.Cells[x][y],board.Cells[x_pos][y_pos]])
        result =  DFS(board, path, x + 1, y)
        if result:
            return path
    