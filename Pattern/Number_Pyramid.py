# Number Pyramid

n = 4

for i in range(1, n+1):
    print(" " * (n - i), end="")
    print((str(i) + " ") * i)


# str(i) → converts the number to a string (so you can repeat it)

# str(i) + " " → adds a space after the number (like "2 ")

# (...) * i → repeats this i times