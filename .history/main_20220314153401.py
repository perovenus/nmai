from tkinter import *
from generation import Board
from solveHan import *
from solveHung import *
from drawdomino import *
from HillClimbing import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = HillClimbing(cas = cas, n  = 3)
solv.board.pre()
cas.pack()
solv.solve()
tk.mainloop()