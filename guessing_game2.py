import random

random_number = random.randint(1, 10)

while True:
    user_guess = int(input("Guess a number between 1 and 10:\n"))
    if (user_guess < random_number):
        print("Too Low, Try again!")
    elif (user_guess > random_number):
        print("Too High, Try again!")
    else:
        print("You guessed it right! YOU WON!")
        play_again = input("Do you want to play again? (y/n):  ")
        if play_again == "y":
            random_number = random.randint(1, 10)
            user_guess = None
        else:
            print("Thank you for playing!")
            break
