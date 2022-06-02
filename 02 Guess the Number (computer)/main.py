# The computer selects a random number.
# We have to guess that number
# The computer will tell us when we're wrong or correct

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        if guess < random_number:
            print('Sorry, guess again. Too low!')
        elif guess > random_number:
            print('Sorry, guess again. Too high!')

    print(f'Yay, Congrats! You have guessed the number {random_number} correctly!!')

guess(10)
