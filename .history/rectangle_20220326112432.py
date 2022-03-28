from tkinter import *
from generation import Board
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
t = Board(cas, 3)
t.drawboard()
cell0 =  self.board.Cells[pos[0]][pos[1]]
cas.pack()
tk.mainloop()