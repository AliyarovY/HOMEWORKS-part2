from dataclasses import dataclass


@dataclass
class Student:
    name: str
    stud_id: int

    def __post_init__(self):
        self.lap = self.Laptop()

    def show(self):
        print(*(self.name, self.stud_id))
        dc = self.lap.__dict__
        print(*[dc[k] for k in dc if k in 'brand cpu ram'.split()])

    @dataclass
    class Laptop:
        brand: str = 'HP'
        cpu: str = 'i5'
        ram: int = 8
