from tkinter import *
from drawdomino import *
from GE
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
board = Bo
drawdomino(cas, 60, 60, 120, 60)
drawdomino(cas, 0, 0, 0, 60)
cas.pack()
tk.mainloop()