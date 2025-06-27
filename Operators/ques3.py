# Write a Python program to check if a number is between 10 and 50 (inclusive).

num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("The number is in the range 10 to 50")

else:
    print("The number is outside the range")


# Take user input of age and income. Print "Eligible for loan" if age > 18 and income > 25000.

age = int(input("Enter your age: "))
income = float(input("Enter your income: "))

if age > 18 and income > 25000:
    print("Eligible for loan")

else:
    print("Not Eligible for loan")