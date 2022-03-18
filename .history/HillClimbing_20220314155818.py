from time import sleep
from generation import *
from drawdomino import *
from numpy import array
class HillClimbing:
    def __init__(self, cas, n) -> None:
        self.canvas = cas
        self.size = n
        self.board = Board(cas, n)
        self.board.drawboard()
        self.visited = []
        self.domino = []
        self.positions = []
        for i in range(n + 1):
            self.visited.append([])
            self.domino.append([])
            for j in range(n + 2):
                self.positions.append([i, j])
                self.visited[i].append(True)
                if j < n + 1:
                    self.domino[i].append(True)
        shuffle(self.positions)
        self.path = []
    def solve(self):
        self.canvas.update()
        sleep(0.5)
        self.canvas.delete("all")
        self.board.drawboard()
        self.draw()
        self.canvas.update()
        pos = self.positions.pop() 
        poslist  = self.Get_Edges(pos[0], pos[1])
        if poslist == [] and len():
            return
        for p in poslist:
            cell0 =  self.board.Cells[pos[0]][pos[1]]
            cell1 = self.board.Cells[p[0]][p[1]]
            x, y = cell0.value, cell1.value
            if self.domino[x][y]:
                self.visited[p[0]][p[1]] = False
                self.visited[pos[0]][pos[1]] = False
                self.positions.remove([p[0],p[1]])
                self.domino[x][y] = False
                self.path.append([cell0, cell1])
                return self.solve()
        
    def draw(self):
        for i  in self.path:
                drawdomino(self.canvas, i[0], i[1])
    def isValid(self, x , y):
        if (0 <= x < self.size + 1 and  0 <= y < self.size + 1) and self.visited[x][y]:
            return True
        return False
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
            y_next = y + move[1]
            if self.isValid(x_next, y_next):
                res.append([x_next, y_next])
        return res

   