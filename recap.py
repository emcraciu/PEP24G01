# for i in range(10):
#     print(i)
#
# print(i)


# check one of the following chars are in the string

# my_str = "abcd1232"
# check_chars = ['5', '!']
# for char_ in check_chars:
#     if char_ in my_str:
#         print(f'success found: {char_}')
#         break
# else:
#     print(f'Could not find any char in: {check_chars}')


my_str = "abcd1232"
check_chars = range(10)
for char_ in check_chars:
    if str(char_) in my_str:
        print(f'success found: {char_}')
        break
else:
    print(f'Could not find any char in: {check_chars}')