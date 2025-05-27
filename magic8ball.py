#George ibsarra
#1/24/2025
import random
import time
respones = ["Yes", "Most Defientely", "of course", "sure", "No", "Hell nah", "youre crazy", "Defeiently not", "when pigs fly", "is the sky blue", "maybe", "try again", "I am not your therapist", "ask your mom", "you tell me"]

#function

#main

print("Welcome to the MAGIC 8 BALL ask a question with a yes or no and I will give you a respone.")
while True:
    print("please enter a question that has a yes or no response")
    question = input("enter a question:")
    while question.endswith("?"):
        print("Shake...")
        time.sleep(2)
        print("Shake...")
        time.sleep(2)
        print("Shake...")
        time.sleep(2)
        print(random.choice(respones))
        print("would you like to countine?")
        ans = input("yes or no")
        if ans == "yes":
            print("please ask another question")
            question = input("enter a question:")
            while question.endswith("?"):
                print("Shake...")
                time.sleep(2)
                print("Shake...")
                time.sleep(2)
                print("Shake...")
                time.sleep(2)
        if ans == "no":
            break

    else:
        print("make sure you have a ? mark")

    print("would you like to countine?")
    ans = input("yes or no")
    if ans == "yes":
        print("please ask another question")
    if ans == "no":
        break


