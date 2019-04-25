'''python can be used to write object oriented programming nad also be used to write impertive
    proogramming. It supports multiple programming paradigm. It also features a dynamic type system & functional
    programming with automatic memory management and large library support.'''

# print("----------Object Oriented Programming----------")
# a=10
# b=10
# print(a+b)
# print(a.__add__(b))  #both the sent give same reslt but we are importing n inbuilt add class to perform operation.
# '''if we click on __add__ it shos ots source code which makes it run'''

class Kettle:
    def __init__(self, make, price):
        self.make=make
        self.price=price
        self.on=False

kenwood = Kettle("Kenwood", 8.99) #from here we are assigning value to make and price
print(kenwood.make)    #prints the value of make
print(kenwood.price)   #prints the value of price

kenwood.price=96.55  #it will overwrite its data and write the new price
print(kenwood.price)

hamilton = Kettle("Hamilton", 22.55)
print(hamilton.make)
print(hamilton.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
#string formatting is used to reteive the values, parameters are given according to the number of {}

'''For more info about each function and its use you can refer its documentation from its official website.'''