# for

# my_str = 'Hello World'
# my_int = 100
#
# for letter in my_str:
#     print(letter)
#
# # for number in my_int:  # int is not iterable
# #     print(number)
#
# for number in range(my_int):
#     print(number)
#
# user_input = input('give string: ')  # search for x
#
# for letter in user_input:
#     print(letter)
#     if letter == 'x':
#         print('found x')
#         break
# else:
#     print('could not find "x"')


user_input = input('give string: ')  # do not print x

for letter in user_input:
    if letter == 'x':
        continue
    print(letter)
else:
    print('x was not printed')