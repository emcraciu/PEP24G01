duplicated = [1, 3, 5, 7, 7, 7, 7, 7, 9, 3]  # remove duplicates

new_list = []
for number in duplicated[::]:
    if number not in new_list:
        new_list.append(number)
    else:
        duplicated.remove(number)
        print(number, 'is duplicate')

duplicated.sort()
print(new_list)
print(duplicated)