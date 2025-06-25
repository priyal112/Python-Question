# Write a Python program to find the maximum of three numbers

def find_max(num1, num2, num3):
    return max(num1, num2, num3)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

maximum = find_max(a, b, c)
print("The maximum number is:", maximum)