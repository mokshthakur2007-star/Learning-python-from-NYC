#Object oriented programming OOP

#imperitive programming
# a = 10
# b = 20
# print(a + b)

#functional programming
# def add(a, b):
#     print(a + b)

# add(10, 20)
# add(30, 40)

#object oriented programming

#class is a blueprint for creating objects
#objetcs are instances of a class -> meaning that we can create multiple objects from a class
#there are 4 pillars of OOP
#1. Encapsulation -> keeping some data safe and only allowing access to it through methods
#2. Abstraction -> hiding the complexity of an object and only showing the essential features
#3. Inheritance -> creating a new class based on an existing class
#4. Polymorphism -> the ability of an object to take many forms

#We store attributes and methods in a class

# class animal:
#     species = "cat"

#     def sound(self):
#         print("meow")

# #you can access the attributes and methods of a class using the dot operator
# print(animal().species)
# animal().sound()

#objects

# class fruit:
#     name = "apple"

#     def color(self):
#         print("red")

# f = fruit() # this object has the power to call out the methods and attributes of the *class* fruit

# print(f.name)
# f.color()

#Constructors are special methods that are called when an object is created. They are used to initialize the attributes of an object.

# class fruit:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# f = fruit("apple", "red")
# print(f.name)
# print(f.color)

# class Bags:
#     def __init__(self, material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets


# reebok = Bags("leather", 3, 2)
# campus = Bags("canvas", 2, 4)

# print(reebok.material)
# print(campus.zips)
# print(reebok.pockets)

# class Animal:
#     def __init__(self, name):
#         self.name = name #object/instance attribute
    
#     def hello(self):
#         print(f"Hello, how are you? my name is {self.name}") #instance/object method
    
#     @classmethod
#     def details(cls):
#         print(f"This is a class method") #class method

#     @staticmethod
#     def speak():
#         print(f"This is a static method") #static method
    
# obj = Animal("Dog")
# print(obj.name)
# obj.hello()
# Animal.details()
# Animal.speak()

# Inheritance is a way to create a new class based on an existing class. 
# The new class is called the child class and the existing class is called the parent class. The child class inherits the attributes and methods of the parent class.

# class Animal: #parent class
#     def __init__(self, name):
#         self.name = name 
    
#     def details(self):
#         print(f"Hello your name is {self.name}")

# class Human(Animal): #child class
#     pass

# obj = Animal("Dog")
# obj2 = Human("John")
# obj.details()
# obj2.details()
# print(obj.name)
# print(obj2.name)

#your child class objects have the power to access the attributes and methods of the parent class. This is called inheritance.

# class BagFactory:
#     def __init__(self, material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets 
    
#     def details(self):
#         print(f"Your bag details are : material: {self.material}, zips: {self.zips}, pockets: {self.pockets}")

# class Reebok(BagFactory):
#     def __init__(self, material, zips, pockets, color):
#         super().__init__(material, zips, pockets) #super() is used to call the parent class constructor
#         self.color = color
    
#     def details(self):
#         print(f"Your bag details are : material: {self.material}, zips: {self.zips}, pockets: {self.pockets}, color: {self.color}")

# class Campus(Reebok):
#     def __init__(self, material, zips, pockets, color):
#         super().__init__(material, zips, pockets, color)

#     def details(self):
#         print(f"Your bag details are : material: {self.material}, zips: {self.zips}, pockets: {self.pockets}, color: {self.color}")

# bag1 = BagFactory("leather", 3, 2)
# bag2 = BagFactory("canvas", 2, 4)

# reebok_bag_1 = Reebok("Polyster", 3, 2, "blue")
# campus_bag_1 = Campus("Canvas", 2, 4, "green")

# bag1.details()
# bag2.details()
# reebok_bag_1.details()
# campus_bag_1.details()

# class Animal:
#     def __init__(self, name):
#         self.name = name
    
# class Humans:
#     def __init__(self, id):
#         self.id = id

# class Robots(Humans, Animal):
#     def __init__(self, name, id):
#         Humans.__init__(self, id)
#         Animal.__init__(self, name)

# robo = Robots("Moksh", 123) 

# Polymorphism

# it means 'many forms', it allows same interface to be used differently based on context and situation

#method 1 to achieve polymophism

# class animals:
#     def speak(self):
#         print("Animal don't speak")

# class humans:
#     def speak(self):
#         print("Humans speak")

# obj1 = animals()
# obj2 = humans()

# obj1.speak()
# obj2.speak()

# method 2 to achieve polymorphism -> method overriding (we need inheritance)

# class animal:
#     a=12
#     def __init__(self, name):
#         self.name = name

#     def details(self):
#         print(f"Animal name is {self.name}")

# class human(animal):
#     b=13
#     def __init__(self, name):
#         super().__init__(name)
    
#     def details(self):
#         super().details() #this will call the parent class method
#         print(f"Human name is {self.name}")
    
#     #if you're using same method in both, parent and child class, then the child class method will be called, and you loose the access to call same method from parent class, and this is called method overriding. But you can still call the parent class method using super() function.

#     def info(self):
#         print(f"your info is name: {self.name}, and that is all we have")

# obj = animal("lion")
# obj1 = human("Alice")
# obj2 = animal("Dog")

# obj.details()
# obj1.info()
# obj1.details()
# obj2.details()

# print(obj.a)
# print(obj1.b)
# print(obj.details)

#Method overloading is not supported in python, but we can achieve it using default arguments.

#Escapsulation is the process of hiding the internal details of an object and only exposing the necessary details to the outside world. This is done to protect the data from being modified by external code.

# class Factory:
#     a=12
#     name = "Kia" #public class attribute
#     _old = 5 #protected class attribute
#     __module = "Automotive" #private class attribute, it cannot be accessed outside the class, it is only accessible within the class.
#     def __init__(self, type, color, tyres):
#         self.__type = type #public instance attribute
#         self.color = color
#         self.tyres = tyres
    
# class hello(Factory):
#     print(Factory._Factory__module) #i can access the private class attribute using name mangling, but it is not recommended to do so.
    

# obj = Factory("SUV", "red", 4)

# obj.name = "Toyota" 
# obj.__type = "Sedan" 
# obj.color = "blue" #public instance attribute can be modified
# obj._old = 10 #protected instance attribute can be modified, it only exists to tell other language users that it exists.

# print(f'Brand : {obj.name}, Type : {obj._Factory__type},{obj.__type}, Color : {obj.color}, Tyres : {obj.tyres}')
# print(obj._old)
#print(obj.__module) #this will give an error because __module is a private attribute and cannot be accessed outside the class.

# also you can make loophole by calling method inside class and making the new method public, but noone writes that sort of code.

# Abstraction 
#it is the process of hiding the implementation details and showing only the functionality to the user. It is achieved using abstract classes and interfaces.

# from abc import ABC, abstractmethod

# class enforce(ABC):
#     @abstractmethod
#     def engine_start():
#         pass

# class bike(enforce):
#     def engine_start():
#         pass

# class car(enforce):
#     def engine_start():
#         pass

# class truck(enforce):
#     def engine_start():
#         pass

# obj1 = bike()
# obj2 = car()
# obj3 = truck()

#dunder methods

# class Animals:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"The name of the animal is {self.name}"

# obj = Animals("Lion")
# obj2 = Animals("Tiger")

# print(obj)
# print(obj2)

# class numbers():
#     def __init__(self, num):
#         self.num = num
    
#     def __add__(self, other):
#         return self.num + other.num

#     def __sub__(self, other):
#         return self.num - other.num
    
#     def __mul__(self, other):
#         return self.num * other.num
    
#     def __truediv__(self, other):
#         return self.num / other.num
    
#     def __mod__(self, other):
#         return self.num % other.num
    
#     def __eq__(self, other):
#         return self.num == other.num
    
# num1 = numbers(20)
# num2 = numbers(32)

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2)
# print(num1 == num2)

#dunder methods are way too many, we won't cover most of them

# a = 123
# print(type(a))
# print(dir(int))

# print dir prints all the dunder methods belonging to that particlar class

