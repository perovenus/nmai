from tkinter import *
from generation import Board
from solveHan import *
from solveHung import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = Solve
cas.pack()
tk.mainloop()