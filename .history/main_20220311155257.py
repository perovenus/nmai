from tkinter import *
from generation import Board
from solvHan import *
from solve
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
board = Board(cas, 3) # 3 là số lớn nhất trên bàn cờ
board.drawboard()
solve(board)
cas.pack()
tk.mainloop()