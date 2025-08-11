# Find the longest word in a sentence

sentence = "Find the longest word in a sentence"
words = sentence.split()  # split into words
longest = max(words, key=len)  # find word with max length
print(longest)
