from tkinter import *
from generation import Board
from drawdomino import *
from HillClimbing import *
from solveHung import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = SolveHung(cas = cas, n  = 3)
solv.solve(0)
cas.pack()
solv.solve()
tk.mainloop()