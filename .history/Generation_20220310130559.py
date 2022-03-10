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
        for i in range(self.Size + 2):
            x0 = i * 60
            x1 = i * 60 + 60
            for j in range(self.Size + 2):
                y0 = j * 60
                y1 = j * 60 + 60
                index  = (self.Size + 2) * i + j
                self.values[index] %= self.Size + 1
                self.Cells.append(Cell(x0, y0, x1, y1, self.values[index]))
        return self.Cells
    def drawboard(self):
        cells = self.pre()
        for cell in cells:
            self.canvas.create_rectangle(cell.x0, cell.y0, cell.x1, cell.y1)
            # self.canvas.create_text(cell.x0 + 30, cell.y0 + 30, cell.value)
