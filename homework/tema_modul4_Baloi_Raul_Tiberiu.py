# Ex.1
# def calcule():
#     for x in range(10, 21):
#         y = 3 * x
#         rezultat = 3 * x ** 2 - 4 * y + 4
#         print("x = ", x)
#         print("Rezutatul functie", rezultat)
# calcule()

# Ex.2 + 3
carti = input("Cate carti doresti sa adaugi : ")

lista_carti = []
for i in range(int(carti)):
    print("Cartea", i + 1)
    nume = input("Numele Cartii: ")
    autor = input("Autorul: ")
    an = input("Anul p ublicarii: ")
    carte = {"nume": nume, "autor": autor, "an": an}
    lista_carti.append(carte)
print("Cartile sunt :")
for carte in lista_carti:
    print(carte)

cauta_an = int(input("Introduceti un an :"))
print("Anul:", cauta_an)
for carte in lista_carti:
    if an >= str(cauta_an):
        print("carte", nume, "publicat in:", cauta_an)
