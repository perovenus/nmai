from tkinter import *
from generation import Board
from solveHan import *
from solveHung import *
from drawdomino im 
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = Solve(cas = cas, n  = 3)
solv.solve()
cas.pack()
tk.mainloop()