def functie(x):
    y = 3 * x
    return  3 * (x ** 2) - 4 * y + 4
for i in range (10, 21):
    print(f" X = {i} ".center(34,"="))
    a = functie(i)
    print(f"Rezultatul functiei: {a}")