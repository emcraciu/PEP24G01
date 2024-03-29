def user_provided_word():
    user_input = input("Type a word: ")
    for letter in enumerate(user_input):
        yield letter


with open("result.txt", "w") as file:
    for letter in user_provided_word():
        file.write(f"{letter[0]}: {letter[1]} \n")

with open("result.txt", "r") as file:
    lines = file.readlines()

result = {}
for line in lines:
    key, value = line.split(':')
    result.update({key: value.strip()})
print(result)
