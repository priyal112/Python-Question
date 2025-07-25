# Create two classes Bird and Sparrow where both have the method fly, but different outputs.

class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow:
    def fly(self):
        print("Sparrow flies fast")

b = Bird()
s = Sparrow()

b.fly()
s.fly()
