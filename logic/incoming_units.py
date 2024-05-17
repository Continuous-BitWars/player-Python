class IncomingUnits:
    incoming: {int: int} = {}

    def __init__(self, incoming: {int: int} = None):
        if incoming is not None:
            self.incoming = incoming

    def __getitem__(self, key):
        return self.incoming[key] if key in self.incoming.keys else 0

    def __setitem__(self, key, value):
        self.incoming[key] = value

    def __delitem__(self, key):
        del self.incoming[key]

    def __str__(self):
        return str(self.incoming)

    def sum(self, indexes: tuple[int]):
        sum_units = 0
        for i in indexes:
            if i in self.incoming.keys:
                sum_units += self.incoming[i]
        return sum_units

