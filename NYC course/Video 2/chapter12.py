# list

# a = [1, 2, 3, 4, 5]
# print(a[-1])
# print(type(a))
# ordered nature and can access any element at any point of time.
# string has immutable nature, list has mutable nature, we can change the value of item in list

# l = [10, 22, 30, 40, 50]
# l[1] = 20
# print(l)

#traversing on list -> running loop on list
#you can have duplicate values

# a = [10, 20, 30, 40, 50]

#traversing in values

# for i in a:
#     print(i)

#traversing in index

# for i in range(0,5,2):
#     print(a[i])

# OR

# for i in range(len(a)):
#     print(f"{i} : {a[i]}")


# CRUD operation -> create, read, update, delete

# append -> add element at the end of list

# a = [10, 20, 30, 40, 50]
# a.append(60)
# a.append("hello")
# print(a)

# insert -> add element at specific index

# a = [10, 20, 30, 40, 50]
# a.insert(2, 25)
# print(a)

# delete -> remove element from list

# a = [10, 20, 30, 40, 50]
# a.remove(30)
# print(a)

# pop -> remove element from list based on index
# a = [10, 20, 30, 40, 50]
# b = a.pop(2)
# print(a)
# print(b)

# sort -> sort the list in ascending order

# a = [20, 10, 50, 30, 40]
# a.sort()
# print(a)

# or

# a.sort(reverse=True)
# print(a)

# reverse -> sort the list in descending order
# a = [50, 20, 30, 40, 10]
# a.reverse()
# print(a)

# clear -> remove all the elements from list
# a = [10, 20, 30, 40, 50]
# a.clear()
# print(a)

# len -> gives the length of list

# a = [10, 20, 30, 40, 50]
# print(len(a))

# return statement

# def hello():
#     return "hello world"

# b = hello()
# print(b)

# Q1

# auto way

l = [3, -1, 4 ,-5, 9]
# def positive(l):
#     res = []
#     for i in l:
#         if i > 0:
#             res.append(i)
#     return res
# def negative(l):
#     res = []
#     for i in l:
#         if i < 0:
#             res.append(i)
#     return res
# print(f"Positive numbers: {positive(l)}")
# print(f"Negative numbers: {negative(l)}")

# bhaiya way

# pos = []
# neg = []
# for i in l:
#     if i > 0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(f"Positive numbers : {pos}")
# print(f"Negative numbers : {neg}")

# Q2
# l = [10, 20, 30, 40]

# sum = 0

# for i in l:
#     sum = sum + i

# avg = sum/len(l)
# print(f"Average of list is : {avg}")

# Q3

# My method

# l = [4, 8, 2, 9, 1]
# s = l.copy()
# s.sort(reverse=True)
# print(f"Greatest number in list is : {s[0]} with index {l.index(s[0])}")

# l = [234, 567, 890, 123, 456, 235, 678, 789, 345, 567, 890, 123, 456, 235, 678, 789]
# s = l.copy()
# s.sort(reverse=False)
# print(f"lowest number in the list is {s[0]} and its index is {l.index(s[0])}")

# Bhaiya method -> better and faster than my method bcz it is not using copy and sort method which are time consuming

# pure bhaiya method

# l = [4, 8, 2, 9, 1]
# largest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
# print(f"Greatest number in list is : {largest} with index {index}")

# changed bhaiya method (more efficient)

# l = [4, 8, 2, 9, 1]
# largest = l[0]
# for i in l:
#     if i > largest:
#         largest = i
# print(f"Greatest number in list is : {largest} with index {l.index(largest)}")

# l = [234, 567, 890, 123, 456, 235, 678, 789, 345, 567, 890, 123, 456, 235, 678, 789]
# largest = l[0]
# for i in l:
#     if i < largest:
#         largest = i
# print(f"Lowest number in list is : {largest} with index {l.index(largest)}")

# Q4

# a = [4, 2, 1, 10, 7]

# larg = l[0]
# second_larg = l[0]

# for i in a:
#     if i > larg:
#         second_larg = larg
#         larg = i
#     elif i > second_larg:
#         second_larg = i
        
# print(second_larg)

# Q5 -> check if list is already sorted or not

# l = [1,2,3,4]

# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("List is not sorted")
#         break
# else:
#     print("List is sorted")