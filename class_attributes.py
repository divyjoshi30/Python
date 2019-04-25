print("Class Attrbbutes begins from here...")
print("-"*50)
print()

class Kettle:
    power_source="electricity"
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
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.power = 1.5
print(kenwood.power)
print(Kettle.power_source)    #returns the value of power_source instance inside the Kettle class
print(kenwood.power_source)     #same applies for them too.
print(hamilton.power_source)  #similar to static fiel in objOriented language like java or c++.
print(Kettle.__dict__)   #Shows every details about it.
print(kenwood.__dict__)
print(hamilton.__dict__)

print("Switch to atomic power")
Kettle.power_source="Atmoic Power"   #once the value is updated somewhere else, it overwrites its previous data.
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("Switch kenwood to gas")
kenwood.power_source="gas"    #any specific instance can be updatede from anywhere.
print(kenwood.power_source)

print("{} Methods Implementation in next file {}".format("="*20,"="*20 ))
