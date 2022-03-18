from random import randrange
from matplotlib.pyplot import fill


def drawdomino(cas,cell0,cell1):
    if cell0.x0 < cell1.x0:
        #draw horizontal domino
        cas.create_rectangle(cell0.x0 + 5, cell0.y0 + 5, cell1.x0 + 55, cell1.y0 + 55,fill="grey40")
    else:
        #draw vertical domino
        cas.create_rectangle(cell1.x0 + 5, cell0.y0 + 5, cell1.x0 + 55, cell1.y0 + 55, fill="grey40")
    cas.create_text(cell0.x0 + 30, cell0.y0 + 30, text = cell0.value)
    cas.create_text(cell1.x0 + 30, cell1.y0 + 30, text = cell1.value)