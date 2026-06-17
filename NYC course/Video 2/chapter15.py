# Dictionary
# A dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed by keys.

# Vanilla Python

# d = {1:10, 2:20, 3:30, 4:40, 5:50}
# d[6] = 60 # creating new key-value pair
# d[1] = 100 # updating value of existing key

# # Method approach

# d = {1:10, 2:20, 3:30, 4:40, 5:50}
# print(d.get(1)) # accessing value using key
# print(d.get(6)) # accessing non-existent key (returns None)
# print(d.get(6, "Key not found")) # accessing non-existent key with default value
# print(d.items()) # returns a view object of key-value pairs
# print(d.keys()) # returns a view object of keys
# print(d.values()) # returns a view object of values
# # d.pop(1) # removes the key-value pair with key 1
# # print(d)
# # d.popitem() # removes and returns an arbitrary key-value pair (in Python 3.7+ it removes the last inserted pair)
# # print(d)
# d.setdefault(6, 60) # returns the value of key 6 if it exists, otherwise sets it to 60 and returns 60
# print(d)
# d.update({7:70, 8:80}) # updates the dictionary with key-value pairs from another dictionary
# print(d)

# Traversing (loops)

# d = {1:10, 2:20, 3:30, 4:40, 5:50}
# for i in d:
#     print(f"key is {i}, value is {d[i]}")


# Practice problems

# Q1

#by method
# d1 = { 'a' : 1}
# d2 = { 'b' : 2}
# d1.update(d2)
# print(d1)

#logic building

# d1 = { 'a' : 1}
# d2 = { 'b' : 2}
# for i in d2:
#     d1[i] = d2[i]
# print(d1)

# Q2

# d = {"a":10, "b":20, "c":30, "d":40, "e":50}
# sum = 0
# for i in d:
#     sum = sum + d[i]
# print(sum)

# Q3

#simple method / noob way
# l = ["a", "b", "a", "c", "b", "a"]
# counta = 0
# countb = 0
# countc = 0
# for i in l:
#     if i == "a":
#         counta += 1
#     elif i == "b":
#         countb += 1
#     elif i == "c":
#         countc += 1
# print(f"count of a is {counta}, count of b is {countb}, count of c is {countc}")

# better way using dictionary
# l = ["a", "b", "a", "c", "b", "a"]
# d = {}
# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# Q4

# d1 = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
# d2 = { 'd' : 2, 'e' : 3, 'f' : 4, 'g' : 5}

# for i in d2:
#     if i in d1:
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)

