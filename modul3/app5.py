my_list = ["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8, ['a']]
for obj in my_list:
    print(f'Tipul obiectului {obj} este {type(obj)}')
    if type(obj) == list:
        for inner_obj in obj:
            print(f'Tipul obiectului {inner_obj} este {type(inner_obj)}')