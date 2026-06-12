#chapter 10 : functions
# fucntion : code of block with a name
# two types of function -> inplicit(user defined) and explicit (built in)

def palindrome_checker(a):
    copy = a
    rev = 0
    while a > 0:
        rem = a % 10
        rev = rev * 10 + rem
        a = a // 10
    if copy == rev:
        print(f"{copy} is a palindrome")
    else:
        print(f"{copy} is not a palindrome")

# this type of approach, by defining a function, is called functional approach

# palindrome_checker(123321)
# palindrome_checker(2342352)
# palindrome_checker(12321)

# parameters are values you accept while calling function.
# arguments are values you provide while calling function.

# positional argunments

def multiply(a, b, c, d):
    print(a * b * c * d)

# multiply(1, 2, 3, 4) here value of argument needs to be given


# default arguments

def addition(a, b, c = 12):
    print(a + b + c)

# addition(1, 2) here value of c is not given, so it will take default value 12, bcz i have set it
# but if i use addition(1, 2, 3) then it will take value of c as 3, bcz i have given it as argument


# keyword arguments
def subtraction(a, b, c = 12):
    print(a - b - c)

subtraction(b = 10, a = 5) 