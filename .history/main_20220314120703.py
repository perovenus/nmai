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
drawdomino(cas, solv.board.Cells[3][3], solv.board.Cells[3][4])
#tren xuong duoi
drawdomino(cas, solv.board.Cells[3][3], solv.board.Cells[3][4])
#duoi len tren
cas.pack()
# solv.solve()
tk.mainloop()