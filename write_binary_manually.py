print("Writing Binary files manually.")
#Write binary files.
with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/binary", 'bw') as bin_files:
    for i in range(17):
        bin_files.write(bytes(range(17)))
#read binary file.
with open("C:/Users/Divy Joshi/Desktop/Stuff/Python/binary", 'br') as binFile:
    for b in binFile:
        print(b)
