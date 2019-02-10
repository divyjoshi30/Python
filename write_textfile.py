print("Writing Text Files Mode Initiliazed")
print("-"*50)
cities = ["vapi", "Surat", "Rajkot", "Ahmedabad"]
'''w makes sure that user is in write mode.
   it automatically creates file if not found else overwrites it'''
with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_write_file_test.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_write_file_test.txt", 'r') as city_file:
    for city in cities: #if end is used here it removes space b/w 2 strings , so we won't use it & it will print
        print(city)     #each name on the next line

cities=[]
with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_write_file_test.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip("\n"))    #it will cut out \n from the output.
'''Instead of using end we can use strip to remove it at the time of importing.'''
print(cities)
for city in cities:
    print(city)
print("Adelaide".strip('del'))  #it cuts out the character at the beginning or at the end, not from the middle.

imelda = "More Mayhem",  "Imelda May", "2011" (
    (1, "Pulling the rug"), (2, "psycho"), (3, "Year "), (4, "Kentish town")
)

with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_write_file1_test.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file )

'''APPENDING to FILE
   instesd of r or w we can use a to append data to a file'''
print("Appending to a file....")
with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_write_file1_test.txt", 'a') as tables:
    for i in range(2, 13):
        for j in range(2, 13):
            print("{0} times {1} is {2}".format(i, j, i*j), file=tables)
        print("-"*40, file=tables)