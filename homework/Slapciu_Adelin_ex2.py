numar_carti = int(input("Introduceti numarul de carti pe care doriti sa le adaugati in biblioteca: "))

biblioteca = []

for _ in range(numar_carti):
    nume_carte = input("Nume carte: ")
    autor = input("Autor: ")
    an_publicare = input("An publicare: ")

    biblioteca.append({"Nume": nume_carte, "Autor": autor, "An Publicare": an_publicare})

# Afisare dictionare
for index, carte in enumerate(biblioteca, start=1):
    print(f"\nCarte {index}:\n{carte}")

# Cautare si afisare carti dupa anul de publicatie
an_cautat = int(input("\nIntroduceti anul pentru a afisa cartile publicate dupa acel an: "))
carti_dupa_an = [carte for carte in biblioteca if int(carte["An Publicare"]) > an_cautat]

if carti_dupa_an:
    print(f"\nCartile publicate dupa anul {an_cautat} sunt:\n")
    for index, carte in enumerate(carti_dupa_an, start=1):
        print(f"Carte {index}:\n{carte}")
else:
    print(f"\nNu exista carti publicate dupa anul {an_cautat}.")