from itertools import count


class Animal:
    storage = dict()
    iter = count(10001)

    def __init__(self, name):
        self.name = name.title()
        self.val = next(self.iter)
        self.storage[self.val] = self.name

    def __str__(self):
        return f"{self.val}. {self.name}"

    @classmethod
    def zoo(cls):
        result = []
        for number, animal in cls.storage.items():
            result.append(f"{number}. {animal}")
        return '\n'.join(result)
