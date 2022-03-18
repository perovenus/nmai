from tkinter import *
from generation import Board
from solveHan import *
from solveHung import *
from drawdomino import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = Solve(cas = cas, n  = 3)
solv.board.pre()
#trai sang phai
drawdomino(cas, solv.board.Cells[0][1], solv.board.Cells[0][0])
#phai sang trai
drawdomino(cas, solv.board.Cells[3][3], solv.board.Cells[0][0])
print(solv.board.Cells[0][1].x0, solv.board.Cells[0][1].y0)
print(solv.board.Cells[0][0].x0, solv.board.Cells[0][0].y0)
cas.pack()
# solv.solve()
tk.mainloop()