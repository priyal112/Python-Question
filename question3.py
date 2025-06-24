#User will input (2numbers).Write a program to swap the numbers

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

k = a
a = b
b = k

print("value of a", a)
print("value of b", b)