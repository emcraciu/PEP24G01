def calculate_function_value(x):
    y = 3 * x
    result = 3 * x**2 - 4 * y + 4
    return result

def main():
    start = 10
    end = 20

    print("============= Calculating Values =============")
    for x in range(start, end+1):
        result = calculate_function_value(x)
        print("============= X =", x, "==================")
        print("Rezultatul functiei:", result)

if __name__ == "__main__":
    main()