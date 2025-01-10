#George Ibarra 1/6/2025
import random
#int


#Player choice
def rps():
    while True:
        print("Welcome to Rock, Paper, Scissors")
        print("Please select one of these three options")
        move = input("Selection: ")
        #computer choice
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("computer chose rock")
        elif computer == 2:
            computer = "paper"
            print("computer chose paper")
        else:
            computer = "scissor"
            print("computer chose scissor")

        #winner
        if computer == "rock" and move == "rock":
            print("tie")
        elif computer == "paper" and move == "paper":
            print("tie")
        elif computer == "scissors" and move == "scissors":
            print("tie")
        elif computer == "scissors" and move == "paper":
            print("computer wins")
        elif computer == "paper" and move == "rock":
            print("computer wins")
        elif computer == "rock" and move == "scissor":
            print("computer wins")
        elif computer == "rock" and move == "paper":
            print("player wins")
        elif computer == "paper" and move == "scissor":
            print("player wins")
        else:
            computer == "scissor" and move == "rock"
            print("player wins")
        playagain = input("would you like to play again?")
        if playagain == "no":
            break
#functions

#Main
rps()
