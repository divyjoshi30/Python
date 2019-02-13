#Order always keeps on changing
'''
animal={"cow", "sheep", "hen"}
print(animal)  #prints the dictionary
for a in animal:   #print each item in different line.
    print(a)
print("-"*40)

wild_animal=set({"lion", "tiger","panther", "elephant"})
print(wild_animal)

animal.add("horse")
wild_animal.add("horse")
print(animal)
print(wild_animal)'''

'''empty_set=set()    #to create an empty set you need to declare an empty set else it will raise an error.
empty_set_2={}      #attribute error
empty_set.add("a")
#empty_set_2.add("a")  #cannot add item to an empty set
print(empty_set)
#print(empty_set_2)'''

'''even= set(range(0, 20, 2))
print(even)

squares_tuple=(2, 4, 9, 16, 25)   #can convert tuples to a set
squares=set(squares_tuple)
print(squares)'''

even= set(range(0, 20, 2))
print(even)

squares_tuple=(2, 4, 9, 16, 25)   #can convert tuples to a set
squares=set(squares_tuple)
print(squares)
'''to add item to a set user need to use union function like this
    first var is where you have to add items and the 2nd is from where it is imported
    even length can be counted by using union unction.
    sets are not reversible'''
'''
print(set(even.union(squares)))
print(len(even.union(squares)))
print(set(squares.union(even)))    # they are by default sorted is ascending order.

print(even.intersection(squares))  # will find the common term in both of them & comes in the order they intersect.
print(even & squares)   #does the same as the intersect.
print(squares & even)    #doesn't matter which is called first.

squares_tuple_1={2, 5, 6, 22, 1, 0}
print(sorted(squares_tuple_1))    #prints sorted sets in ascending order.

print("Even minus squares")
print(even.difference(squares))    #shows the difference in them
print(even - squares)    #same as differncce function.

print("-"*40)
print(sorted(even))
even.difference_update(squares)   #this will update the set with removing the difference and save it.
print(sorted(even))   '''

even=set(range(0, 40, 2))
print(sorted(even))
squares_tuple={4, 9, 16, 25, 36}
print(squares_tuple)

print("Symmetric Difference")
print("Symmetric even minus squares_tuples.")
print(even.symmetric_difference(squares_tuple))  #used to find the symmetric difference
even.symmetric_difference_update(squares_tuple)  #updates the set without printing it.
print(sorted(even))                              #updated set is printed here when needed.

print("For symmetric difference in sqyuares_tuples minus even")
squares_tuple.symmetric_difference_update(even)
print(sorted(squares_tuple))                      #prints the symmetric difference in squares_tuples and even
print(squares_tuple.symmetric_difference(even))
