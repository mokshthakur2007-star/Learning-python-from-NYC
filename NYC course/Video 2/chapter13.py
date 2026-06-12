# Tuple -> immutable list mean we cannot change the value of item in tuple

# t = (10, 20, 30, 40, 50)
# print(type(t))

# a = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
# print(a[0])
# print(a[-1])
# print(a[2:5])

# you can also convert list to tuple 
# l = [10, 20, 30, 40, 50, 10, 10, 'mpo', 'ewr', 'mpo']
# t = tuple(l)


# tuple has only 2 built in function -> count and index

# print(t.count(10))
# print(t.index(30))

# example for tuple unpacking

def student():
    return "akarsh" , 20, "akarsh@gmail.com"

print(student())
print(type(student()))
name, age, email = student()
print(name)
print(age)
print(email)