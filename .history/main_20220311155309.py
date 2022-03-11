from tkinter import *
from generation import Board
from solvHan import *
from solve import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solve(board)
cas.pack()
tk.mainloop()