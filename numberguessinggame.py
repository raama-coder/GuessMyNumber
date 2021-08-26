import random
number = random.randint(1, 9)
guess = int(input("Guess a number between 1 and 9: "))
chances = 1
while chances < 5:
    if guess > number:
        print(guess, "was too high. Try again")
    if guess < number:
        print(guess, "was too low. Try again")
    guess = int(input("Guess again:  "))
    chances=chances+1

if chances==5:
    print("No more guessing,",number, "is my number!!!")