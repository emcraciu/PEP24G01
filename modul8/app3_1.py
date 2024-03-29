# salarii_input = input("Introduceti salariile separate cu virgula: ")
# salarii = [int(s) for s in salarii_input.split(",")]
#
# procent_maj = float(input("Introduceti procentul de marire: "))
#
# salarii_marite = list(map(lambda x: x * (1 + procent_maj / 100), salarii))
#
# print("Salariile marite sunt:")
# for salariu in salarii_marite:
#     print(salariu)
#
#
# # version 2
# salarii_input = input("Introduceti salariile separate cu virgula: ")
# procent_maj = (input("Introduceti procentul de marire: "))
# print("Salariile marite sunt:")
#
# print('\n'.join(map(lambda x: str(int(x) * (1 + float(procent_maj) / 100)), salarii_input.split(","))))

# version3

salarii_input = input("Introduceti salariile separate cu virgula: ")
procent_maj = (input("Introduceti procentul de marire: "))
print("Salariile marite sunt:")


def marire():
    for sal in salarii_input.split(","):
        yield str(int(sal) * (1 + float(procent_maj) / 100))


print('\n'.join(marire()))
