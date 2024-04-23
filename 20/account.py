class Account:

    def __init__(self):
        self._transactions = []
        self._backup_transactions = None

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager
    def __enter__(self):
        # this option enables full rollback mode, all or nothing
        self._backup_transactions = self._transactions.copy()
        return self

    def __exit__(self, etype, value, traceback):
        if self.balance < 0:
            self._transactions = self._backup_transactions.copy()
            self._backup_transactions = None
