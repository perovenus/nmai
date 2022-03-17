from tkinter import *

import time

root = Tk()

class Clock:
    def __init__(self):
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')
        self.mFrame = Frame()
        self.mFrame.pack(side=TOP,expand=YES,fill=X)
        self.watch = Label (self.mFrame, text=self.time2, font=('times',12,'bold'))
        self.watch.pack()
        self.watch.after(200,self.time2)

obj1 = Clock()
root.mainloop()