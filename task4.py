class MyInt:
    def __init__(self, x):
        assert isinstance(x, int | str)
        self.x = x

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return f'{self.__class__}: {self.x}'

    @staticmethod
    def check(y):
        return [y, int(y)][isinstance(y, str)]

    for n, op in zip('add mul sub truediv'.split(), '+*-/'):
        exec(f'def __{n}__(self, other): return MyInt(self.x {op} self.check(other))')
    for n, op in zip('eq gt ge lt le'.split(), '== > >= < <='.split()):
        exec(f'def __{n}__(self, other) : return self.x {op} self.check(other)')
