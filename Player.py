from dataclasses import dataclass, field


@dataclass()
class Player:
    name: str
    used: list[str] = field(default_factory=lambda: [])

    def __post_init__(self):
        self.name = self.name.title()

    def n_used(self) -> int:
        return len(self.used)

    def add(self, word: str) -> None:
        if not isinstance(word, str):
            return False
        self.used.append(word)

    def is_used(self, word: str) -> bool:
        return word in self.used

    def __repr__(self):
        return f'{self.name}, {self.used}'

    def __str__(self):
        return f'{self.name}\'s used words is ->   | {" | ".join(self.used)} |'
