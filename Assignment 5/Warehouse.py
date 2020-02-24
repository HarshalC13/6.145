class Warehouse:
    def __init__(self):
        self.dict = {}

    def process(self, tup):
        if tup[0] == 'receive':
            if tup[1] in self.dict:
                self.dict[tup[1]] = self.dict[tup[1]] + tup[2]
            elif tup[1] not in self.dict:
                self.dict[tup[1]] = tup[2]
        if tup[0] == 'ship':
            if tup[1] in self.dict:
                self.dict[tup[1]] = self.dict[tup[1]] - tup[2]
            elif tup[1] not in dict:
                self.dict[tup[1]] = tup[2]

    def lookup(self, char):
        if char in self.dict:
            return self.dict[char]
        elif char not in self.dict:
            return 0


w = Warehouse()
w.process(('receive', 'a', 10))
w.process(('ship', 'a', 7))
print(w.lookup('a'))  # prints 3
print(w.lookup('b'))  # prints 0
