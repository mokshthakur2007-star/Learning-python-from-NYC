# if not(5 == 5 and 10 > 5) or (3 < 2 and 4 > 1):
#     print("This will be printed.")
# else:
#     print("This will not be printed.")

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor, and you cannot vote.")
# else:
#     print("You are an adult, and you can vote.")

# score = float(input("Enter your score: "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B") # This runs, and Python skips the rest.
# elif score >= 70:
#     print("Grade: C")
# else:
#     print("Grade: F")


# money = int(input("Enter the amount of money mom gave you : "))

# if money >= 100 and money < 500:
#     print("You can buy a mcd meal.")
# elif money >= 50 and money < 100:
#     print("You can buy momos.")
# elif money >= 20 and money < 50:
#     print("You can buy a lays packet.")
# elif money >= 10 and money < 20:
#     print("You can buy a chocolate.")
# elif money >= 5 and money < 10:
#     print("You can buy a candy.")
# elif money >= 0 and money < 5:
#     print("You cannot buy anything. you are poor atm.")
# elif money >= 500 and money < 1000:
#     print("You got a lot of money, don't waste it on food only.")


# question 1
# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))

# if number_1 > number_2:
#     print(f"{number_1} is greater than {number_2}.")
# elif number_1 < number_2:
#     print(f"{number_2} is greater than {number_1}.")
# else:
#     print("Both numbers are equal.")

# question 2 (did a little different variation)
# age = int(input("Enter your age: "))
# gender = input("Enter your gender ( M/F ): ")

# if age < 0:
#     print("Invalid age. Age cannot be negative.")
# elif age < 18:
#     if gender == "M":
#         print("Greetings Master, you are a minor.")
#     elif gender == "F":
#         print("Greetings Miss, you are a minor.")
# elif age >= 18:
#     if gender == "M":
#         print("Greetings Sir, you are an adult male.")
#     elif gender == "F":
#         print("Greetings Ma'am, you are an adult female.")
#     else:
#         print("Invalid gender. Please enter either 'M' or 'F'.")

# print("hello" == "hello") # True
# print("Hello" == "hello") # False (bcz ord of "H" is 72 and that of "h" is 104, since 72 != 104, it returns False)
# print("123" == "123") # True
# print("123" == 123) # False, (because one is a string and the other is an integer and their ord is different)
# print("abc" == "ABC") # False, (because of case sensitivity)
# print("abc" == "abc") # True
# print("Hello" < "hello") # True, (because of the ord values of "H" and "h")

# print(ord("H"))


#question 2 (the real one this time)
# gen = input("Enter your gender (M/F) :- ")

# if gen == "M" or gen == "m":
#     print("Hello Sir")
# elif gen == "F" or gen == "f":
#     print("Hello Ma'am")
# else:
#     print("Invalid input. Please enter 'M' for male or 'F' for female.")


#question 3
# num = int(input("Enter a number : "))
# if num % 2 == 0:
#     print(f"{num} is an even number.")
# elif num % 2 != 0:   
#     print(f"{num} is an odd number.")
# elif num == 0:
#     print("0 is neither even nor odd.") 


#question 4
# name = input("Enter your name : ")
# age = int(input("Enter your age : "))


# if 18 <= age <= 125:
#     print(f"Hello {name}, you are an adult therefore you can vote.")
# elif 0 < age < 18:
#     print(f"Hello {name}, you will become a valid voter in {18 - age} years.")
# else :
#     print("Invalid age.")

#question 5
#approach 1
# year = int(input("Enter the year : "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:    
#     print(f"{year} is not a leap year.")

#approach 2
# year = int(input("Enter the year : ")) 
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:   
#     print(f"{year} is not a leap year.")

#approach 3
# year = int(input("Enter the year : "))
# if year % 100 == 0 and year % 400 == 0:
#     print(f"{year} is a leap year.")
# elif year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is a leap year.")
# elif year % 100 == 0 and year % 400 != 0:
#     print(f"{year} is not a leap year.")
# else:    
#     print(f"{year} is not a leap year.")

#approach 4
# year = int(input("Enter the year : "))
# if year % 4 == 0 or year % 400 == 0:
#         print(f"{year} is a leap year.")
# elif year % 100 == 0 and year % 400 != 0:
#         print(f"{year} is not a leap year.")
# else:
#     print(f"{year} is not a leap year.")

#question 6
# temp = float(input("Enter the temperature in Celsius : "))

# if temp <= 5 and temp >= -50:
#     print("It's freezing cold.")
# elif temp > 5 and temp <= 15:
#     print("It's a cold day.")
# elif temp > 15 and temp <= 27:
#     print("It's a pleasant day.")
# elif temp > 27 and temp <= 35:
#     print("It's a hot day.")
# elif temp > 35 and temp <= 50:
#     print("It's scorching hot.")
# elif temp > 50 and temp <= 60:
#     print("It's extremely hot.")
# elif temp < -50 or temp > 60 :
#     print("Invalid temperature. Please enter a value between -50 and 60 degrees Celsius.")