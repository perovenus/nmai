def drawdomino(cas, x0, y0, x1, y1):
    if x0 == x1 - 60:
        #draw hor domino
        cas.create_rectangle(x0 + 5, 65, 175, 115)
    else:
        #draw vertical domino
        cas.create_rectangle(65, 65, 175, 115)