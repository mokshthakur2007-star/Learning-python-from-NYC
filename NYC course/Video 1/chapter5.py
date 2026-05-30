# name = "Moksh"
# age = 18

# print(f"My name is {name} and I am {age} years old.")

# # OR

# print("My name is ",name,"and I am ",age," years old.")

# name = input("Enter your name: ")
# print(f"Hello {name} welcome to Python programming!")

# age = int(input("Enter your age: "))
# print(f"You will be {age + 1} years old next year.")

# #Arithmetic operators : +, -, *, /, //, %, **
# a = 10
# b = 3
# print(a + b) #13
# print(a - b) #7
# print(a * b) #30
# print(a / b) #3.33
# print(int(a / b)) #3 this is same as a // b
# print(a // b) #3 this is same as int(a / b)
# print(a % b) #1
# print(a ** b) #1000

# print(2 ** 3 ** 2) #512 because it is evaluated from right to left, so it is 2 ** (3 ** 2) = 2 ** 9 = 512
# print((2 ** 3) ** 2) #64 because it is evaluated from left to right, so it is (2 ** 3) ** 2 = 8 ** 2 = 64
# print(2 ** 3 * 4) #64 because it is evaluated from left to right, so it is (2 ** 3) * 4 = 8 * 4 = 32
# print(2 * 3 ** 4) #162 because it is evaluated from right to left, so it is 2 * (3 ** 4) = 2 * 81 = 162
# print(1000 ** 1000)

# % is called mod operator and it gives the remainder when a is divided by b, it is also used to check if a number is divisible by another number or not, 
# if a % b == 0 then a is divisible by b, otherwise it is not divisible by b.
"""
() :- brackets
** :- exponentiation(right to left : 2**3**2 = 2**9 = 512)
* / // % :- multiplication, division, floor division, modulus(left to right)
+ - :- addition and subtraction(left to right)
"""

#11,6,22

#comparision operators : ==, !=, >, <, >=, <=
"""x = 10
y = 20
print(x == y) 
print(x != y) 
print(x > y) 
print(x < y) 
print(x >= y) 
print(x <= y) """

#logical operators : and, or, not
print (True and False) 
print (True or False) 
print (not True)
print (not False) 

print (12 > 234 or 234 == 234)
print (not (12 > 234 and 234 == 234))

#true, false, false

#assignment operators : =, +=, -=, *=, /=, //=, %=, **=
a = 10
a += 5 # a = a + 5
a -= 3 # a = a - 3
a *= 2 # a = a * 2
a /= 4 # a = a / 4
a //= 2 # a = a // 2
a %= 3 # a = a % 3
a **= 2 # a = a ** 2
print(a)