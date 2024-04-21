class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.score = None

    def __call__(self, *args, **kwargs):
        """ make sure there is at least one are to use"""
        if self.score is not None and len(args) > 0:
            self.score = max(args[0], self.score)




