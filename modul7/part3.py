print(len([1, 2]))
print(len('abcd'))

print([1, 2].__len__())
print('abcd'.__len__())
# print((1).__len__())


class Car:

    def __len__(self):
        return 120

c = Car()
print(len(c))

class Truck(Car):

    def __len__(self):
        return 250


t = Truck()
print(len(t))

t = [1, 2, 33]

def check_truck(t: Truck):

    if t.__len__() > 200:
        print('Truck is to long')
    else:
        print('Truck is not to long')

check_truck(t)
