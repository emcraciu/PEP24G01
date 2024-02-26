import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = {"rock": rock, "paper": paper, "scissors": scissors}

player_name = input("Player name: ")

for key, value in choices.items():
    print_choices = "".join(key + value)
    print(print_choices)


combinations = {("rock", "paper"): False, ("paper", "rock"): True,
                ("rock", "scissors"): True, ("scissors", "rock"): False,
                ("paper", "scissors"): False, ("scissors", "paper"): True}

game_on = True

while game_on:
    player_choice = input("Type an option rock/paper/scissors or q if you want to quit: ").lower()
    if player_choice == "q":
        game_on = False
        print("Bye bye!")
        break
    elif player_choice not in choices.keys():
        player_choice = input("Invalid option. Type rock/paper/scissors or q if you want to quit: ").lower()
    else:
        pc_choice = random.choice(list(choices.keys()))
        print(f"{player_name}'s choice:\n", choices[player_choice])
        print("Computer choice:\n", choices[pc_choice])
        if player_choice == pc_choice:
            print("Draw!")
            continue
        result = combinations[(player_choice, pc_choice)]
        if result:
            print(f"{player_name} won!")
            break
        else:
            print("Server won! You lose!")
            break