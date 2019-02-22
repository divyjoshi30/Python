'''ip=input("Enter ip")     #Using count function
print(ip.count("."))'''

#append function
'''
parrot_list=["A stiff","Good","no pinin"]
parrot_list.append("A novereign blue")
for state in parrot_list:
    print("The parrot is "+state)  '''

#list concatenation & sort function
'''
even=[2,4,6,8]
odd=[1,3,5,7]
numbers=odd + even
print(numbers)
numbers.sort()  #to print numbers in sorted in sorted order
print(numbers)

no_in_sorted=sorted(numbers)
print(no_in_sorted)

if numbers==no_in_sorted:     #lists can be compared directly
    print("Lists are equal")
else:
    print("Lists are not equal")

if no_in_sorted==sorted(numbers):  #comparing lists
    print("Lists are equal")
else:
    print("Lists are not equal")  '''

#create an empty list
'''
list_1=[]
list_2=list()
print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1==list_2:
    print("Both lists are the same")
else:
    print("They are different")
print(list("This is a list"))'''

#reversing a list
'''even=[2,4,6,8]
another_even=sorted(even, reverse=True)  #if even written in list constructor is cretes another list which in returns ans as false
#another_even.sort(reverse=True)
print(another_even)
print(another_even == even)'''   # is and == work as same

#list conataining list
odd=[1,3,5,7,9]
even=[2,4,6,8]
numbers=[odd,even]
print(numbers)
for number_in_set in numbers:
    print(number_in_set)

for value in number_in_set:
    print(value)
