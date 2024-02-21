# Exercise 1

for x in range(10, 21):
    y = 3 * x
    result = 3 * x ** 2 - 4 * y + 4
    print(f'========{x}=======')
    print(f'Rezultatul functie este : {result}')

# Exercise 2 + 3

nr_carti = int(input("Cati carti doriti sa adaugati in biblioteca? "))
lista_carti = []

for i in range(1, nr_carti + 1):
    print(f'=====Cartea {i} =====')
    nume_carte = input("Numele cartii :")
    autor_carte = input('Autorul este :')
    anul_publicarii = input("Anul publicari este :")
    info_carti = {'Nume': nume_carte, 'Autor': autor_carte, 'Anul': anul_publicarii}
    lista_carti.append(info_carti)

print('Cartile dumneavoastra sunt : ')
for info in lista_carti:
    print(info)

an_cautat = int(input('Alege anul publicarii :'))
print(f'Anul publicari ales este : {an_cautat}')


for an in lista_carti:
    if int(an['Anul']) > an_cautat:
        print(an)

