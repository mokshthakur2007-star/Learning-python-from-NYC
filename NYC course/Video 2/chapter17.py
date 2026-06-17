# File handling in python

# file = open("file.txt", "w")
# file.write("This is a file handling example in python")
# file.close()

# with open("superman.txt", "w") as file:
#     file.write("This file contains super secret information about superman")

# with open("file.txt", "a") as file:
#     file.write("This is another file handling example in python")


file = open("newfile.txt", "w")

data = input("Enter some data to write in the file : ")
file.write(data)

new_data = input("Enter some data to append in the file : ")
with open("newfile.txt", "a") as file:
    file.write(new_data)

file = open("newfile.txt", "r")
print(file.read())