# Create a class Calculator with methods for addition, subtraction, multiplication, and division.

class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Can't divide"
        
calc = Calculator()
print("Add:", calc.add(5, 3))
print("Divide:", calc.divide(10, 2))
print("Subtract:", calc.sub(9, 3))
print("Multiply:", calc.multiply(4, 6))