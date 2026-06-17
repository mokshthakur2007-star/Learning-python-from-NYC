from pathlib import Path
import os

def createfile():
    try:
        name = input("Enter the name of the file to create : ")
        path = Path(name)
        if path.exists():
            print("File already exists")
        else:
            with open(path, "w") as file:
                data = input("Enter some data to write in the file : ")
                file.write(data)
            print("File created successfully")
    except Exception as err:
        print(f"sorry you have encountered '{err}' error")

def readfile():
    try:
        name = input("Enter the name of the file to read : ")
        path = Path(name)
        if not path.exists():
            print("File does not exist")
        else:
            with open(path, "r") as file:
                print(file.read())
    except Exception as err:
        print(f"sorry you have encountered '{err}' error")

def appendfile():
    try:
        name = input("Enter the name of the file to append to : ")
        path = Path(name)

        if not path.exists():
            print("File does not exist")
        else:
            print("Operations")
            print("1. Change name of the file")
            print("2. Append data to the file")
            print("3. Append data to the file with new line")
            print("4. Overwrite the file with new data")
            print("5. Exit")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                newname = input("Enter the new name of the file : ")
                newpath = Path(newname)
                if not newpath.exists():
                    path.rename(newpath)
                    print("File renamed successfully")
                else:
                    print("File with this name already exists")
            elif choice == 2:
                with open(path, "a") as file:
                    new_data = input("Enter some data to append in the file : ")
                    file.write(new_data)
                print("Data appended successfully")
            elif choice == 3:
                with open(path, "a") as file:
                    new_data = input("Enter some data to overwrite the file : ")
                    file.write("\n" + new_data)
                print("File appended successfully")
            elif choice == 4:
                with open(path, "w") as file:
                    new_data = input("Enter some data to overwrite the file : ")
                    file.write(new_data)
                print("File overwritten successfully")
            elif choice == 5:
                print("Exiting the program")
            else:
                print("Invalid choice")
    except Exception as err:
        print(f"sorry you have encountered '{err}' error")

def deletefile():
    try:
        name = input("Enter the name of the file to delete : ")
        path = Path(name)
        if not path.exists():
            print("File does not exist")
        else:
            path.unlink()
            print("File deleted successfully")
    except Exception as err:
        print(f"sorry you have encountered '{err}' error")

while True:
    print("File Handling Menu")
    print("\npress 1 for creating a file")
    print("press 2 for reading a file")
    print("press 3 for appending to a file")
    print("press 4 for deleting a file")
    print("press 5 for exiting the program")

    try:
        a = int(input("\nEnter your choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        break

    if a == 1:
        createfile()
    if a == 2:
        readfile()
    if a == 3:
        appendfile()
    if a == 4:
        deletefile()
    if a == 5:
        break
    elif a < 1 or a > 5:
        print("Invalid choice")

    choice = input("\nDo you want to continue (y/n) : ")
    if choice == "y":
        continue
    else:
        break