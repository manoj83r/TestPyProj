class Iterator:
    def __init__(self):
        self.a=1

    def __iter__(self):
        return self

    def __next__(self):
        if (self.a <=10):
            b = self.a
            self.a += 1
            return b
        else:
            raise StopIteration


val = Iterator()

print(next(val))

for i in val:
    print("value is:" + str(i))