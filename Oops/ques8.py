# Create a class Box and compare two objects by their volume using ==.

class Box:
    def __init__(self, length, width, height):
        self.volume = length * width * height

    def __eq__(self, other):
        return self.volume == other.volume
    
b1 = Box(2, 3, 4)
b2 = Box(4, 3, 2)
print("Boxes equal?", b1 == b2)