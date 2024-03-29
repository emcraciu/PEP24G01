import random


def alegere_nr_random():
    lista_nr = []
    for i in range(1, 50):
        lista_nr.append(i)

    lista_nr_random = []
    while True:
        numar = random.choice(lista_nr)
        if len(lista_nr_random) == 6:
            break
        try:
            numar = int(numar)
        except ValueError:
            print('Number not valid: ')
            continue
        lista_nr_random.append(numar)

    return lista_nr_random


