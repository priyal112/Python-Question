#User will input (3ages).Find the oldest one

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))

max = a

if max < b:
    max = b

if max < c:
    max = c

print(max)