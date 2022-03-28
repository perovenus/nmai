from tkinter import *
from generation import Board
from drawdomino import *
from HillClimbing import *
from solveHung import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = HillClimbing(cas = cas, n  = 3) 
cas.pack()
import tracemalloc
tracemalloc.start()
solv.solve()

tk.mainloop()