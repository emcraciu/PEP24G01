import random

while True:
    nume_p = input('banga nume: ')
    optiuni = {'p': 'piatra', 'f': 'foarfeca', 'h': 'hartie', 'q': 'renunta'}
    optiuni_afisate = str()

    for key, value in optiuni.items():
        optiuni_afisate += f'{key}, ({value})'

    optiune_player = input(f'Alege optiune: [{optiuni_afisate}]')
    optiuni_server = list(optiuni.keys())
    optiuni_server.remove('q')

    optiune_server = random.choice(optiuni_server)
    print(f'> Server: {optiuni[optiune_server]}')
    print(f'> {nume_p}: {optiuni[optiune_player]}')

    if optiune_server == "p" and optiune_player == "f":
        print("Serverul a castigat")
        break
    elif optiune_server == "h" and optiune_player == "p":
        print("Serverul a castigat")
        break
    elif optiune_server == "f" and optiune_player == "h":
        print("Serverul a castigat")
        break
    elif optiune_server == optiune_player:
        print("Egalitate")

    else:
        print(nume_p, "A castigat")
        break