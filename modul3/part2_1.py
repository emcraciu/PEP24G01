# lists

result = '5,10'.split(',')
print(type(result))
print(result)

my_str = 'hello'
print(id(my_str))
print(id(my_str.capitalize()))

my_list = []
print(my_list, 'before append')
print(id(my_list), 'in memory')
my_list.append(1)
print(my_list, 'after append')
print(id(my_list), 'in memory')
my_list.pop()
print(my_list, 'after pop')
print(id(my_list), 'in memory')

# id keyword
my_var1 = f"test 1 {10-9}".capitalize()
print(id(my_var1))
my_var2 = "Test 1 1"
print(id(my_var2))
print(my_var1 is my_var2)
print(my_var1 == my_var2)

# for with lists
print(80 * '#')

print()

new_list = [1, '5', True, None, [1,2,3]]
print(id(new_list) == id(new_list[::]))
print(new_list == new_list[::])
print(new_list, new_list[::])

for obj in new_list[::]:
    print(obj)
    new_list.pop(2)

