from termcolor import colored
import random
from playsound import playsound

# Define the ASCII art for the Rock, Paper, Scissors game
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

# Store the game images in a list
game_images = [rock, paper, scissors]

# Initialize the round counter
count = 1
# Start the game loop
while (count < 11):
    # Prompt the user for their choice and store it in a variable
    user_choice = int(input('What do you choose? Type "0" for Rock, "1" for Paper or "2" for Scissors.\n'))

    # Generate the computer's choice
    computer_choice = random.randint(0, 2)

    # Print the computer's choice
    print("Computer chose:")
    print(colored(game_images[computer_choice], 'green'))

    # Check if the user's choice is valid
    if user_choice >= 3 or user_choice < 0: 
        print(colored("You typed an invalid number, you lose!", 'red'))
    # Check if the user wins
    elif user_choice == 0 and computer_choice == 2:
        print(colored("You win!", 'green'))
        playsound('you_win.mp3')
    # Check if the user loses
    elif computer_choice == 0 and user_choice == 2:
        print(colored("You lose", 'red'))
        playsound('sorry_try_again.mp3')
    elif computer_choice > user_choice:
        print(colored("You lose", 'red'))
        playsound('sorry_try_again.mp3')
    elif user_choice > computer_choice:
        print(colored("You win!", 'green'))
        playsound('you_win.mp3')
    # Check if it's a draw
    elif computer_choice == user_choice:
        print(colored("It's a draw", 'yellow'))
        playsound('Draw.mp3')
    # Increase the round counter
    count += 1