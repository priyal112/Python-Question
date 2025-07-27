# Create classes Person and Employee. Create a class Manager that inherits from both.

class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, salary):
        self.salary = salary

class Manager(Person, Employee):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Employee.__init__(self, salary)

    def details(self):
        print(f"Manager: {self.name}, Salary: {self.salary}")

m = Manager("Mita", 90000)
m.details()