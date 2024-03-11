result = 'abc'.__iter__()
print(type(result))

print(id(result))
print(id(result.__iter__()))

print(next(result))
print(result.__next__())
print(result.__next__())
# print(result.__next__())
print('Iterator is consumed')

result = 'abc'
iterator = result.__iter__()
for i in iterator:
    print(i)

# number = 5
# for i in number:
#     print(i)


# class Number:
#
#     def __init__(self, number):
#         self.number = number
#
#     def __iter__(self):
#         return range(self.number).__iter__()  ### but we want float
#
# n = Number(5)
#
# for i in n:
#     print(i)

print('Iterator is consumed')
class Number(int):

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return NumberIterator(self.number)

    # def __add__(self, other):
    #     return other.__add__(self)

class NumberIterator:

    def __init__(self, number):
        self.number = number
        self.number_list = []
        for i in range(self.number):
            self.number_list.append(i+1)
        self.number_list.sort(reverse=True)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.number_list.pop()
        except IndexError:
            raise StopIteration
        return float(result)


n = Number(5)
m = Number(6)

for i in n:
    print(i)

print(m + n)
print(m - n)
print(m / n)

# for i in n + m:
#     print(i)