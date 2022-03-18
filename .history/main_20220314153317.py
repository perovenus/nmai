from tkinter import *
from generation import Board
from solveHan import *
from solveHung import *
from drawdomino import *
from HillClimbing import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = H(cas = cas, n  = 3)
solv.board.pre()
# #trai sang phai
# drawdomino(cas, solv.board.Cells[0][1], solv.board.Cells[0][0])
# #phai sang trai
# drawdomino(cas, solv.board.Cells[3][3], solv.board.Cells[3][4])
# #tren xuong duoi
# drawdomino(cas, solv.board.Cells[2][0], solv.board.Cells[3][0])
# #duoi len tren
# drawdomino(cas, solv.board.Cells[1][4], solv.board.Cells[0][4])
cas.pack()
solv.solve()
tk.mainloop()