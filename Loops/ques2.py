# Print multiplication table of a number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")


# Print even numbers between 1 and 100

for i in range(2, 102, 2):
    print(i, end=' ')