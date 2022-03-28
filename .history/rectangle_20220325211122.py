from tkinter import *
from generation import Board
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
t = Board(cas, 3)
t.drawboard()
tk.mainloop()