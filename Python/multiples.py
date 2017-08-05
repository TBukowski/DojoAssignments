'''
Assignment: Multiples, Sum, Average
This assignment has several parts. All of your code should be in one file that is well commented to
indicate what each block of code is doing and which problem you are solving.
Don't forget to test your code as you go!

Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop
and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
'''
#Multiples Part I
def multiple1():
    for i in range(1, 1001):
        if i % 2 == 1: #Modulo 2 == 1 gives all odd numbers
            print i
multiple1()
#Miltiples Part II
def multiple5():
    for i in range(5, 1000001):
        if i % 5 == 0: #Modulo 5 == 0 ensures a number is divisble by 5
            print i
multiple5()
#=================================
a = [1, 2, 5, 10, 255, 3]
#Sum list
print sum(a)
#Average List
print sum(a)/len(a)