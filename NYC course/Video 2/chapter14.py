# sets

# set can never be empty, it can never have duplicate values, and it is unordered

# a = {1, 2, 3, 4, 5}
# print(type(a))

# conversion of list to set

# a = [1,1,2,2,2,3,4,5,5,5,5,6,7,8,6,5,6,7,8,8,9,9,9,9]
# s = set(a)
# print(s)


# basic functions of set
# s = {1, "hello", 1234, 1.5, (1, 2, 3)}

# s.add(10)
# print(s)
# a = s.pop()
# print(s)
# print(a)
# s.remove(1234)
# print(s)

# imp function of sets

# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# s3 = {4, 5}


# print(s2 - s1)
# #or
# print(s1.difference(s2))

# print(s1 - s2)
# #or
# print(s2.difference(s1))

# print(s1.intersection(s2))
# #or
# print(s1 & s2)

# print(s1.union(s2))
# #or
# print(s1 | s2)

# # is subset
# print(s3 <= s1)

# #is superset
# print(s1 >= s3)

# = us used to update the set with the union of itself and another set
# is symmetric difference -> gives the unique element in both sets
# print(s1 ^ s2)