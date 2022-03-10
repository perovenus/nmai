from tkinter import *
from drawdomino import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)

drawdomino(cas, 60, 60, 120, 60)
    drawdomino(cas, 0, 0, 0, 60)
cas.pack()
tk.mainloop()