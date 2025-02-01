"""A number-guessing game."""

'''This program greets a player, asks the player to guess a number between 1-100,
and tells the player if the number is too low, too high, or correct.'''

import random

def guess_random_number():
    player_name = input("Hello, what is your name?")
    random_num = random.randint(1,100)
    guesses = 0
    
    while True:
        guess_num = int(input(f"{player_name}, guess a number between 1 and 100."))

        guesses += 1

        if guess_num == random_num:
            print(f"{player_name}, you guessed my number correctly in {guesses} tries!") 
            break

        else:

            if guess_num < random_num:
                print("Your guess is too low!")

            elif guess_num > random_num:
                print("Your guess is too high.")
            

    return player_name, guess_num, random_num
    

guess_random_number()

