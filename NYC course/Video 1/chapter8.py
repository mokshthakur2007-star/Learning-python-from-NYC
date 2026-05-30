# this chapter is dedicated to for loop.
# here also range works range (start, stop, step) -> start is inclusive, stop is exclusive, step is the increment.
# for eg. range(0, 10, 2) will give us 0, 2, 4, 6, 8.
# note if you want range from 0 to 9, you can simply write range(10) as the default value of start is 0 and step is 1.
# if we want to print 0 to 9, we can do it like this :
# default values of start and step are 0 and 1 respectively, so we can simply write range(10) to get the same result. 
# steps for the range can be -ve if the range allows

# for i1 in range(10, 101, 1):
#      print(i1)

# print("I have printed numbers from 10 to 100.")

# for i2 in range(23, 57, 1):
#      print(i2)

# print("I have printed numbers from 23 to 56.")

# for i3 in range(0, 46, 1):
#     print(i3)

# print("I have printed numbers from 0 to 45.")

for i4 in range (0, 101, 10):
    print(i4)

# print("I have printed multiples of 10 from 0 to 100.")

# for i5 in range(100, 0, -10):
#     print(i5)

# print("I have printed multiples of 10 from 100 to 0.")

# for i6 in range(5, 51, 5):
#     print(i6)

# print("I have printed multiples of 5 from 5 to 50.")

# n = int(input("Enter a number : "))
# for i7 in range(n, (10*n)+1, n):
#     print(i7)

# a = "Students"
# for i in a:
#     print(i)
# for i in range(0,8,2):
#     print(a[i])
# for i in range(0, len(a), 1):
#     print(a[i])

# name = input("Enter your name : ")
# for i in range(0, len(name), 5):
#     print(f"[{i}] : {name[i]}")
# for i in name:
#     print(i)

# for i in range(0, 11, 1):
#     if i == 5:
#         break
#     print(i)

# print("I have printed numbers from 0 to 4.")

# for i in range(0, 11, 1):
#     if i == 5:
#         continue
#     print(i)

# print("I have printed numbers from 0 to 10, excluding 5.")

# for i in range(0, 11, 1):
#     if i == 3:
#         pass
#     if i == 2 or i == 5 or i == 7:
#         continue
#     if i == 8:
#         continue
#     if i == 9:
#         break
#     print(i)

# for i in range(0, 11, 1):
#     if i == 50:
#         break
#     print(i)
# else:
#     print("I have printed numbers from 0 to 4.")

# Q1
# for i in range(3):
#     print("Hello!")

# Q2
# n = int(input("Enter a number : "))
# for i10 in range(1, n+1 , 1):
#     print(i10)

# Q3
# n = int(input("Enter a number : "))
# for i11 in range(n, 0, -1):
#     print(i11)

# Q4
# made with help of AI
# n = int(input("Enter a number : "))
# for i12 in range(n, 10*n+1, n):
#     print(f"{n} x {i12//n} = {i12}")

#Easier format of Q4
# n = int(input("Enter a number : "))
# for i14 in range(1, 11, 1):
#     print(f"{n} x {i14} = {n*i14}")

# Q5
# n = int(input("Enter a number : "))
# for i13 in range(n+1):
#     print((i13*i13+i13)/2)

# Q5 easier format
# n = int(input("Enter a number : "))
# print (int((n*n+n)/2))

# Q5 even easier format
# a = 0
# n = int(input("Enter a number : "))
# for i in range(1, n+1, 1):
#     a = a + i
# print(a)

# Q6 bhaiya ke help se and using Q5's even easier format thinking
# a = 1
# n = int(input("What number's factorial do you want to find? : "))
# for i in range(1, n+1, 1):
#     a = a * i
# print(a)

# Q7 print sum of all even and odds numbers in a range seperately
# a = 0
# b = 0
# n = int(input("Enter a number : "))
# for i in range(1, n+1, 1):
#     if i % 2 == 0:
#         a = a + i
#     else:
#         b = b + i

# print(f"The sum of even numbers from 1 to {n} is {a}.")
# print(f"The sum of odd numbers from 1 to {n} is {b}.")

# Q8 print all factors of a number
# n = int(input("Enter the number whose factors you want to find : "))
# for i in range(1, n+1, 1):
#     if n % i == 0:
#         print(i)



# self question -> print all prime numbers in a range given by user

# lower = int(input("Enter the lower limit from which you want to find prime numbers : "))
# upper = int(input("Enter the upper limit up to which you want to find prime numbers : "))

# for num in range(lower, upper + 1, 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
#     elif num == 1:
#         print("1 is neither prime nor composite.")
#     elif num == 0:
#         print("0 is neither prime nor composite.")
#     elif num < 0:
#         print(f"{num} is a negative number and negative numbers cannot be prime.")
#     else:
#         print("Invalid input.")


# Q9 check if a number is perfect number or not
# n = int(input("Enter a number : "))
# s = 0

# for i in range(1, n):
#     if n % i == 0:
#         s = s + i

# if s == n:
#     print(f"{n} is a perfect number.")
# else:
#     print(f"{n} is not a perfect number.")


# Q10 check if number is prime or not

# n = int(input("Enter the number : "))
# for i in range(2, n):
#     if n % i == 0:
#         print(f"{n} is not a prime number.")
#         break
# else:   
#     print(f"{n} is a prime number.")

# method by bhaiya for Q10
# n = int(input("Enter the number : "))
# count = 0

# for i in range(1, n+1, 1):
#     if n % i == 0:
#         count = count + 1


# if count == 2:
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is composite number. It has {count} factors, and those factors are : ", end="") # extra part added by me for fun, bcz i want coding to be fun
#     for i in range(1, n+1, 1):
#         if n % i == 0:
#             print(i, end=" ")

# Q11 reverse the string wihtout using build in functions

# a = input("Enter a word : ")
# rev = ""

# for i in range(len(a)-1, -1, -1):
#     rev = rev + a[i]
# print(f"the reversed word is : {rev}")


# Q12 check if a word is palindrome or not

# word = input("Enter a word : ")
# rev = ""
# for i in range(len(word)-1, -1, -1):
#     rev = rev + word[i]
# if word == rev:
#     print(f"{word} is a palindrome.")
# else:
#     print(f"{word} is not a palindrome.")


# Q13 count letter, digits and special characters in a string

# using inbuilt functions
# string = input("Enter a string : ")
# count_letters = 0
# count_digits = 0
# count_special = 0
# for i in string:
#     if i.isalpha():
#         count_letters =  count_letters + 1
#     elif i.isdigit():
#         count_digits = count_digits + 1
#     else:
#         count_special = count_special + 1

# print(f"Letters: {count_letters}")
# print(f"Digits: {count_digits}")
# print(f"Special Characters: {count_special}")

# print(ord('1'))
# print(ord('2'))
# print(ord('3'))
# print(ord('4'))
# print(ord('5'))
# print(ord('6'))
# print(ord('7'))
# print(ord('8'))
# print(ord('9'))
# print(ord('0'))
# 48 to 57 are the ascii values of digits from 0 to 9 respectively.

# print(ord('a'))
# print(ord('b'))
# print(ord('c'))
# print(ord('x'))
# print(ord('y'))
# print(ord('z'))
# 97 to 122 are the ascii values of lowercase letters from a to z respectively.

# print (ord('!')) 33
# print (ord('@')) 64
# print (ord('#')) 35
# print (ord('$')) 36
# print (ord('%')) 37
# print (ord('^')) 94
# print (ord('&')) 38
# print (ord('*')) 42
# print (ord('(')) 40
# print (ord(')')) 41


# method without using inbuilt functions
# string = input("Enter a string : ")
# count_letters = 0
# count_digits = 0
# count_special = 0

# for i in string:
#     if 97 <= ord(i) <= 122:
#         count_letters =  count_letters + 1
#     elif 48 <= ord(i) <= 57:
#         count_digits = count_digits + 1
#     elif 33 <= ord(i) <= 42 or 64 <= ord(i) <= 94:
#         count_special = count_special + 1

# print(f"Letters: {count_letters}")
# print(f"Digits: {count_digits}")
# print(f"Special Characters: {count_special}")