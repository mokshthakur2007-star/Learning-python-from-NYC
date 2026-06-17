# Exception Handling

# some errors that are unfixable.
# these are syntax errors, logical errors and runtime errors

# while other errors are fixable and we can handle them using exception handling.
# these are ZeroDivisionError, IndexError, KeyError, FileNotFoundError, ValueError etc

# Example

# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))

# try:
#     print(a/b)
# except Exception as err:
#     print(f"sorry you have encountered '{err}' error")
# else:
#     print("division is successful")
# finally:
#     print("this will always execute, no matter what!")
# raise Exception("This is a custom error message") 

# name = input("Enter your name : ")
# print(f"your name is {name}")

age = int(input("Enter your age : "))

if age < 18:
    raise Exception("Sorry you are not eligible to vote")

print (f"your age is {age}")