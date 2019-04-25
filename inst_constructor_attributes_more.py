print("---------------INSTANCES, CONSTRUCTOR AND MORE HERE---------------")
'''for complete understanding pls first refer oop_&_classes'''

class Kettle:
    def __init__(self, make, price):
        self.make=make
        self.price=price
        self.on=False

    def switch_on(self):
        self.on=True

kenwood = Kettle("Kenwood", 8.99)
kenwood.price=96.55
hamilton = Kettle("Hamilton", 22.55)
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

'''string formatting makes it easier this way to locate & print'''

'''
    Summarize :-
    class: Template for creating obj, All objs createed using same class will have same characteristics.
    Object: An instance of a class.
    Instantiate: create an instance of a class.
    Attribute: A variable bound to an instance of a class.
    Method: A function defined in a class.
'''
print(hamilton.on)
'''Returns true if instance is set to true on else false'''
hamilton.switch_on()   #instance set to true
print(hamilton.on)

'''we can the instance by this code also given below'''

Kettle.switch_on(kenwood)
print(kenwood.on)    #it will also return true because we have the class definition here you -
                     # - can see the def part for better uderstanding.

kenwood.power = 1.5
print(kenwood.power)

'''It is added to the Kettle class from here. We are able to do this because python classes are dynamic and can 
   be modified after their creation,power here is the attribute.'''
# print(hamilton.power)  if we run this it returns error as there is no attribute called power in hamilton instance

'''-------------------CLASS ATTRIBUTES-------------------'''
print("-" *50)
print("class attributes up next.....")