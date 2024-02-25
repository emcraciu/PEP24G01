import random


def get_6_numbers_from_user(user_numbers: list):
    """Returns a list of 6 numbers got from the user"""
    count = 1
    while count <= 6:
        try:
            user_choice = int(input("Choose a number from 1 to 49: "))
        except ValueError:
            print("Your input must be a valid integer number!")
            continue
        else:
            if 1 <= user_choice <= 49:
                user_numbers.append(user_choice)
                count += 1
            else:
                print("Number not in range! Please...")
                continue
    return user_numbers


def generate_list_of_random_numbers():
    """Returns a list of 6 unique random integer numbers"""
    set_of_numbers = set()
    while len(set_of_numbers) < 6:
        set_of_numbers.add(random.randint(1, 49))
    return list(set_of_numbers)


def compare_numbers(user_nums, nums_drawn):
    """Returns how many numbers the user have guessed by comparing both lists."""
    numbers_guessed = 0
    for choice in user_nums:
        if choice in nums_drawn:
            numbers_guessed += 1
    return numbers_guessed


def main():
    print("Let's play 6/49. You have to choose 6 numbers between 1 and 49.")
    user_choices = get_6_numbers_from_user([])
    numbers_drawn = generate_list_of_random_numbers()
    guesses = compare_numbers(user_choices, numbers_drawn)
    print(f"Your numbers: {user_choices} \nNumbers drawn: {numbers_drawn}")
    if 1 <= guesses <= 3:
        print("Congratulations! You've won 50 lei!")
    elif 4 <= guesses <= 5:
        print("Congratulations! You've won 500 lei!")
    elif guesses == 6:
        print("Congratulations! You've won 1500 lei!")
    else:
        print("You didn't guess any number! Better luck next time!")


if __name__ == "__main__":
    main()





