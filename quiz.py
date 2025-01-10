import random

user= input("please enter username")
print("welcome " + user + " this game will quiz you on your multiplication")
#ans=random.randint()

def generate_muliplication_problems():
    length = int(input("how many question do you want:"))
    score = 0
    for i in range(length):
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print(str(num1) + " times " + str(num2) )
        ans = int(input("please enter an answer:"))
        if ans == (num1 * num2):
            score = score + 1
            print("You got it right"  + " your points is " + str(score ))

        else:
            print("you got it wrong")
    print("you got " + str(score) + "/" + str(length) + " right")



generate_muliplication_problems()
