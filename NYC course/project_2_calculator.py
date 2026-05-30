num1 = float(input("Enter a number : "))
num2 = float(input("Enter another number : "))
function = input("Enter the function you want to perform (+,-,*,/, **) : ")
if function == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif function == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif function == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif function == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division by zero is not allowed.")
elif function == "**":
    print(f"{num1} ** {num2} = {num1 ** num2}")
else:
    print("Invalid function entered. Please enter one of +, -, *, /, or **.")