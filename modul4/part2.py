# dictionary


my_dict = {'one': 1, 'two': 2, 'true': True}

print(my_dict)
print(type(my_dict))

my_dict = dict(one=1, two=2)
print(my_dict)


# iter dict

for element in my_dict:  # same as my_dict.keys()
    print('dict key:', element)

for element in my_dict.values():
    print('dict values:', element)

for element in my_dict.items():
    print('dict values:', element)

for key, value in my_dict.items():
    print('dict values:', key, value)

# get key/ value

value = my_dict['one']
print(f'returned value is: {value}')
my_dict['one'] = '''one'''
value = my_dict['one']
print(f'returned value is: {value}')

# test = {[1]: 'test'}
# print(test)

# 'x'.__hash__()
# [].__hash__()

# Tuple

a, b = (1, 2)  # same as 1, 2
print(a)
print(b)
a, b = b, a
print(a)
print(b)
## not like this
# a=b
# b=a
# print(a)
# print(b)