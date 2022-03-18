from tkinter import *
from generation import Board
from drawdomino import *
from HillClimbing import *
from solveHung import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = SolveHung(cas = cas, n  = 3)
sb = Scrollbar(tk)  
sb.pack(side = RIGHT, fill = Y)  
  
mylist = Listbox(tk, yscrollcommand = sb.set )  
cas.pack()
solv.solve((0,1))
tk.mainloop()