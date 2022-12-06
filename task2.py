class Bottle():
    def __init__(self, color: str, volume: float = 0):
        self.color = color
        self.contains = volume

    def get_content(self):
        return self.contains

    def fill(self, volume):
        self.contains += volume


bottle_1 = Bottle('Красная')
bottle_2 = Bottle('Синяя')