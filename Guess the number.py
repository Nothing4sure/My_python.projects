import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guesses_taken = 0
    
    while True:
        try:
            # Ask the player to guess the number
            guess = int(input("Enter your guess: "))
            guesses_taken += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {guesses_taken} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Start the game
if __name__ == "__main__":
    start_game()
