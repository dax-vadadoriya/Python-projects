import random

secret_number = random.randint(1, 10)

guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        print("You got it in", attempts, "guesses.")
