from tkinter import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
for i in range(5):
    x0 = i * 50
    x1 = i * 50 + 50
    for j in range(5):
        y0 = j * 50
        y1 = j * 50 + 50
        cas.create_rectangle(x0, y0, x1, y1)
cas.pack()
tk.mainloop()