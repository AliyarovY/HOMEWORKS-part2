class Employee:
    __slots__ = ('first', 'last')

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, nn: str):
        nn = nn.split()
        self.first = nn[0]
        self.last = nn[~0]

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    email = property(lambda self: f'{self.first}.{self.last}@email.com')



