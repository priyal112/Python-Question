# Write a program that takes two numbers and prints whether the first is greater, less, or equal to the second.

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

if a > b:
    print("First number is greater")

elif a < b:
    print("First number is smaller")

else:
    print("Both numbers are equal")