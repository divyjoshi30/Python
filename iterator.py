string="1234567890"
'''for char in string:
    print(char)'''

'''my_iterator=iter(string)
print(my_iterator)        #Prints object location
print(next(my_iterator))'''  # write no of times we want to iter and want the output. for loop performs well than this function

'''for char in iter(string):   #does the same like precious for loop just used iter function
    print(char)'''

lst=["abc", "acf", "gg"]
my_iteratotr=iter(lst)
for i in range(0, len(lst)):    #using range and len function
    next_item= next(my_iteratotr)   #create my iterator
    print(next_item)            #print created iterator

for i in lst:
    print(i)
