class Flight:

    def __init__(self, city_from, city_to):
        assert all(isinstance(x, str) for x in [city_from, city_to])
        self.__city_from = city_from
        self.__city_to = city_to

    def __str__(self):
        return f'Flight from {self.__city_from} to {self.__city_to}'



