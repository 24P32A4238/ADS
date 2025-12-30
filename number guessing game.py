import random

number = random.randint(1, 50)

while True:
    guess = int(input("Guess the number (1-50): "))
    if guess == number:
        print("Correct! You won 🎉")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")