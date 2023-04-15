# Animal: Parent, Base class
class Animall:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


# Mammal: Child, Sub class
class Mammal(Animall):
    def __init__(self):
        print("Mamal Constructor")
        super().__init__()
        self.weight = 2


dog = Mammal()
dog.eat()
print(dog.age)
print(dog.weight)
