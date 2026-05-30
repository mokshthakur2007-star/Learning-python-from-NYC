# While loop 
# while loop keeps running as long as the condition is true.
# Here we need to use conditions similar to the things we were using in if else
# this shit works infinite times

#example 1
# while True:
#     print("Hello")

#example 2
# a = int(input("Enter a number : "))
# while a <= 100:
#     print(a)
#     a = a + 1
# if a > 100:
#     print("a is greater than 100")

# Example 3
# a = -20
# while a != 20:
#     print(a)
#     a = a + 1

# seperate each digit of a number and print it in a new line

# a = int(input("Enter a number : "))
# while a > 0:
#     print(a % 10)
#     a = a // 10

# print number is reverse

# a = int(input("Enter a number : "))
# rev = 0
# while a > 0:
#     rev = rev*10 + a%10
#     a = a//10
# print(f"The reverse of your number is {rev}")
# print(f"The difference between the original number and the reverse number is {a - rev}")

# check if the given number is a palindrome or not

a = int(input("Enter a number : "))
b = a 
# b is copy of a and by defining a=b and then using b in the while function, we are essentially retaining the value of a for later use,
# while we can manipulate b in the while loop to calculate the reverse of the number. This way, we can compare the original number (a) 
# with its reverse (rev) to determine if it is a palindrome or not.
rev = 0
while b > 0:
    rev = rev*10 + b%10
    b = b//10


if rev == a:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")