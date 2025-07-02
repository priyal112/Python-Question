# Check if Number is Divisible by 3 and 5

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")

else: 
    print("Not Divisible by both 3 and 5")


# Check if Triangle is Valid

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a+b+c == 180:
    print("Valid triangle")

else:
    print("invalid triangle")