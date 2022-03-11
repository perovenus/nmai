from tkinter import *
from generation import Board
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
board = Board(cas, 3) # 3 là số lớn nhất trên bàn cờ
board.drawboard()
cas.pack()
tk.mainloop()