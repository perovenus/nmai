from tkinter import *
from generation import Board
from drawdomino import *
from HillClimbing import *
from solveHung import *
from time import *
import tracemalloc
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = HillClimbing(cas = cas, n  = 3) 
cas.pack()
tracemalloc.start()



tk.mainloop()
