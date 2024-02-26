nr = input("Cate carti doriti sa adaugati in biblioteca?")
lista_carti = []

for i in range(int(nr)):
    print(f" Cartea {i+1} ".center(28, "="))
    numele = input("Numele cartii: ")
    autorul = input("Numele autorului: ")
    anul = input("Anul publicarii: ")
    carte = {'nume': numele, 'autor': autorul, 'an': anul}
    lista_carti.append(carte)

print("Cartile dvs sunt: ")
for carte in lista_carti:
    print(carte)

an_publicatie = input("Anul: ")
for carte in lista_carti:
    if(int(an_publicatie) < int(carte['an'])):
        print(f"Cartea {carte['nume']} a fost publicata dupa anul {an_publicatie}")
