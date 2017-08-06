'''
Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes
have your program print the number of that iteration and specify whether it's an odd or even number.
'''

# def odd_even():
#     for val in range(1,2001,1): ##the step in unnecessary, 1 is default. I just wanted practice typing the step
#         if val % 2 == 0:
#             print val, 'Even number'
#         else:
#             print val, 'Odd number'

# odd_even()

'''
Multiply:
Create a function called 'multiply' that iterates through each value in a list
(e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
The function should multiply each value in the list by the second argument.
'''

def multiply(arr, num):
    newList = list()
    for x in range(len(arr)):
        newList.append(arr[x]*num)
    return newList
a = [5, 10, 15, 20, 25]
b = multiply(a,5)
print b

'''
Hacker Challenge:
Write a function that takes the multiply function call as an argument. Your new function should
return the multiplied list as a two-dimensional list. Each internal list should contain the 1's
times the number in the original list.
'''
def layered_multiples(arr):   
    newList = list()  #newList will be the master list
    for i in range(0, len(arr)): #loop to determine how many inner lists
        innerList = list() #innerList are the lists within newList
        for x in range(0, arr[i]): #loop to determine how many 1's are in each list
            innerList.append(1) #append 1's to list
        newList.append(innerList) #append innerList to newList
    print newList
layered_multiples(multiply([1, 2, 3], 3)) #provides arguements for layered_multiples function
