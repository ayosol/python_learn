import random

random_number = random.randint(1, 10)

user_guess = int(input("Guess a number between 1 and 10:\n"))

while user_guess != random_number:
    if (user_guess < random_number):
        print("Too Low, Try again!")
    elif (user_guess > random_number):
        print("Too High, Try again!")
    else:
        print("You guessed it right! YOU WON!")
    user_guess = int(input("Guess Again: \n"))
    #Do you want to keep playing? (y/n):
    # if user_choice == "n":
    #     break
    # else:
    #     user_guess = int(input("Guess a number:\n")) 
if (user_guess == random_number):
    print("You guessed it right! YOU WON!")
