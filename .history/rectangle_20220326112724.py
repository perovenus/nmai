from tkinter import *
from generation import Board
from drawdomino import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
t = Board(cas, 3)
t.drawboard()
cell0 =  t.Cells[0][0]
cell1 =  t.Cells[0][1]
drawdomino(cas, cell0, cell1)
cell0 =  t.Cells[0][2]
cell1 =  t.Cells[1][2]
cas.pack()
tk.mainloop()