import random
while True:
     choices = ["rock","paper","scissors"]
     computer = random.choice(choices)
     player= None
     while player not in choices:
            player = input("rock, paper,or scissors?: ").lower()
     if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
     elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print('YOU LOSE !')
        else:#(computer == "scissors")
            print("computer: ", computer)
            print("player: ", player)
            print('YOU WIN !')
     elif player == "paper":
        if computer == "rock":
           print("computer: ", computer)
           print("player: ", player)
           print("YOU WIN !'")
        else:#(computer == "scissors")
           print("computer: ", computer)
           print("player: ", player)
           print("YOU LOSE !")
     elif player == "scissors":
        if computer == "rock":
           print("computer: ", computer)
           print("player: ", player)
           print('YOU LOSE !')
        else : #(computer == "paper")
           print("computer: ", computer)
           print("player: ", player)
           print('YOU WIN !')
     play_again = input("play again? (yes/no)").lower()
     if play_again !="yes":
        print("bye")
        break


