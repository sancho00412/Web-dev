class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 35:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = Mynumbers()
myiter = iter(myclass)
print(next(myiter))
for x in myiter:
    print(x)