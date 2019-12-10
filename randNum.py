import random 

print("")
print("Jason's Random Number Guessing Game") 


roundNum = 1

wins = 0
loses = 0

def runGame(roundNum, wins, loses):
    print("")
    print("READY FOR ROUND " + str(roundNum)) 
    print("The Standings Are WINS " + str(wins) + " LOSES " + str(loses)) 

    text = raw_input ("Your number is: ")
    print("")
    print("Your number is: ")
    print(text)
    print("") 
    outputNumber = random.randint(1,1)

    verdict = ""

    if (int(text) == outputNumber): 
        verdict = "WON"
        wins = wins + 1
    else:
        verdict = "LOST"
        loses = loses + 1

    # print("YOU HAVE ", verdict, "Round", roundNum)
    print("YOU HAVE " + verdict + " Round")
    roundNum = roundNum + 1
    return runGame(roundNum, wins, loses)



runGame(roundNum, wins, loses)
