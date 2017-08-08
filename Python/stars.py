def draw_stars(myList):
    for val in myList:
        if isinstance(val, int):
            print '*' * val
        elif isinstance(val, str):
            print val[:1] * len(val)
        else:
            print 'No bueno, be well John Spartan'

draw_stars(['ni', 4, 10, 4, [1, 2, 3]])
