import random 

print("")
print("Jason's Random Number Guessing Game") 


roundNum = 1

def runGame(roundNum):
    print("")
    print("READY FOR ROUND " + str(roundNum)) 

    text = raw_input ("Your number is: ")
    print("")
    print("Your number is: ")
    print(text)
    print("") 
    outputNumber = random.randint(1,1)

    print("The Game Chose: ", outputNumber)

    verdict = ""

    if (int(text) == outputNumber): 
        verdict = "WON"
    else:
        verdict = "LOST"

    # print("YOU HAVE ", verdict, "Round", roundNum)
    print("YOU HAVE " + verdict + " Round")
    roundNum = roundNum + 1
    return runGame(roundNum)



runGame(roundNum)
