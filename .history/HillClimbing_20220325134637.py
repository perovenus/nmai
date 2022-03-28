from time import sleep

from cv2 import solve
from generation import *
from drawdomino import *
from numpy import argmax, array
class HillClimbing:
    def __init__(self, cas, n) -> None:
        self.canvas = cas
        self.size = n
        self.board = Board(cas, n)
        self.board.drawboard()
        self.visited = [] # để check xem là cái vị trí trên board game
        self.domino = [] # n + 1 x  n + 1
        self.positions = [] # listposition trí chưa chọn 
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
        self.total = (n + 1) * (n + 2)/2
    def solve(self):
        res = self.hillclimbing()
        if res:
            print("Da tim dc loi giai toi uu")
        else:
            print("Day la loi giai cuoi cung")
    def hillclimbing(self):
        case = []
        #####################
        # self.canvas.update()
        # sleep(0.5)
        # self.canvas.delete("all")
        # self.board.drawboard()
        # self.draw()
        # self.canvas.update()
        ######################
        if self.total == 0:
            return True
        if self.positions == [] and self.total != 0:
            return False
        pos = self.positions.pop() 
        poslist  = self.Get_Edges(pos[0], pos[1])
        shuffle(poslist)
        ##body 
        while poslist == []  and len(self.positions) > 0:
            pos = self.positions.pop() 
            poslist  = self.Get_Edges(pos[0], pos[1])
        if len(self.positions) == 0 and poslist == []:
            return False
        cell0 =  self.board.Cells[pos[0]][pos[1]]
        for p in poslist:
            cell1 = self.board.Cells[p[0]][p[1]]
            x, y = cell0.value, cell1.value
            if self.domino[x][y]:
                self.visited[p[0]][p[1]] =  False
                self.visited[pos[0]][pos[1]] =  False
                self.positions.remove([p[0],p[1]])
                self.domino[x][y] = self.domino[y][x] = False
                # self.path.append([cell0, cell1])
                # self.total -= 1
                # return self.hillclimbing()
                # self.visited[p[0]][p[1]] =  True
                # self.visited[pos[0]][pos[1]] =  False
                # self.positions.remove([p[0],p[1]])
                # self.domino[x][y] = self.domino[y][x] = False
                case.append(self.check(self.positions))
                self.visited[p[0]][p[1]] =  True
                self.visited[pos[0]][pos[1]] = True
                self.positions.append([p[0],p[1]])
                self.domino[x][y] = self.domino[y][x] = True
        if case != []:
            p = poslist[argmax(case)]
            cell1 = self.board.Cells[p[0]][p[1]]
            x, y = cell0.value, cell1.value
            self.visited[p[0]][p[1]] =  False
            self.visited[pos[0]][pos[1]] =  False
            self.positions.remove([p[0],p[1]])
            self.domino[x][y] = self.domino[y][x] = False
            self.path.append([cell0, cell1])
            self.total -= 1
            return self.hillclimbing()
        if len(self.positions) == 2:
            return False
        return self.hillclimbing()

    def check(self, path):
        count  = 0
        for pos in path:
            if len(self.Get_Edges(pos[0],pos[1])) > 0:
                count  +=  1
        return count
    def draw(self):
        for i  in self.path:
                drawdomino(self.canvas, i[0], i[1])
    def isValid(self, x , y):
        if (0 <= x < self.size + 1 and  0 <= y < self.size + 2) and self.visited[x][y]:
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
                    cell0 =  self.board.Cells[x][y]
                    cell1 =  self.board.Cells[x_next][y_next]
                    x1, y1 = cell0.value, cell1.value
                    if self.domino[x1][y1]:
                        res.append([x_next, y_next])

        return res
    #write function to get pri

   