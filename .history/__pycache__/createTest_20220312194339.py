from random import choice, shuffle
from xml import dom
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
        print(f'My step  at {x} {y}')
        if self.isValid(self.size, x , y):
            if self.visited[x][y] == True:
                if x >= self.size  + 1 and y < self.size + 2:
                    return self.createTest( 0 , y + 1)
                elif y >= self.size + 2:
                    return True
                return self.createTest( x+1 , y )
        else:
            if x >= self.size  + 1 and y < self.size + 2:
                return self.createTest( 0 , y + 1)
            elif y >= self.size + 2:
                return True
        if self.count == self.total:
            return True
        Edges = self.Get_Edges( x ,y)
        shuffle(Edges)
        print(f'My legal moves ', Edges)
        if len(Edges) == 0:
            return False
        domino = self.values.pop()
        for move in Edges:
            self.visited[x][y] = True
            if self.visited[x + move[0]][y + move[1]]:
                return self.createTest( x+1 , y )
            # first = self.board.Cells[x][y].value
            # second = self.board.Cells[x + move[0]][y + move[1]].value
            # cell0  = self.board.Cells[x][y]
            # cell1 = self.board.Cells[x + move[0]][y + move[1]]
            self.board[x][y] = domino[0]
            self.board[x+ move[0]][y  + move[1]] = domino[1]
            self.visited[x + move[0]][y + move[1]] = self.visited[x][y] = True
            self.count += 1
            if self.count == self.total:
                return True
            result =  self.createTest( x+1 , y )
            if result:
                return result   
            self.visited[x + move[0]][y + move[1]] = self.visited[x][y] = False
            self.values.append(domino)
            self.count -=1
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
            x_next = x + move[0]
            y_next = y + move[1]
            if self.isValid(self.size, x_next, y_next):
                print(f"x_next :{x_next} y_next: {y_next}")
                Edges.append(move)
        return Edges
    
P = CreateTest(3)
P.createTest(0,0)
print(P.board)