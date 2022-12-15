class Item:
    pay_rate = 0.8
    alll = []

    def __init__(self, name: str, price: float, quantity=0):
        assert all(isinstance(x, y) for x, y in zip([name, price, quantity], [str, float, int]))
        self.name = name
        self.price = price
        self.quantity = quantity
        self.alll += [self]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Название слишком длинное!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        with open(file) as ff:
            for i, j in enumerate(ff):
                if i == 0:
                    continue
                j = j.strip().split(',')
                [Item(j[0], float(j[1]), int(j[2])), Item(j[0], float(j[1]))][len(j) == 2]

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'
