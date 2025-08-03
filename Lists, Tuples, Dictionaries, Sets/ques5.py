# Find all pairs in a list whose sum is equal to a target number

def find_pairs(nums, target):
    seen = set()      # to remember the numbers we have seen
    pairs = []        # to store pairs that add up to target

    for num in nums:
        match = target - num     # the number we want to find
        if match in seen:
            pairs.append((match, num))  # found a pair!
        seen.add(num)           # remember this number
    
    return pairs

# Test the function
numbers = [2, 4, 3, 5, 7, 8, 1]
target_sum = 9
result = find_pairs(numbers, target_sum)
print(result)
