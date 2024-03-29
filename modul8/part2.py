# # generators
#
# r = range(11)
# print(type(r))
#
# result_generator = (_ for _ in range(3))
# print(type(result_generator))
# print(next(result_generator))
# print(next(result_generator))
# print(next(result_generator))
# # print(next(result_generator))
#
# result_generator = (_ for _ in range(1000000000000))
# # result_generator = [_ for _ in range(1000000000000)]
#
# def my_generator():
#     for _ in range(3):
#         yield _
#
# print(type(my_generator))
# print(type(my_generator()))
#
# generator = my_generator()
# # generator.__next__()
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# file operations

result = open('modul8/example.py', 'rt')
output = result.read()
print(output)
print(type(output))
# print(result.readlines())
result.flush() # write to disk
result.close() # no more write operation can be done

with open('modul8/example.py', 'rt') as file:
    output = file.readlines()
print(type(output))

with open('modul8/test.txt', 'wt') as file:
    file.write("\n # comment")

with open('modul8/test.txt', 'rb') as file:
    output = file.read()

print(type(output))
print(output)

with open('modul8/Cap8_Lab1.pdf', 'rb') as file:
    output = file.read()
print(output)