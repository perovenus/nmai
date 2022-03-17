from random import choice, shuffle
class CreateTest:
    def __init__(self, n) -> None:
        self.x = 0
        self. y = 0
        self.board = [[0] * (n +1)]
        self.size = n
        self.values  = []
        for i in range(n + 1):
            for j in range( i + 1):
                self.values.append([i, j])
        shuffle(self.values)
    def createTest(self, x, y):
        edges = self.Get_Edges(self.x, self.y)
        move  = choice(edges)
        domino = self.values.pop()
        if 
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
    def DFS(self, board, path, x, y):
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
        if len(path) == (self.size + 2)*(self.size + 1):
            return True
        Edges = self.Get_Edges( x ,y)
        print(f'My legal moves ', Edges)
        if len(Edges) == 0:
            return False
        for move in Edges:
            self.board.visited[x][y] = True
            if self.board.visited[x + move[0]][y + move[1]]:
                return self.DFS(board, path, x+1 , y )
            first = self.board.Cells[x][y].value
            second = self.board.Cells[x + move[0]][y + move[1]].value
            cell0  = self.board.Cells[x][y]
            cell1 = self.board.Cells[x + move[0]][y + move[1]]
            print(f'My domino [{cell0.value} | {cell1.value}]')
            path.append([cell0, cell1])
            self.board.numbersexist[first][second] = self.board.numbersexist[second][first] = True
            self.board.visited[x + move[0]][y + move[1]] = True
            if len(path) == (self.size + 2)*(self.size + 1):
                return True
            result =  self.DFS(board, path, x + 1, y)
            if result:
                return result   
            self.board.numbersexist[first][second] = self.board.numbersexist[second][first] = False
            self.board.visited[x][y] = False
            self.board.visited[x + move[0]][y + move[1]] = False
            path.pop()
        return False
P = CreateTest(3)
print(P.values)