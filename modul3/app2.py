number = int(input('give number:'))

print(range(0, number, 2))
print(type(range(number)))

for count in range(0, number, 2):
    print(count)

print(f'last value: {count}') # can be undefined