import random


randomNumber = str(random.randint(1000,9999))

print("Choose the level of difficulty:\n1. Easy(10 attempts)\n2. Medium(5 attempts)\n3. High(3 attempts)")
attempts = int(input())

n = 0
a = 0

if(attempts == 1):
    a = 10
elif(attempts == 2):
    a = 5
elif(attempts == 3):
    a = 3

while n < a:
    print("Please enter the 4 Digits to guess")
    userInput = str(input())
    if(userInput == "Hint"):
        print("A Number from the pass code:",randomNumber[-random.randrange(1,4)])
        continue
    output = ""

    for i in range(4):
        if userInput[i] == randomNumber[i]:
            output += "🟢"
        elif userInput[i] in randomNumber:
            output += "🟡"
        else:
            output += "❌"

    print(output)
    n += 1
    
    if output == "🟢🟢🟢🟢":
        print("Hey!! You won..")
        break
else:
    print("You've reached max number of times, and the random number is:", randomNumber)
