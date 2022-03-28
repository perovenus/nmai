from tkinter import *
from generation import Board
from drawdomino import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
t = Board(cas, 3)
t.drawboard()

cas.pack()
tk.mainloop()