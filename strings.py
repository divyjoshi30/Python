#Strings Formatting and prcessing
'''parrot="Norwegian Blue"
print(parrot)
print(parrot[3])    #starts counting from the front and begins with 0.
print(parrot[-1])   #starts counting from backwards and starts with 1.
print(parrot[0:6])  #here 0 is the initial point from where to start and 6 is the total count of the numbers to be counted from the string.
print(parrot[:6])   #start value is not defined so it is taken by default as 0. line 6 and 7 are the same.
print(parrot[6:])   #if stop value is not given it goes till the end if the string.
print(parrot[-4:-2]) #stats from -4 and counts 2 from there
print(parrot[:6:2])  #counts upto 6 characters from the beinning and prints every alternate character. Values can be changed as per need.

#to extract informatio
number="9,22,63,85"
print(number[1::4])  #prints every 5th character.
numbers="0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])  #prints every 3rd character leaves a gap of 2 characters

#string concatenation
string1="Hello "
string2="DIVY!"
print(string1+string2)
print("Hello " "DIVY" "!")  #concatenates the strings just like line21.
print("Hello "*5)  #print sstring n times the number given.
print("Hello "*(5+4))  #prints hello 5 times in line 1 and total sum times sum line 2.
print("Divy "*3 +"96") #prints string n times and adds number at the end of the string.
today="saturday"
print("day" in today)                #returns boolean function
print("hur" in today)
print("atu" in today)'''

#String Formatting
'''age=20
print("My age is "+str(age)+" years")
print("My age is {0} Years".format(age))    #0 indicates it is an integer & format.age helps to print it by finding the appropriate location.
print("There are {0} days in {1}, {2}, {3}, {4}, {5}.".format(31, "January", "March", "May", "July", "August"))  #nos in curly brackets indicate the position of the element to be placed in.
print("My age is %d years"%age)   #%d replaces the digit by %age
print("my age is %d %s, %d %s"%(age, "Years" ,1, "Month"))'''     #%d for digits and %s for strings

'''for i in range(1, 12):
    print("No. %2d Squared is %4d and Cubed is %4d"%(i, i**2, i**3))'''   #here %2d allocates 2 spaces & 4d allocates 4 spaces to string
#print("Pi is approximately %5f"%(22/7))

#print("Value of pi is approximately %5.50f"%(22/7))  #number after decimal places denote the range to which decimal places can go upto.
'''for i in range(1, 12):
    print("No {0:2} Squared is {1:4} and Cubed is {2:4}".format(i, i**2, i**3))'''  #first nu in {} shows location to format tag and second nu indicates space

'''for i in range(1, 12):
    print("No {0:2} Squared is {1:<4} and Cubed is {2:<4}".format(i, i**2, i**3))'''

print("Pi value is {0:<12.10} approximately".format(22/7))
