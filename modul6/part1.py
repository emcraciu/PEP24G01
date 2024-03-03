class Car:
    brand = 'Dacia'
    fuel_support = [95, 98]
    color = 'white'
    doors = 4
    # cars_built = []

    def __init__(self, doors=None):
        if doors:
            self.doors = doors
        print('Starting construction')

    def change_car_color(self, color):
        print(f'Changing car {self.brand}')
        self.color = color
    def change_car_color_user_input(self):
        print(f'Changing car {self.brand}')
        self.color = input('Set new car color:')


car = Car(2)
print(car.brand)
car.brand = 'BMW'
car.fuel_support.append(101)
print(car.brand)
print(car.fuel_support)
car.change_car_color('red')
print(car.color)
print(f'Car {car.brand} nr of door is: {car.doors}')

car2 = Car()
print('new car:', car2.brand)
print('new car:', car2.fuel_support)
car2.change_car_color('blue')
print(car2.color)
print(f'Car {car2.brand} nr of door is: {car2.doors}')
car2.change_car_color_user_input()
print(car2.color)

# def change_car(self):
#     print('Changing car')
#
# change_car()



# x = [1,2,3]
# x.append(4)
# print(x)