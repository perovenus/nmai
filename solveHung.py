from genericpath import exists
from mimetypes import init
from tracemalloc import start
from turtle import position
from generation import *
from drawdomino import *
from random import *

class SolveHung:
    def __init__(self, cas, n) -> None:
        self.canvas = cas
        self.size = n
        self.board = Board(cas, n)
        self.board.drawboard()
        self.possiblePositions = self.getPossiblePositions()
        self.listOfDomino = []

    def solve(self, init_position):
        print("Dfs value", self.Dfs(init_position))
        print("list of domino", self.listOfDomino)
        for domino in self.listOfDomino:
            drawdomino(self.canvas, self.board.Cells[domino[0][0]][domino[0][1]], self.board.Cells[domino[1][0]][domino[1][1]])

    def getPossiblePositions(self):
        legalPositions = []
        for i in range(len(self.board.visited)):
            for j in range(len(self.board.visited[i])):
                if self.board.visited[i][j] == False:
                    legalPositions.append((i,j))

        return legalPositions

    def getPossibleDominos(self, pos):
        positions = []
        possibleDominos = []

        positions.append((pos[0]-1,pos[1]))
        positions.append((pos[0]+1,pos[1]))
        positions.append((pos[0],pos[1]-1))
        positions.append((pos[0],pos[1]+1))
        
        for x in positions:
            if x[0] in range(self.size+1) and x[1] in range(self.size+2) and self.board.visited[x[0]][x[1]] == False:
                if self.board.dominosexist[self.board.Cells[pos[0]][pos[1]].value][self.board.Cells[x[0]][x[1]].value] == False:
                    possibleDominos.append(((pos[0],pos[1]),(x[0],x[1])))
        
        return possibleDominos

    def Dfs(self, cell1_pos):
        possibleDominos = self.getPossibleDominos(cell1_pos)
        print("Possible dominos: ", possibleDominos)
        
        # self.possiblePositions.remove(cell1_pos)
        if possibleDominos == []: return False
        shuffle(possibleDominos)
        
        while len(possibleDominos) > 0:
            domino = possibleDominos.pop()
            print("Domino: ", domino)
            self.placeDomino(domino)
            if self.possiblePositions == []:
                return True
            shuffle(self.possiblePositions)
            next_pos = self.possiblePositions[-1]
            if possibleDominos == []:
                if self.Dfs(next_pos) == False:
                    self.removeDomino(domino)
                    return False
                else: return True
            if self.Dfs(next_pos) == False:
                self.removeDomino(domino)
            else: return True

    def checkExistDomino(self):
        for pos in self.possiblePositions:
            if self.getPossibleDominos(pos) != []:
                return True
        return False

    def placeDomino(self, domino):
        print("Place domino: ", domino)
        print("Prev possible positions",self.possiblePositions)
        cell1_pos = domino[0]
        cell2_pos = domino[1]
        cell1_value = self.board.Cells[cell1_pos[0]][cell1_pos[1]].value
        cell2_value = self.board.Cells[cell2_pos[0]][cell2_pos[1]].value
        self.possiblePositions.remove(cell1_pos)
        self.possiblePositions.remove(cell2_pos)
        print("Current possible positions",self.possiblePositions)
        self.board.visited[cell1_pos[0]][cell1_pos[1]] = True
        self.board.visited[cell2_pos[0]][cell2_pos[1]] = True
        self.board.dominosexist[cell1_value][cell2_value] = True
        self.board.dominosexist[cell2_value][cell1_value] = True

        self.listOfDomino.append(domino)

    def removeDomino(self, domino):
        print("Remove domino: ", domino)
        print("Prev possible positions",self.possiblePositions)
        cell1_pos = domino[0]
        cell2_pos = domino[1]
        cell1_value = self.board.Cells[cell1_pos[0]][cell1_pos[1]].value
        cell2_value = self.board.Cells[cell2_pos[0]][cell2_pos[1]].value

        self.possiblePositions.append(cell1_pos)
        self.possiblePositions.append(cell2_pos)
        print("Current possible positions",self.possiblePositions)
        self.board.visited[cell1_pos[0]][cell1_pos[1]] = False
        self.board.visited[cell2_pos[0]][cell2_pos[1]] = False
        self.board.dominosexist[cell1_value][cell2_value] = False
        self.board.dominosexist[cell2_value][cell1_value] = False

        self.listOfDomino.remove(domino)





        
