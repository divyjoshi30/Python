#Reading and writing text files

#READ FILES MODE
f=open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_io_file_test.txt",'r')   #to open file give its path location, r stands for read & always writeen in single quotes \ is interpreted as command so use / or \\.
for line in f:          #to print lines iteratively
    print(line)
f.close()                     #close file work is finished.
#if the file is in same folder as the py file than no need to specify the complete path
print("-"*40)
f=open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_io_file_test.txt",'r')
for line in f:
    if "write" in line.lower():             #it only prints line that contains the specified word
        print(line, end='')
f.close()

with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_io_file_test.txt",'r') as f:
    for line in f:                          #no need to close file when using with bcs it already takes cares of it.
        if "HELLO" in line.upper():         #used for upper case string.
            print(line, end='')             #end prevents from printing next unwanted line

with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_io_file_test.txt",'r') as f:
    line=f.readline()           #read each line in the file
    while line:
        print(line, end='')   #end will remove extra spaces between lines.
        line=f.readline()

with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_io_file_test.txt",'r') as f:
    lines=f.readlines()           #read each lines in the file but will be converted to list when printed.
print(lines)                      #each line will printed as a part of list as different string.

'''Next(below) statement will print line as they were in the original file no in list form
    or we can say they will b gain converted to normal form instead of list view, much better.
    it reads \n as next line and gives the result.'''
for line in lines:
    print(line, end='')

with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_io_file_test.txt",'r') as f:
    lines=f.readlines()
print(lines)

for line in lines[::-1]:      # to print the lines in reverse(vertically)
    print(line, end='')

with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/python_io_file_test.txt",'r') as f:
    lines=f.read()
print(lines)

for line in lines[::-1]:      # to print the lines in reverse(horizontally as well vertically).
    print(line, end='')
print("reading text files done")