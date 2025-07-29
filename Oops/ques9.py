# Create a class MathTools with a static method is_even(n)

class MathTools:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

# Test
print("Is 4 even?", MathTools.is_even(4))
