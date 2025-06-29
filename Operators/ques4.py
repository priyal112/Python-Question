# Write a program that asks if the user has a license and is above 18. Print "Can drive" only if both are true.

license_has = input("Do you have license? (yes/no): ").lower()
age = int(input("Your age: "))

if license_has == "yes" and age>=18:
    print("Can drive")

else:
    print("Can not drive")