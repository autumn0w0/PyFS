import random

target = random.randint(1, 100)
print("Welcome to the Guess the Number Game!")

while True:
    guess = int(input("Enter your guess (between 1 and 100): "))

    if (guess== target):
        print("Congratulations! You've guessed the number!")
        break
    elif guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")
    else:
        print("the number is out of rangle! Please enter a number between 1 and 100.")
        break
