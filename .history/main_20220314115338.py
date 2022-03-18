from tkinter import *
from generation import Board
from solveHan import *
from solveHung import *
from drawdomino import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = Solve(cas = cas, n  = 3)
drawdomino(cas, solv.board[1][])
cas.pack()
# solv.solve()
tk.mainloop()