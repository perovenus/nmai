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
        check_board[x0][x1] = True
        return True
    def isValid(self, n, x , y):
        if 0<= x < n  and 0<= y < n + 1:
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
            first = self.board.Cells[x][y].value
            if self.isValid(self.size, x + move[0], y + move[1]):
                second = self.board.Cells[x + move[0]][y + move[1]].value
                if self.isLegal(self.board.checkboard, first, second):
                    Edges.append(move)
                else:
                    continue
            else:
                continue
        return Edges

    def DFS(self, board, path, x, y):
        Edges = self.Get_Edges( x ,y)
        for move in Edges:
            first = self.board.Cells[x][y].value
            second = self.board.Cells[x + move[0]][y + move[1]].value
            cell0  = self.board.Cells[X][Y]
            path.append([self.board.Cells[X][]])
            result =  self.DFS(board, path, x + 1, y)
            if len(result) == (board.Size + 1)* (board.Size + 2) / 2:
                return path
            self.board.checkcell[first][second] = False
            path.pop()
        