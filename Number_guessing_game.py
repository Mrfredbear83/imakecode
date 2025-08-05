import random

def number_guessing_game():
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100") 
    
    number_to_guess = random.randint(1, 100)  # Fixed: randint
    guess = None 
    attempts = 0

    while guess != number_to_guess: 
        try: 
            guess = int(input("Take a guess: "))
            attempts += 1 
            
            if guess < number_to_guess:
                print("Too low! Try again or you're just not trying.")
            elif guess > number_to_guess: 
                print("Too high!")
            else: 
                print(f"Congratulations! You guessed the number in {attempts} tries.")
        except ValueError: 
            print("Please enter a valid number.")

# Call the function to start the game
number_guessing_game()
