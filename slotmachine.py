#George ibarra 3 slot machine
#init
import random
win = 0 #Global variable
symbols = [" 7 " ," ♣ ", " ♣ " ," ❤ ", " ❤ "]
credits = 100 #gobalal varibale
import time
#functions
#
def slots(): #This is our function for our slot machine game
    global credits #This is our global variable that will allow our "credits" variable to retain its value througout our entire code
    global win #^^^Same applies, excpet it will retain the players wins throutout the game
    print("Hello!, Welcome to our Slot Machine Game")
    print("You are starting with 100 credits ")
    print("""Here are a few rules for you:
    1. Each spin is worth 10 credits
    2. If you spin three matching symbols, you win 30 credits
    3. If you spin three '7' symbols, congrats!, you hit the jackpot
    4. If you spin no matching symbols, you do not recieve any credits""")
    while True: #This is an infinite loop for our slot machie game to allow players to keep playing until they decide to quit or run out of credits.
        if credits == 0:
            break
        print("would you like to spin or quit?")
        spin = input("yes or no?:")
        if spin == "yes":
            roll = ""
            for i in range(3): #This loop, cycles a roll 3 times to create a pause inbetween the spin
                roll = roll + random.choice(symbols)
            print("slot 1 spinning...") #Time sleep generates a pause to induce a feeling of suspense for our players
            time.sleep(2)
            print("slot 2 spinning...")
            time.sleep(2)
            print("slot 3 spinning...")
            time.sleep(2)
            print(roll)
            if roll == "♠♠♠":
                print("You spinned a MATCH!")
                credits = credits - 10
                credits = credits + 30
                print("Your total credit score is: " + str(credits))
            if roll == "777":
                print("YOU SPINNED THE JACK POT!!! CONGRATS")
                credits = credits - 10
                credits = credits + 100
                print("Your total credit score is: " + str(credits))
            if roll == "❤ ❤ ❤ ":
                print("You spinned a MATCH!")
                credits = credits - 10
                credits = credits + 30
                print("Your total credit score is: " + str(credits))
            if roll == "❤ ❤ 7 ":
                print("You spinned a partial MATCH!")
                credits = credits - 10
                credits = credits + 15
                print("Your total credit score is: " + str(credits))
            if roll == "❤ ❤ ♠ ":
                print("You spinned a partial MATCH!")
                credits = credits - 10
                credits = credits + 15
                print("Your total credit score is: " + str(credits))
            if roll == " 7 7 ❤ ":
                print("You spinned a partial MATCH!")
                credits = credits - 10
                credits = credits + 15
                print("Your total credit score is: " + str(credits))
            if roll == "7 7 ♠ ":
                print("You spinned a partial MATCH!")
                credits = credits - 10
                credits = credits + 15
                print("Your total credit score is: " + str(credits))
            if roll == "♠ ♠ 7":
                print("You spinned a partial MATCH!")
                credits = credits - 10
                credits = credits + 15
                print("Your total credit score is: " + str(credits))
            if roll == "♠ ♠ ❤":
                print("You spinned a partial MATCH!")
                credits = credits - 10
                credits = credits + 15
                print("Your total credit score is: " + str(credits))
            else:
                credits = credits - 10
                print("Aw no! You did not spin any matches")
                print("You did not gain any credits this round. Your total credit score is: " + str(credits))
            if roll == "777" or roll == "♠♠♠" or roll == "❤ ❤ ❤": #This will keep track of
                win = win + 1
                print("Congrats, you currently have " + str(win) + " wins")
        else:
            print("Thank You for Playing, I Hope You Won BIG!!!")
            break

#main
#1.Introduction
#2.player decides to spin and quit
#3.if spin randomly pull three symbols
#tip you must remeber these three\
#symbols using variable!!!!
#4.determine outcome using if,elif,else
#print(symbols)
slots()
