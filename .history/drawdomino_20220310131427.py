from cv2 import BORDER_DEFAULT, borderInterpolate
from matplotlib.pyplot import fill


def drawdomino(cas,cell0,cell1):
    if cellx0 == x1 - 60:
        #draw hor domino
        cas.create_rectangle(cell0.x0 + 5, cell0.y0 + 5, cell1.x0 + 55, cell1.y0 + 55,fill="grey40")
    else:
        #draw vertical domino
        cas.create_rectangle(cell0.x0 + 5, cell0.y0 + 5, cell1.x0 + 55, cell1.y0, fill="grey40")