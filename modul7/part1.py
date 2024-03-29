class Car(object):
    name = 'car'
    fuel_support = [95, 98]
    color = 'white'
    doors = 4

    def __init__(self, doors=None):
        if doors:
            self.doors = doors
        print('Starting construction')

    def change_car_color(self, color):
        print(f'Changing car {self.name}')
        self.color = color

    def change_car_color_user_input(self):
        print(f'Changing car {self.name}')
        self.color = input('Set new car color:')

    def drive(self, whiles):
        print(f'Driving {whiles} while drive car')

class Dacia(Car):
    name = 'Logan'
    brand = '''Dacia'''

    def drive(self):
        print('Driving 2 while drive car')


class BMW(Car):
    name = 'x3'
    brand = '''BMW'''

    def drive(self):
        print('Driving 4 while drive car')


car = Car()
car.drive(3)

dacia = Dacia()
dacia.change_car_color('red')
dacia.drive()

bmw = BMW()
bmw.change_car_color('blue')
bmw.drive()

ZeroDivisionError()

