#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Oct. 18, 2022
# Number guessing program, this random numbers being generated.
import random


def main():

    # Spacer
    print("")

    # Obtain user guess for the correct answer
    print("This is a number guessing game, choose a number between 1-10")
    guess_answer = input("Insert your guess (0 - 9): ")

    # Spacer
    print("")

    # Generates the random number
    guess_generated = random.randint(0, 9)

    try:
        guess_answer = int(guess_answer)
        # Answer checking, seeing if user input is correct
        if guess_answer == random.randint:
            print("Your guess is correct!")

        else:
            print(
                f"Your answer is incorrect! the correct answer was: {guess_generated}"
            )

    except Exception:
        print("Enter an integer(0-9) only!")


if "__main__" == __name__:
    main()
