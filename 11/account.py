class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self):
        return len(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __str__(self):
        return f"{self.name} account - balance: {self.balance:d}"

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError

        self._transactions.append(other)
        return self

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError

        self._transactions.append(-other)
        return self

    def __index__(self):
        return self._transactions

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]
