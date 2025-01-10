#George Ibarra
#11/11/24
#Generate number 1-10 ask the kids to guess the number if they guess it right tell them they winn

#intro
import random
#guess_number = random.randint(1,10)
easy = random.randint(1,10)
meduim  = random.randint(1,50)
hard  = random.randint(1,100)
guess_number = random.randint(1,10)

def Guessing_game():
    guess_number
    input("This is a game where you will guess a number between 1 to 10 or 1 to 50 or 1 to 100")
    input("you will have three guess")
    diffculty = input("choose diffcult easy,meduim,hard")# this control the diffculty
    if diffculty == "easy":
        for i in range(3):
            guess = int(input("please guess a number between 1,10"))#this read what number you put
            if guess == guess_number:
                print("You got it right!!")
                break
            else:
                print("sorry try again ")
        print("the right answer was "+ str(meduim))#this tell u the right answer
    elif diffculty == "meduim":
        for i in range(3):#This loop give u 3 guess
            guess = int(input("please guess a number between 1,50"))
            if guess == meduim:
                print("You got it right!!")
                break
            else:
                print("sorry try again ")
        print("the right answer was "+ str(meduim))
    elif diffculty == "hard":
        for i in range(3):
            guess = int(input("please guess a number between 1,100"))
            if guess == hard:
                print("You got it right!!")
                break
            else:
                print("sorry try again ")
        print("the right answer was "+ str(hard))
#functions
#Main9
Guessing_game()

