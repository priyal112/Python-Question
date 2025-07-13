# Count Words in a Sentence

def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("I love it"))