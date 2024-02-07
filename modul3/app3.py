print('1. Cappuccino ...4 lei ')
print('2. Espresso ...3.5 lei ')

option = int(input('Ce optiune alegeti? [1,2]: '))
coin = int(input('Introduceti o bacnota [5,10]: '))

# if option == 1 and coin == 5:
#     rest = 5 - 4
# elif option == 1 and coin == 10:
#     rest = 10 - 4
# elif option == 2 and coin == 5:
#     rest = 5 - 3.5
# elif option == 2 and coin == 10:
#     rest = 10 - 3.5
# else:
#     print('invalid Product')

# solution for for loop
if option == 1:
    product_value = 4
elif option == 2:
    product_value = 3.5

for possible_coin in '5,10'.split(','):
    if coin == int(possible_coin):
        break
else:
    print('not a valid coin')

print(f'Veti primi restul de {float(possible_coin) - float(product_value)} lei.')