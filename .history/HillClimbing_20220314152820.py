from time import sleep
from generation import *
from drawdomino import *
class HillClimbing:
    def __init__(self, cas, n) -> None:
        self.canvas = cas
        self.size = n
        self.board = Board(cas, n)
        self.board.drawboard()
        self.visited = [[True]* (n + 2)]*(n + 1)
        self.domino = [[True]* (n + 1)]*(n + 1)
        self.positions = []
        for i in range(n + 1):
            for j in range(n + 2):
                self.positions.append([i, j])
        shuffle(self.positions)
        self.path = []
    def solve(self):
        pos = self.positions.pop()
        poslist  = self.Get_Edges(pos[0], pos[1])
        for p in poslist:
            x = self.board.Cells[pos[0]][pos[1]].value
            y = self.board.Cells[p[0]][p[1]].value
            if self.domino[x][y]:
                self.visited[p[0]][p[1]] = False
                self.visited[pos[0]][pos[1]] = False
                self.domino[x][y] = False
                return self.s


        
    def draw(self):
        for i  in self.path:
                drawdomino(self.canvas, i[0], i[1])
    def isLegal(self, x, y):
        pass
    def isValid(self, x , y):
        return self.visited[x][y]
    def Get_Edges(self, x, y):
        moves = [
            [0, -1],
            [0, 1],
            [-1, 0],
            [1, 0]
        ]
        res = []
        for move in moves:
            x_next =  x + move[0]
            y_next = y+ move[1]
            if self.isValid(x_next, y_next):

                return res.append([x_next, y_next])
        return res

   