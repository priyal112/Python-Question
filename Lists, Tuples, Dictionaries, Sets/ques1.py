# Remove duplicates from a list

def remove_duplicates(lst):
    return list(set(lst))

# Test
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# Reverse a list without using reverse()

def reverse_list(lst):
    return lst[::-1]

# Test
print(reverse_list([1, 2, 3, 4]))
