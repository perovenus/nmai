from tkinter import *
from drawdomino import *
from generation import Board
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
board = Board(cas, 3) # 3 là số lớn nhất trên bàn cờ
board.drawboard()
drawdomino(cas, board.Cells[0][0], board.Cells[1][1])
cas.pack()
tk.mainloop()