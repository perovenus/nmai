from tkinter import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
for i in range(5):
    x0 = i * 60
    x1 = i * 60 + 60
    for j in range(5):
        y0 = j * 60
        y1 = j * 60 + 60
        cas.create_rectangle(x0, y0, x1, y1)
    cas.create_rectangle(65, 65, 115, 115)
cas.pack()
tk.mainloop()