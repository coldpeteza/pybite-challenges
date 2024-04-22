from dataclasses import dataclass


@dataclass(order=True)
class Bite:
    number: int
    title: str
    level: str = 'Beginner'

    # def __init__(self, number: int, title: str, level: str = 'Beginner'):
    #     self.number = number
    #     self.title = title
    #     self.level = level

    def __post_init__(self):
        self.title = self.title.capitalize()


