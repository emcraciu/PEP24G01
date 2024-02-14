# def add_(x, y):
#     print(locals())
#     return x + y
#     # print(x) # will never execute
#
# # print(x) # not available outside function
#
# result = add_(3, 4)
# print(result)

# local variable
# def factorial(x):
#     result = 1
#     for i in range(1, x+1):
#         result *= i
#     return result
#
# result = factorial(4)
# print(result)

# global variable
result = 1
def factorial(x):
    global result
    for i in range(1, x+1):
        result *= i

factorial(4)
# factorial(4) # calling function one more time starts from 24
print(result)

def gauss(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
print(gauss(100))

# sum from 1/1 to 1/n
def sumafractii(x):
    suma = 0
    for i in range(1, x+1):
        suma += 1/i
    return suma

x = int(input())
print(sumafractii(x))