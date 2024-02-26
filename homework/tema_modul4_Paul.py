# Ex 1
def functie(x):
    y = 3 * x
    return 3 * x ** 2 - 4 * y + 4

while True:
    x = int(input(" x = "))
    if x < 10 or x > 20:
        while True:
            x = int(input("Numarul trebuie sa fie in intervalul [10;20]"))
            if x >= 10 and x <= 20:
                break
    print(f"Rezultatul functiei: {functie(x)}")



# Ex 2
# nr = int(input("Cate carti doriti sa adaugati in biblioteca? "))
# lista_carti = []
#
# for i in range(nr):
#     dictionar = {}
#     print(f'==== Cartea {i+1} ====')
#
#     var = input('Numele cartii: ')
#     dictionar.update({'nume': var})
#
#     var = input('Numele autorului: ')
#     dictionar.update({'autor': var})
#
#     var = input('Anul publicarii: ')
#     dictionar.update({'an': var})
#
#     lista_carti.append(dictionar)
#
# print("Cartile dvs sunt: ")
# for i in lista_carti:
#     print(i)
#
# # continuare cu ex3
# an_publicatie = int(input("Anul: "))
# for i in lista_carti:
#     dictionar_nou = i
#     for j in dictionar_nou.values():
#         if str(an_publicatie) == j:
#             print(f'{dictionar_nou['nume']} a fost publicat in {dictionar_nou['an']}')
