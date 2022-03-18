from tkinter import *
from generation import Board
from drawdomino import *
from HillClimbing import *
from solveHung import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)

solv = SolveHung(cas = cas, n  = 3)
# sb = Scrollbar(tk)  
# sb.pack(side = RIGHT, fill = Y)  
  
# mylist = Listbox(tk, yscrollcommand = sb.set ) 
# for line in range(30):  
#     mylist.insert(END, "Number " + str(line))  
  
# mylist.pack( side = RIGHT )  
# sb.config( command = mylist.yview )  
cas.pack()
solv.solve((0,1))
tk.mainloop()