def calcul_x_y(x):
    y = 3 * x
    return 3 * x ** 2 - 4 * y + 4

for i in range (10, 21):
    print(f"""============= X = {i} ==================
Rezultatul functiei: {calcul_x_y(i)}""")