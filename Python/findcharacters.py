'''
Write a program that takes a list of strings and a string containing a single character,
and prints a new list of all the strings containing that character.
Hint: how many loops will you need to complete this task?
'''
# input
word_list = ['killer', 'rabbit', 'black', 'knight', 'King', 'Arthur']
char = 'k' #case sensitive
# output
new_list = []

for val in word_list:
    if char in val:
        new_list += [val]

print new_list