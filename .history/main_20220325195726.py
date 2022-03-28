from tkinter import *
from generation import Board
from drawdomino import *
from HillClimbing import *
from solveHung import *
from time import *
import tracemalloc
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = HillClimbing(cas = cas, n  = 3) 
cas.pack()
time_start = time()  # tính thời gian chạy, bắt đầu từ đây
tracemalloc.start()
solv.solve()
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop() 
time_end = time.time()
print("Run time: " + str(time_end - time_start))

tk.mainloop()
