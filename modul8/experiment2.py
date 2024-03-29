class Test():
    color = None
    size = None

    def __str__(self):
        return f'{self.__class__.__name__}_{self.color}_{self.size}'

    def __repr__(self):
        return 'b'

    def __init__(self, color, size):
        self.color = color
        self.size = size

a = Test('blue', 10)
b = Test('green', 20)

print(a, b)