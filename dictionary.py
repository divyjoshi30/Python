print("Dictionaries Starting")
'''Dictionaries can hold all sort of data like string, integer, tuples, list etc.
    A dictionary always prints same type functions first and then the other.
'''

fruit={"orange":"A sweet citrus fruit",
       "apple":"Sweet red fruit which contains almost all vitamins",
        "lemon":"Sour, yellow citus fruit"}
'''print(fruit)     #prints the dictionary
print(fruit["apple"])  #prints the details of the specified object.
bike={"name":"CBR 250", "engine_size":250, "maker":"Honda"}
print(bike["name"])
print(bike["engine_size"])

fruit["pear"]="An odd shped apple"   #can append dict from anywhere by just adding content.
print(fruit["pear"])    #can call a specified object anytime.
del fruit["lemon"]       #to delete a specific enrtry.   
print(fruit)
#del fruit   #To delelte complete dictionary
#fruit.clear()  #to cleareverything from the dictionary leaving it empty.
print(fruit["tomato"])   #if not in directoey returrns key-error.
print(fruit[2])'''

'''Following code will not stop until quit string is not inserted, 
    it takes the name of fruit as input and returns is corresponding value as output'''

'''while True:
    dict_key=input("Enter fruit ")
    if dict_key == "quit" or dict_key == "exit":
        break
    elif dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have any fruit called "+dict_key)'''
for f in fruit:
    print(fruit[f])

for i in range(10):
    for f in fruit:
        print(f + " is " + fruit[f])
    print("-"*40)

ordered_keys = list(fruit.keys())
#ordered_keys.sort()  #sort function will sort the items in the list.
#ordered_keys= sorted(list(fruit.keys()))   #sorted does the same like sort function just implemented differently.
'''for f in ordered_keys:
    print(f+ "-"+fruit[f])'''
for f in sorted(fruit.keys()):   #this can also be used to sort items in dictionary.
    print(f+ "-"+fruit[f])
for f in sorted(fruit.values()):   #only return values not the keys line by line in sorted manner.
    print(f)

for f in sorted(fruit.keys()):   #only return keys not the values line by line in sorted manner.
    print(f)