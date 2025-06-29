# Check if a Character is a Vowel or Consonant

ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("It is vowel")

elif ch.isalpha():
    print("Is is consonant")

else:
    print("Not an alphabet")