
class PowerOfTwo:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            result = 2 ** self.current
            self.current += 1
            return result
        raise StopIteration

numbers = PowerOfTwo(8)

for number in numbers:
    print(number)
