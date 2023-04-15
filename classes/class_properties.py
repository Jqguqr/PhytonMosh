class Product:

    """
    def __init__(self, price):
        self.set_price(price)

    # This methods (getter and setter) is not pytonic
    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value

    # Pithon better prictise using Python language features
    price = property(get_price, set_price)
    """

    # Best pryctice
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value


product = Product(-10)
print(product.price)
