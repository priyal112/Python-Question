# Create a class Book with title and author. Create two book objects and print their details.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"'{self.title}' by {self.author}")

b1 = Book("Python Basics", "Alice")
b2 = Book("Learn OOP", "Bob")

b1.display()
b2.display()