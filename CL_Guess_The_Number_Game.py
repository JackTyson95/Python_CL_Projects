import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    while attempts < 3:
        try:
            player_guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if player_guess < number_to_guess:
            print("Too low!")
        elif player_guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number.")
            return

    print(f"Sorry, you didn't guess the number. It was {number_to_guess}.")

guess_the_number()