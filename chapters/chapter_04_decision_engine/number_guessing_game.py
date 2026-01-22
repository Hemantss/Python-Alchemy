"""
Python Alchemy

Module:
chapters.chapter_04_decision_engine.number_guessing_game

Number Guessing Game
--------------------
This program demonstrates practical use of Python control flow concepts:
- Conditional statements: if, elif, else
- Loops: while for repeated attempts
- Loop control statements: break
- Input validation and user interaction
"""

import random  # Import the random module to generate random numbers

def number_guessing_game():
    """
    A simple number guessing game where the user tries to guess
    a randomly generated number between 1 and 100.
    """

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Maximum number of attempts allowed
    max_attempts = 10
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it correctly.\n")

    # Main game loop: continues until the user guesses correctly or runs out of attempts
    while attempts < max_attempts:
        try:
            # Prompt the user for input and validate it
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 100.")
            continue  # Skip to the next iteration if input is invalid
        
        # Increment attempt count
        attempts += 1
        
        # Check the guess using conditional statements
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            # Correct guess
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break  # Exit the loop since the game is won
        
        # Inform the player about remaining attempts
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}\n")
    
    # If the user did not guess correctly after all attempts
    else:
        print(f"Game Over! The correct number was {secret_number}. Better luck next time!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
