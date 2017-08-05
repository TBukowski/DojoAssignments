def typelist(yourList):
    words = ''
    total = 0

    for val in yourList:
        if isinstance(val, int) or isinstance(val, float):
            total += val
        elif isinstance(val, str):
            words += (' ' + val)

    if total and words:
        print 'this list has mixed types'
        print total
        print words
    elif words:
        print 'the list is a string'
        print words
    else:
        print 'the list is a number'
        print total


typelist(['I', 'see', 'a', 'poor', 'boy'])
typelist([1.2, 2.3, 7.5])
typelist([5, 4, 3, 2, 1, 'BOOM!'])
