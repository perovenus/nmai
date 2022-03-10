from random import shuffle
class Board:
    def __init__(self, n):
        self.Size = n
        self.values = list(range((n + 1)*(n + 2)))
        shuffle(self.values)
        self.Cells = []
        print(self.values)
    def drawboard(self):
        for i in range(self.Size + 1):
            x0 = i * 60
            x1 = i * 60 + 60
            for j in range(self.Size + 2):
                y0 = j * 60
                y1 = j * 60 + 60
                index  = (self.Size + 2) * i + j
                self.values[index] %= self.Size + 1
                self.Cells.append(Cell(x0, y0, x1, y1, self.values[index]))
        print([x, for ])

class Cell:
    def __init__(self, x0, y0, x1, y1, value):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.value = value
a = Board(3)
a.drawboard()