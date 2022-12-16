class Meta(type):
    def __new__(cls, name, base, attrs):
      attrs = {k.upper(): v for k, v in attrs.items()}
      return super().__new__(cls, name, base, attrs)


class Math(metaclass=Meta):
    pi = 3.141592653589793
    e = 2.718281828459045
    tau = 6.283185307179586
