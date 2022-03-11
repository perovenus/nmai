from multiprocessing.spawn import prepare
from random import shuffle
class Cell:
    def __init__(self, x0, y0, x1, y1, value):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.value = value
class Board:
    def __init__(self, canvas, n):
        self.canvas = canvas
        self.Size = n
        self.values = list(range((n + 1)*(n + 2)))
        shuffle(self.values)
        self.Cells = []
    def pre(self):
        for i in range(self.Size + 1):
            x0 = i * 60
            x1 = i * 60 + 60
            self.Cells.append([])
            for j in range(self.Size + 1):
                y0 = j * 60
                y1 = j * 60 + 60
                index  = (self.Size + 1) * i + j
                self.values[index] %= self.Size + 1
                self.Cells[i].append(Cell(x0, y0, x1, y1, self.values[index]))
    def drawboard(self):
        self.pre()
        for cell in self.Cells:
            for v in cell:
                self.canvas.create_rectangle(v.x0, v.y0, v.x1, v.y1)
                self.canvas.create_text(v.x0 + 30, v.y0 + 30, text = v.value)
