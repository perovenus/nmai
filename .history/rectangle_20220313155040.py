from tkinter import *
tk = Tk()
cas = Canvas(tk , width=100, height= 100)
for i in range(0, 100, 5):
    cas.create_rectangle(i,i,i,i)
cas.pack()
tk.mainloop()