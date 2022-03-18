from tkinter import *
from generation import Board
from solveHan import *
from solveHung import *
from drawdomino import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = Solve(cas = cas, n  = 3)
solv.board.pre()
drawdomino(cas, solv.board.Cells[0][1], solv.board.Cells[0][0])
print(solv.board.Cells[0][1])
cas.pack()
# solv.solve()
tk.mainloop()