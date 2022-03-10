from cv2 import BORDER_DEFAULT, borderInterpolate
from matplotlib.pyplot import fill


def drawdomino(cas,cell0,cell1):
    if x0 == x1 - 60:
        #draw hor domino
        cas.create_rectangle(x0 + 5, y0 + 5, x1 + 55, y1 + 55,fill="grey40")
    else:
        #draw vertical domino
        cas.create_rectangle(x0 + 5, y0 + 5, x1 + 55, y1 + 55, fill="grey40")