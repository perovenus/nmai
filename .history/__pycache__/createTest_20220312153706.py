class CreateTest:
    def __init__(self, n) -> None:
        self.x = 0
        self. y = 0
        self.board = []
        self.size = n
    def createTest(self):
    def isLegal(self, check_board, x0, x1):
        if  check_board[x0][x1] :
            return False
        return True
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
                if self.board.visited[x_next][y_next] == False:
                    first = self.board.Cells[x][y].value
                    second = self.board.Cells[x_next][y_next].value
                    if self.board.numbersexist[first][second] == False:
                        Edges.append(move)
        return Edges
