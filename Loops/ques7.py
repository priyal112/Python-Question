# Check if a number is prime

num = int(input("Enter number: "))

if num <= 1:
    print("Not Prime")

else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")

    else:
        print("Not Prime")