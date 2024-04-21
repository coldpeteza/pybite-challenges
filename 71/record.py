class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.score = 0

    def __call__(self, *args, **kwargs):
        """ make sure there is at least one are to use"""
        if len(args) > 0:
            self.score = max(*args, self.score)

    def __str__(self):
        return str(self.score)


if __name__ == '__main__':
    a = RecordScore()
    # alternate use for multiple scoring
    a(10, 9, 22)
    print(a)
