class Vehicle:

    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return 0  # to be realized

    def move_along(self, route):
        print("moving")


class Car(Vehicle):
    turn_on_radio = lambda self, x: print(x) if isinstance(x, str) else print('Type')


class Airplane(Vehicle):
    pass
