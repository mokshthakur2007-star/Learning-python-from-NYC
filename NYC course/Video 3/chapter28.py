# Decorators

# def extragreetings(func):
#     def wrapper():
#         print("Hello, i'm Moksh")
#         func()
#         print("Thank you, Visit again")
    
#     return wrapper

# @extragreetings
# def greetings():
#     print("Good Morning")

# greetings()

# Args -> these can take any number of positional arguments and save them as a tuple, Kargs -> these can take any number of keyword arguments and save them as a dictionary

# def addition(a, b):
#     return a + b

# print(addition(5, 3))  # This will work correctly
# print(addition(5, 3, 4))  # This will raise an error because addition only takes 2 positional arguments

# but we can accept any number of arguments using *args

# def addition(*args):
#     return sum(args)

# print(addition(5, 3))  # This will work correctly
# print(addition(5, 3, 4))  # This will now work correctly with *args

# #or

# def addition(*args):
#     t = 0
#     for num in args:
#         t = t + num
#     return t

# print(addition(52, 3234))  # This will work correctly
# print(addition(5234, 3234, 234,243,346,4754, 457,1346,13764,1))  # This will now work correctly

# kwargs

# def info(**kwargs):
#     return kwargs

# print(info(name='Moksh', age=20, city='Mumbai'))  # This will work correctly

# def extragreetings(func):
#     def wrapper(*args, **kwargs):
#         print("Hello, i'm Moksh")
#         func(*args, **kwargs)
#         print("Thank you, Visit again")
    
#     return wrapper


# @extragreetings
# def addition(*args):
#     print(f"sum of given numbers is {sum(args)}")

# @extragreetings
# def subtraction(*args):
#     print(f"subtraction of given numbers is {args[0] - args[1]}")

# addition(5, 3, 4, 5, 6, 7, 8, 9)  # This will now work correctly with *args
# subtraction(10, 5)  # This will work correctly with the subtraction function

#Ternary operations

# a = 10

# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # OR

# print("Even") if a % 2 == 0 else print("Odd")

# Comparehensions

from ast import Pass


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# even = []
# odd = []

# for i in a:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even numbers:", even)
# print("Odd numbers:", odd)

#OR

# even = [i for i in a if i % 2 == 0]
# odd = [i for i in a if i % 2 != 0]

# print("Even numbers:", even)
# print("Odd numbers:", odd)

# Maping

# a = ["Moksh", "is", "a", "good", "boy"]
# b = list(map(len, a))
# print(b)

# temp_celc = [0, 10, 20, 34.5]
# temp_fahr = list(map(lambda x: (float(9)/5)*x + 32, temp_celc))
# print(temp_fahr)

# Filter

# m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = list(filter(lambda x: x % 2 == 0, m))
# print(even)

# more_than_5 = list(filter(lambda x: x > 5, m))
# print(more_than_5)

# Passed = list(filter(lambda x: x > 4, m))
# print(Passed)

# Zips

name = ["Moksh", "Rohit", "Sahil"]
marks = [90, 80, 70]

result = list(zip(name, marks))  # This will create a zip object
print(result)  # This will convert the zip object to a list of tuples
