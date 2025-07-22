# Create a Class with Attributes and Method

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, marks: {self.marks}")

s1 = Student("Priyal", 87)
s1.display()