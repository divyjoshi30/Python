lst=list(range(2, 10))    #addding numbers till range in list
print(lst)             #printing the list

even=list(range(0, 10, 2))
print("Prints even number",even)
odd=list(range(1, 10, 2))
print("Prints odd numbers",odd)
my_string="abcdefghijklmnopqrstuvwxyz"
print(my_string.index("e"))             #indexing starts with 0
print(my_string[4])                     #return element at the given index

small_decimels=range(0, 10)
print(small_decimels)           #prints range 010
print(small_decimels[4])        #prints value at index written in sq brackets

odd=range(1, 100, 2)
print(odd)
print(odd[20])  #prints the number that is odd and at index 20

for i in range(5):
    print(1, 2, 3, 4)  #if i run this they will b separated by space and not by commas.
    '''whatever the value is given in sep will be used to separate the elements, space allocation is done as
       same as in sep, if end is used with space, there won't be an separation in line'''
    print(1, 2, 3, 4, sep=';', end=' ')
