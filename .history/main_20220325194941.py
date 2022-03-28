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
snapshot1 = tracemalloc.take_snapshot()
solv.solve()
snapshot2 = tracemalloc.take_snapshot()
tracemalloc.stop()
tk.mainloop()
for stat in snapshot2.compare_to(snapshot1, 'lineno'):
    print(stat)