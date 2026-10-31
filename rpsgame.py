import random

print("Welcome to the Rock Paper Scissors game!")
options = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Choose rock, paper, or scissors: ").lower().strip()
        if player not in options:
            print("Invalid option!")

        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "paper":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (y/n): ").lower().strip()
        if play_again != "y":
            playing = False

print("Thanks for playing!")