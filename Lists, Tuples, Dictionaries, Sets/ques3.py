# Merge two dictionaries

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
merged = {**a, **b}  # b will override common keys
print(merged)


# Count frequency of characters in a string

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Test
print(char_frequency("interview"))


