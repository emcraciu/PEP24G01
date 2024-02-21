def calcul_x_y(x):
    y = 3 * x
    return 3 * x ** 2 - 4 * y + 4

for numar_interval in range (10 , 21):
    print(f"{13 * '='} X = {numar_interval} {13 * '='}")
    print(f"Rezultatul functiei: {calcul_x_y(numar_interval)}")

