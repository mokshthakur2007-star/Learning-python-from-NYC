import timeit
import random

# Generate a large list of 100,000 random numbers
large_list = [random.randint(1, 1000000) for _ in range(100000)]

# Code 1: The Loop Approach
def loop_approach(l):
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
    idx = l.index(largest)
    return largest, idx

# Code 2: The Sort Approach
def sort_approach(l):
    s = l.copy()
    s.sort(reverse=True)
    idx = l.index(s[0])
    return s[0], idx

# Run each 100 times to get a stable average
time_loop = timeit.timeit(lambda: loop_approach(large_list), number=100)
time_sort = timeit.timeit(lambda: sort_approach(large_list), number=100)

print(f"Loop Approach Total Time: {time_loop:.5f} seconds")
print(f"Sort Approach Total Time: {time_sort:.5f} seconds")
print(f"The Loop approach is roughly {round(time_sort / time_loop)}x faster at this scale.")