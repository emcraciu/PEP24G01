#ex.1
def fx_and_y():
    for x in range(10, 21):
        y = 3 * x
        equation_result = 3 * (x**2) - 4 * y + 4
        print(f"============= x = {x} =============")
        print(f"Rezultatul functiei : {equation_result}")

fx_and_y()


#ex2
nr = input("Cati carti doriti sa adaugati la lista? ")
lista_carti = []

for i in range(int(nr)):
    print(f"======== Cartea {i + 1} ========")
    carte = {}
    carte["nume"] = input("Numele cartii: ")
    carte["autor"] = input("Numele autorului: ")
    carte["an"] = input("Anul publicarii: ")
    lista_carti.append(carte)

print("Cartile dvs sunt:")
for i, carte in enumerate(lista_carti, 1):
    print(f"{i}. {carte}")


#ex3

nr = input("Cati carti doriti sa adaugati la lista? ")
lista_carti = []

for i in range(int(nr)):
    print(f"======== Cartea {i + 1} ========")
    carte = {}
    carte["nume"] = input("Numele cartii: ")
    carte["autor"] = input("Numele autorului: ")
    carte["an"] = input("Anul publicarii: ")
    lista_carti.append(carte)

print("Cartile dvs sunt:")
for i, carte in enumerate(lista_carti, 1):
    print(f"{i}. {carte}")

an_aparitie = input("Introduceti un an: ")
print(f"Anul: {an_aparitie}")
for carte in lista_carti:
    if int(carte["an"]) > int(an_aparitie):
        print(f"{carte['nume']} a fost publicat dupa {an_aparitie}.")