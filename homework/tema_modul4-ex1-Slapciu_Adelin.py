def calcul_valoare(x):
    y = 3 * x
    return 3 * x**2 - 4 * y + 4

#Calculul in intervalul 10, 20
for x in range(10, 21):
    rezultat = calcul_valoare(x)
    print(f'Pentru x = {x} si y = {3 * x}, valoarea lui x este: {rezultat}')