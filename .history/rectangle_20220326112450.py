from tkinter import *
from generation import Board
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
t = Board(cas, 3)
t.drawboard()
cell0 =  t.board.Cells[0][0]

cas.pack()
tk.mainloop()