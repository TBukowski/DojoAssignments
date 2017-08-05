def typelist(yourList):
    words = ''
    total = 0

    for value in yourList:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            words += (' ' + value)

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
