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
tracemalloc.start()

solv.solve()

tk.mainloop()
for stat in snapshot2.compare_to(snapshot1, 'lineno'):
    print(stat)
tracemalloc.stop()
time_start = time.time()  # tính thời gian chạy, bắt đầu từ đây
tracemalloc.start()
solv.solve()
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop() 
time_end = time.time()
print("Run time: " + str(time_end - time_start))