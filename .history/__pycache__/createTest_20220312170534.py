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
    def createTest(self, x, y):
        if self.isValid(self.size, x , y):
            if self.board.visited[x][y] == True:
                if x >= self.size  + 1 and y < self.size + 2:
                    return self.DFS(board, path, 0 , y + 1)
                elif y >= self.size + 2:
                    return True
                return self.DFS(board, path, x+1 , y )
        else:
            if x >= self.size  + 1 and y < self.size + 2:
                return self.DFS(board, path, 0 , y + 1)
            elif y >= self.size + 2:
                return True
        edges = self.Get_Edges(self.x, self.y)
        shuffle(edges)
        domino = self.values.pop()
        for move in edges:
            x_pos = x + move[0]
            y_pos = y + move[0]
            self.board[x][y] = domino[0]
            self.board[x + move[0]][y + move[1]] = domino[1]
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
    
P = CreateTest(3)