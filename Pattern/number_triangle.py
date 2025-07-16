# Number Triangle

n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    print()


# Reverse Number Triangle

n = 4

for i in range(n, 0, -1):        # Start at n → which is 4 , Stop before 0 (so it stops at 1), 
    for j in range(1, i + 1):    # Step is -1 → which means we go down by 1 each time
        print(j, end=" ")

    print()