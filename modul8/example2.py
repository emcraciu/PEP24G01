# for i in range(10):
#     user_input = input('give letter:')
#     print(user_input)

def get_letter_from_user():
    for i in range(10):
        user_input = input('give letter/letters:')
        for letter in user_input:
            yield letter

user_letter = get_letter_from_user()

for letter in user_letter:
    print(letter)

# print(next(user_letter))
# print(next(user_letter))
# print(next(user_letter))
