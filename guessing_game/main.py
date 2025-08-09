import random

def choose_difficulty():
    print("🎯 Welcome to the Number Guessing Game!\n")
    print("Select Difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)\n")
    
    difficulty_setting = {
        1: ("Easy", 1, 10, 5),
        2: ("Medium", 1, 50, 7),
        3: ("Hard", 1, 100, 10)
    }
    
    choice = int(input("Enter your choice: "))
    
    if choice in difficulty_setting:
        level, low, high, attempts = difficulty_setting[choice]
        print(f'\nYou selected {level} mode.')
        print(f"\nYou'll have to guess a number between {low} and {high} in {attempts} attempts.")
        return (low, high, attempts)
    else:
        print("Invalid choice. Please select a valid difficulty level.")
        return choose_difficulty()
    
def play_game(low, high, max_attempts):
    secret_number = random.randint(low, high)
    attempts_left = max_attempts
    
    while attempts_left > 0:
        try:
            guess = int(input(f"\nGuess the number ({attempts_left} attempts left): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if guess < low or guess > high:
            print(f"Your guess is out of bounds! Please guess a number between {low} and {high}.")
            continue
        
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly! ")
            print(f"✅ You took {max_attempts - attempts_left + 1} attempt(s).")
            return
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
        attempts_left -= 1
        
    print(f"\n💀 You've run out of attempts! The correct number was {secret_number}. Better luck next time!")
    
    
def main():
    result = choose_difficulty()
    if result:
        low, high, max_attempts = result
        play_game(low, high, max_attempts)
        
if __name__ == "__main__":
    main()