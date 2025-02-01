"""A number-guessing game."""

'''This program greets a player, asks the player to guess a number between 1-100, and tells the player if the number is too low, too high, or correct, as well the number of guesses.'''

import random

def guess_random_number():
    player_name = input("Hello, what is your name?")
    random_num = random.randint(1,100)
    guesses = 0
    
    while True:
        guess_num = int(input(f"{player_name}, guess a number between 1 and 100."))
        
        guesses += 1

        if guess_num < 1 or guess_num > 100:
            print("Oops, your number is out of range! Try again!")

        # try:
            # guess_num
        # except ValueError:
            # print("Oops, that was not a number! Try again!")

        if guess_num == random_num:
            print(f"Congratulations {player_name}, you guessed my number in {guesses} tries!") 
            break

        else:

            if guess_num < random_num:
                print("Your guess is too low!")

            elif guess_num > random_num:
                print("Your guess is too high.")
            

    return player_name, guess_num, random_num
    

guess_random_number()

