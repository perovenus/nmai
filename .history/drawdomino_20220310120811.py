def drawdomino(cas, x0, y0, x1, y1):
    if x0 == x1 - 60:
        #draw hor domino
        cas.create_rectangle(x0 + 5, y0 + 5, x1 + 55, y1 - 5)
    else:
        #draw vertical domino
        cas.create_rectangle(x0 + 5, y0 + 5, x1 + 65, y1 - 5)