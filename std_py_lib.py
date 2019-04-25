# print(dir())
# #print(dir(__builtins__))
# for m in dir(__builtins__):
#     print(m)        #prints all the builtin modules in a list format.
print("Using Standard Python library")

import shelve
# print(dir())  #prints all the functions
# print()
# print(dir(shelve))       #prits all the functions of the shelves.

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)
help(shelve)    #gives detailed information about shelves & also the link to its documentation.

import random
help(random.randint)   #gives info about a specific function also
