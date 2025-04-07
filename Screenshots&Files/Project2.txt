#Completed:
'''
1. Game developed
2. Leaderboards: Track and display the fastest successful attempts.'''

import random
import time

randomNumber = str(random.randint(1000,9999))
attempts = 0
#Range doesnt include 11, so max attempts will be 10
maxAttempts = 11

print("Enter your name!!")
name = input()

print("Your timer starts now!!")
startTime = time.time()
print("Start guessing the 4-digit passcode!")

for i in range(1, maxAttempts):
    n = input()

    if len(n) != 4:
        print("Please enter 4 digits only")
        break

    guessFeedback = ""

    for i in range(4):
        if n[i] == randomNumber[i]:
            guessFeedback += "🟢"
        elif n[i] in randomNumber:
            guessFeedback += "🟡"
        else:
            guessFeedback += "❌"
    
    print("Match level of the passcode you entered", guessFeedback)

    if guessFeedback == "🟢🟢🟢🟢":
        print("Congratulations!! You guessed it correct", guessFeedback)
        endTime = time.time()

        fi = open("/Users/pranith/Python/Screenshots&Files/leaderShipBoard.txt","a")
        fi.write(f"Name: {name}, Completed challenge in: {endTime-startTime}")
        fi.close()
        break

else:
    endTime = time.time()
    print("You've reached your maximum attempts and the random number was:", randomNumber, "You've spent:", endTime-startTime)
    
    print("\nLeaderShip Board")
    f = open("/Users/pranith/Python/Screenshots&Files/leaderShipBoard.txt","r")
    print(f.read())
    f.close()