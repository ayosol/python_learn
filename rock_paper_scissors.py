print("Rock...\nPaper...\nScissors...")
player_one = input("Player one:  ")
player_two = input("Player two:  ")

if (player_one == player_two):
    print("It's a TIE")
if (player_one == "Rock"):
    if (player_two == "Paper"):
        print("Player 2 wins")
    if (player_two == "Scissors"):
        print("Player 1 wins")
    
elif (player_one == "Paper"):
    if (player_two == "Scissors"):
        print("Player 1 wins")
    if (player_two == "Rock"):
        print("Player 2 wins")
     
elif (player_one == "Scissors"):
    if (player_two == "Scissors"):

        print("It's a tie")
    if (player_two == "Rock"):
        print("Player 2 wins")
     
else:
    print("You haven't entered a correct word")