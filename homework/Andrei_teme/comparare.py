# functie care va compara numerele extrase cu cele alese (comparare liste)

def comparare_liste_nr(x, y):
    m = 0
    for i in x:
        for j in y:
            if i == j:
                m = m + 1
            else:
                continue
    if 0 < m <= 3:
        return print(f' Ai ghicit {m} nr, ai castigat 50 lei')
    elif m == 4 or m == 5:
        return print(f' Ai ghicit {m} nr, ai castigat 500 lei')
    elif m == 6:
        return print(f' Ai ghicit {m} nr, ai castigat 1500 lei')
    else:
        return print('Nu ai ghicit nici un numar')
