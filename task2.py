from task1 import Item


class Phone(Item):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        assert isinstance(d, int)
        self.broken_phones = d
