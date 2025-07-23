# Create a class Animal with a method speak. 
# Create another class Dog that inherits from Animal and overrides the method.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()
