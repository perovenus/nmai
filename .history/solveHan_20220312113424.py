from tkinter import E
from generation import *
from drawdomino import *

class Solve:
    def __init__(self, cas, n) -> None:
        self.canvas = cas
        self.size = n
        self.board = Board(cas, n)
        self.board.drawboard()
    def solve(self):
        self.path = []
        res =[]
        res = self.DFS(self.board, self.path, 0 ,0)
        if res:
            print("Da tim dc dg di")
            for i  in self.path:
                drawdomino(self.canvas, i[0], i[1])
        else:
            print("Ko tim dc dg di")
            for i  in self.path:
                drawdomino(self.canvas, i[0], i[1])
    def isLegal(self, check_board, x0, x1):
        if  check_board[x0][x1] :
            return False
        return True
    def isValid(self, n, x , y):
        if 0<= x < n + 1  and 0<= y < n + 2:
            return True
        return False
    def Get_Edges(self, x, y):
        moves = [
            [0, -1],
            [0, 1],
            [-1, 0],
            [1, 0]
        ]
        Edges = []
        for move in moves:
            x_next =  x + move[0]
            y_next = y+ move[1]
            if self.isValid(self.size, x_next, y_next) :
                if self.board.visited[x_next][]

        return Edges

    def DFS(self, board, path, x, y):
        print(f'My step  at {x} {y}')
        if self.isValid(self.size, x , y):
            self.board.visited[x][y] = True
        else:
            if x >= self.size  + 1 and y < self.size + 2:
                return self.DFS(board, path, 0 , y + 1)
            elif y >= self.size + 2:
                return False
        if len(path) == (self.size + 2)*(self.size + 1):
            return True
        Edges = self.Get_Edges( x ,y)
        print(f'My legal moves ', Edges)
        if len(Edges) == 0:
            return False
        for move in Edges:
            first = self.board.Cells[x][y].value
            second = self.board.Cells[x + move[0]][y + move[1]].value
            cell0  = self.board.Cells[x][y]
            cell1 = self.board.Cells[x + move[0]][y + move[1]]
            print(f'My domino [{cell0.value} | {cell1.value}]')
            path.append([cell0, cell1])
            if len(path) == (self.size + 2)*(self.size + 1):
                return True
            result =  self.DFS(board, path, x + 1, y)
            if result:
                return result   
            self.board.numbersexist[first][second] = False
            self.board.visited[x][y] = False
            path.pop()
        return False
