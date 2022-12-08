class Derivative:
    def __init__(self, f):
        self.func = f
    def __call__(self, a):
        assert isinstance(a, int | float)
        return (self.func(a + 0.0001) - self.func(a)) / 0.0001

