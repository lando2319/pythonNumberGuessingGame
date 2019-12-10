import random 
print("")
print("Jason's Random Number Guessing Game") 
text = raw_input ("Your number is: ")
print("")
print("Your number is: ")
print(text)
print("") 
outputNumber = random.randint(1,1)

print("The Game Chose: ", outputNumber)

if (int(text) == outputNumber): 
	print(text, "is correct")
else:
	print(text, "is incorrect")
