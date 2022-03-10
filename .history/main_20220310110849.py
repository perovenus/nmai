from tkinter import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
for i in range(5):
    x0 = i * 10
    x1 = i * 10 + 10
    for j in range(5):
        x0 = i * 10
        x1 = i * 10 + 10
        cas.create_rectangle()
cas.pack()
tk.mainloop()