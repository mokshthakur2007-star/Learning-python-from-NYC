# multiplication table generator

n = int(input("Enter a number to generate its multiplication table: "))
print(f"Multiplication table for {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")