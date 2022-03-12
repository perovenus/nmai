from random import choice, shuffle
class CreateTest:
    def __init__(self, n) -> None:
        self.x = 0
        self. y = 0
        self.count = 0 
        self.total = (n + 1) * (n + 2)/2
        self.board = [[-1] * (n + 2)] *(n + 1)
        self.visited = [[False]*(n + 1)] *(n+1)
        self.size = n
        self.values  = []
        for i in range(n + 1):
            for j in range( i + 1):
                self.values.append([i, j])
        shuffle(self.values)
    def createTest(self, x = 0, y = 0):
        if self.isValid(self.size, x , y):
            if self.visited[x][y] == True:
                if x >= self.size  + 1 :
                    if y < self.size + 2:
                        return self.createTest(0, y +1)
                    else:
                        if self.count == self.total:
                            return True
                        return False
                else: # x < size + 1
                    if y < self.size + 2:
                        return self.createTest(x + 1, y)
                    else:
                        if self.count == self.total:
                            return True
                        return False
        else:
            if self.count == self.total:
                return True
            return False
        edges = self.Get_Edges(self.x, self.y)
        shuffle(edges)
        print(f"gia tri {x} {y}")
        print(edges)
        domino = self.values.pop()
        for move in edges:
            x_pos = x + move[0]
            y_pos = y + move[1]
            print(x_pos, y_pos)
            self.board[x][y] = domino[0]
            self.board[x_pos][y_pos] = domino[1]
            self.visited[x][y] =self.visited[x_pos][y_pos] = True
            self.count += 1
            if self.count == self.total:
                return True
            result = self.createTest(x + 1, y)
            if result:
                return result
            self.values.append(domino)
            self.visited[x][y] =self.visited[x_pos][y_pos] = False
            self.count -= 1
            self.createTest(x + 1, y)
    def isValid(self, n, x , y):
        if 0<= x < n + 1  and 0<= y < n + 2:
            print(f"A {x}{y}")
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
            y_next = y + move[1]
            print(f"x_next :{x")
            if self.isValid(self.size, x_next, y_next):
                Edges.append(move)
        return Edges
    
P = CreateTest(3)
P.createTest(0,0)
print(P.board)