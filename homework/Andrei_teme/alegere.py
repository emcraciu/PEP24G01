def alegere_nr_utilizator():
    numere = []
    while True:
        numar = input("Introduceti un numar (Dupa ce ati introdus 6 numere, apasati tasta Q): ")
        if len(numere) == 6:
            break
        try:
            numar = int(numar)
        except ValueError:
            print('Number not valid: ')
            continue
        if 0 < numar <= 49:
            numere.append(numar)

    return numere

