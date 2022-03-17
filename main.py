from tkinter import *
from generation import Board
# from solveHan import *
from solveHung import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solution = SolveHung(cas, 3).solve((0,0))
cas.pack()
tk.mainloop()