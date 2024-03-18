# lambda functions
# a = 10
def name_function(a, b):
    return a + b


print(name_function(10, 20))

name_function = lambda a, b: a + b

print(name_function(10, 20))

# f = a*x + 1
x = 10
def  check_all_a(func_a):
    for a in range(1, 101):
        print(func_a(x, a))

check_all_a(lambda x, a: a * x + 1)

print('#'*80)
list_of_functions = []
for a in range(1, 101):
    list_of_functions.append(lambda x: a * x + 1)

for func in list_of_functions:
    print(func(x))


# map function
# map to ascii
result = map(lambda char: ord(char), 'Hello World')

# We can cast to list
new_result = list(result)
print(new_result)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

