from tkinter import *
from generation import Board
from drawdomino import *
from HillClimbing import *
from solveHung import *
from time import *
tk = Tk()
cas = Canvas(tk, height = 600, width= 800)
solv = HillClimbing(cas = cas, n  = 3) 
cas.pack()
import tracemalloc
tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()
solv.solve()
snapshot2 = tracemalloc.take_snapshot()
tk.mainloop()
for stat in snapshot2.compare_to(snapshot1, 'lineno'):
    print(stat)
tracemalloc.stop()
time_start = time.time()  # tính thời gian chạy, bắt đầu từ đây
tracemalloc.start()

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop() 
time_end = time.time()
print("Run time: " + str(time_end - time_start))