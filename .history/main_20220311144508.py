from tkinter import *
from drawdomino import *
from generation import Board
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
board = Board(cas, 5)
board.drawboard()
drawdomino(cas, board.Cells[0], board.Cells[3])
cas.pack()
tk.mainloop()