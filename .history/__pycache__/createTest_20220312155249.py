from random import choice, shuffle
class CreateTest:
    def __init__(self, n) -> None:
        self.x = 0
        self. y = 0
        self.board = []
        self.size = n
        self.values  = []
        for i in range(n + 1):
            for j in range( i + 1):
                self.values.append([i, j])
        shuffle(self.values)
    def createTest(self):
        edges = self.Get_Edges(self.x, self.y)
        move  = choice(edges)
        
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
            if self.isValid(self.size, x_next, y_next):
                Edges.append(move)
        return Edges
