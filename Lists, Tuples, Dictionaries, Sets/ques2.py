# Swap two tuples

a = (1, 2)
b = (3, 4)
a, b = b, a
print("a =", a, "b =", b)


# Count occurrences of an element in a tuple

t = (1, 2, 3, 2, 2, 4, 2)
print(t.count(2))  # Output: 4
