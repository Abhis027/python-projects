import random

# Generate a random 3-digit number with unique digits
def generate_number():
    digits = random.sample(range(1, 10), 3)
    return digits[0] * 100 + digits[1] * 10 + digits[2]

# Check the guess against the secret number and return the result
def check_guess(secret, guess):
    pico = fermi = 0
    for i in range(3):
        secret_digit = (secret // 10**i) % 10
        guess_digit = (guess // 10**i) % 10
        if guess_digit == secret_digit:
            fermi += 1
        elif guess_digit in [secret // 10**j % 10 for j in range(3)]:
            pico += 1
    return (fermi, pico)

# Main game loop
def play_game():
    print("Welcome to Pico Fermi!")
    secret = generate_number()
    attempts = 0
    while True:
        guess = input("Enter your guess (a 3-digit number with unique digits): ")
        if len(guess) != 3 or not guess.isdigit():
            print("Invalid guess. Please enter a 3-digit number with unique digits.")
            continue
        guess = int(guess)
        attempts += 1
        result = check_guess(secret, guess)
        print(f"{result[0]} Fermi, {result[1]} Pico")
        if result[0] == 3:
            print(f"Congratulations! You guessed the secret number in {attempts} attempts!")
            break

play_game()
