class Item:
    def __init__(self, name, price, quantity=0):
        assert self.__check(name, price, quantity), 'the type does not fit'
        self.name = name
        self.price = price
        self.quantity = quantity

    __check = lambda self, name, price, quantity: \
        [type(x) for x in (name, price, quantity)] == [str, int, int]

    __str__ = lambda self: f'{self.__class__.__name__}({(self.name, self.price, self.quantity)})'
