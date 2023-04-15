class Point:
    # class attribute
    # default_color = "red"

    def __init__(self, x, y):
        # instance attribute
        self.x = x
        self.y = y

    # class method
    """
    @classmethod
    def zeros(cls):
        cls(0, 0)
    """

    # Magic method
    def __str__(self):
        return (f"({self.x}, {self.y})")

    # Magic method to compare objects
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Magic method to comparate mayority
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # Aritmetic Magic methods
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# point.draw()
# print(point)

other = Point(1, 2)
# print(point == other)
# print(point > other)

combined = point + other
print(combined.x, combined.y)
