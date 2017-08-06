# for num in range(0,5):
#     print num

# for idx in [3,2,1]:
#     print idx

# myDictionary = {
#     'name':'Todd',
#     'location':'Warshington'
# }
# for key in myDictionary:
#     print key

# for num1 in range(0,5):
#     for num2 in range(6,10):
#         print num1, ':', num2

# def printXTimes(your_number): #your_number is a parameter, 100 is an argument
#     for num in range(1,your_number):
#         print num

# print printXTimes(100)

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.iteritems():
     print key, " = ", data
