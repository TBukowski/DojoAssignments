'''
FIND AND REPLACE
words = "It's Thanksgiving day, It's my birthday too!"
print words.replace('day', 'month', 1)
MIN AND MAX
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print min(x)
print max(x)
FIRST AND LAST
x = ["hello",2,54,-2,7,12,98,"world"]
y = [x[0], x[len(x)-1]]
print y
NEW LIST
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = x[:5]
x[0] = y
print x
'''
#answer for New list copied from Solutions
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero
second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list