from cv2 import BORDER_DEFAULT, borderInterpolate
from matplotlib.pyplot import fill


def drawdomino(cas,cell0,cell1):
    if cell0.x0 == cell1.x0 - 60:
        #draw hor domino
        cas.create_rectangle(cell0.x0 + 5, cell0.y0 + 5, cell1.x0 + 55, cell1.y0 + 55,fill="grey40")
        self.canvas.create_text(cell.x0 + 30, cell.y0 + 30, text = cell.value)
    else:
        #draw vertical domino
        cas.create_rectangle(cell0.x0 + 5, cell0.y0 + 5, cell1.x0 + 55, cell1.y0, fill="grey40")