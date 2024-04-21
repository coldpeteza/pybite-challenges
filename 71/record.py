class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.score = 0

    def __call__(self, *args, **kwargs):
        """ make sure there is at least one are to use"""
        if len(args) > 0:
            self.score = max(args[0], self.score)

        return self.score




