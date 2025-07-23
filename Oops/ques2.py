# Class with Default Constructor and Method

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} Car Started....")

c = Car("lamborghini")
c.start()
