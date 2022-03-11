from tkinter import *

from matplotlib.pyplot import text
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
for i in range(5):
    x0 = i * 60
    x1 = i * 60 + 60
    for j in range(5):
        y0 = j * 60
        y1 = j * 60 + 60
        cas.create_rectangle(x1, y0, x1, y1)
        cas.create_text(x0/2, y0/ 2, text  = i)
    cas.create_rectangle(65, 65, 175, 115)
    cas.create_rectangle(5, 5, 55, 115)
cas.pack()
tk.mainloop()