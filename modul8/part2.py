# generators

r = range(11)
print(type(r))

result_generator = (_ for _ in range(3))
print(type(result_generator))
print(next(result_generator))
print(next(result_generator))
print(next(result_generator))
# print(next(result_generator))

result_generator = (_ for _ in range(1000000000000))
# result_generator = [_ for _ in range(1000000000000)]

def my_generator():
    for _ in range(3):
        yield _

print(type(my_generator))
print(type(my_generator()))

generator = my_generator()
# generator.__next__()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


