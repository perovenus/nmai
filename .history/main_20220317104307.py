from tkinter import *
from generation import Board
from drawdomino import *
from HillClimbing import *
from sol
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = HillClimbing(cas = cas, n  = 3)
solv.board.pre()
cas.pack()
solv.solve()
tk.mainloop()