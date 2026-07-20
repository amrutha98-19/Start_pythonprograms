#Number guessing game
import random

number=random.randint(1,50)  # Generate a random number between 1 and 50

attempt=0 # Initialize the attempt counter
print("Welcome to the number guessing game:")
print("Guess a number between 1 and 50")
while True:                        # Repeat until the user guesses the correct number
    guess = int(input("Enter your guess: "))  # Get the user's guess
  
    attempt+=1                                # Increase the attempt count
    if guess<number:                          # Check if the guess is smaller than the secret number
        print("Too low,try again")
    elif guess>number:                        # Check if the guess is greator than the secret number
        print("Too high,try again")
    else:                                     # If the guess is correct
        print(f"congratulations !you guessed it in {attempt} attempts")
        break
