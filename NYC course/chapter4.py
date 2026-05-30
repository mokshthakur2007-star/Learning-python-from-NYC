#a = " "

#print(ord(a))

# from turtle import st


# b = "COLLEGE"
# print(b)

# blank = " "
# print(blank)

# the thing in the [] is called an 
# index and it starts from 0 which is the first letter of any word
# so when i type print(c[0]), it will print the first letter of the string c
# there is both positive and negative indexing
# positive idexing begins from the leftmost letter, while negative indexing 
# begins from the rightmost letter

# c = "UNIVERSITY"
# print(c[0], c[-9])
# print(c[1], c[-8])
# print(c[2], c[-7])
# print(c[3], c[-6])
# print(c[4], c[-5])
# print(c[5], c[-4])
# print(c[6], c[-3])
# print(c[7], c[-2])
# print(c[8], c[-1])
# print(c[9])

# #string slicing
# d = 'COLLEGE'
# print(d[::])

# #practice question
# r = 'Hello how are you'
# print(r[6:9]) #how
# print(r[14:17]) #you
# print(r[0:5]) #Hello


# #type conversion 
# x = '2134'
# y = int(x)
# print(x)
# print(type(x))
# print(y)
# print(type(y))

# since python is interpreted, it can automatically convert one data type to another if needed, this is called implicit type conversion
# and for the same reason, when we provide same integer with 2 distinct values, it will always print the last value that was assigned.
# you can convert string to int if it holds valid integers
# you can convert float to int but it will only take the whole number part and ignore the decimal part
# you can convert int to float but it will add .0 at the end of the number

# a = 12.532

# a = float(a)
# print(a)


# b = '1243'
# b = float(b)
# print(b)

# m = 123
# n = 123.235235
# o = 12 + 234j
# p = True

# m = str(m)
# n = str(n)
# o = str(o)
# p = str(p)

# print(m)
# print(n)
# print(o)
# print(p)

# there are 7 values in python that are considered false, they are 0, 0.0, 0j, '', [], {}, set(), and None. all other values are considered true.

a = 12
b = 0
c = 123.3452
d = 0.0
e = ""
f = "Hello"
g = []
h = [1, 2, 3]
i = {}
j = {"name": "Alice", "age": 25}
k = set()
l = set([1, 2, 3])
m = None
print(bool(a)) #True
print(bool(b)) #False
print(bool(c)) #True
print(bool(d)) #False
print(bool(e)) #False
print(bool(f)) #True
print(bool(g)) #False
print(bool(h)) #True
print(bool(i)) #False
print(bool(j)) #True
print(bool(k)) #False
print(bool(l)) #True
print(bool(m)) #False

 