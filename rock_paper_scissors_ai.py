from random import randint

player_wins = 0
computer_wins = 0

while True:
    if player_wins == 5 or computer_wins == 5:
            break
    print(" ")
    print("rock...\npaper...\nscissors...")
    player = input("What's your game, player?\n").lower()
    rand_num = randint(0, 2)
    if (rand_num == 0): #Computer plays rock    
        computer = "rock"
    elif (rand_num == 1): #Computer plays paper
        computer = "paper"
    else: #Computer plays scissors
        computer = "scissors"
    print(f"Computer played {computer}")

    if (player != None):
        if (player == computer):
            print("It's a TIE")
        if (player == "rock"):
            if (computer == "paper"):
                print("Computer wins")
                computer_wins += 1
            if (computer == "scissors"):
                print("Human wins")
                player_wins += 1
            
        elif (player == "paper"):
            if (computer == "scissors"):
                print("Computer wins")
                computer_wins += 1
            if (computer == "rock"):
                print("Human wins")
                player_wins += 1
            
        elif (player == "scissors"):
            if (computer == "paper"):
                print("Human wins")
                player_wins += 1
            if (computer == "rock"):
                print("Computer wins")
                computer_wins += 1
            
        else:
            print("You haven't entered a correct word")

if computer_wins == 5 or player_wins == 5:
    print(f"Thanks for playing the game, the score is \nComputer: {computer_wins} \nPlayer: {player_wins}")
        