from tkinter import *
from generation import Board
# from solveHan import *
from solveHung import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = SolveHung(cas, 7)
cas.pack()
solv.solve((4,2))
tk.mainloop()