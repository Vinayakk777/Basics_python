import random

# ASCII art for moves
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
---'    ____)____
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

# Map text input to ASCII
moves = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# User choice
user_input = input("What do you choose rock, paper or scissors? ").lower()

if user_input not in moves:
    print("Invalid choice! Please choose rock, paper or scissors.")
else:
    user_choice = moves[user_input]
    computer_choice = random.choice(list(moves.values()))

    # Print choices
    print("\nYou chose:")
    print(user_choice)
    print("Computer chose:")
    print(computer_choice)

    # Compare results directly with ASCII
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == rock and computer_choice == scissors) or \
         (user_choice == paper and computer_choice == rock) or \
         (user_choice == scissors and computer_choice == paper):
        print("You win! 🎉")
    else:
        print("You lose! 😢")
