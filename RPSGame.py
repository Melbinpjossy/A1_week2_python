from random import randint

# available weapons => store this in a array
choices = ["Rock", "Paper", "Scissors"]
player = False



while player is False:
    print("Choose your Weapon!\n")
    player = input("Rock, Paper or Scissor?\n")
    print("Player chooses:", player)

# make the computer pick one item at random
computer = choices[randint(0,2)]

#shows the computers choice in the terminal window
print("Computer chooses: ", computer)

if(player == computer):
	print("Tie! Live to shoot another day")
elif player == "Rock":
    if computer == "Paper":
    	#computer won
    	print("You lose", computer,"cover",player)
    else:
    	print("You win!", player, "smashes", computer)

elif player == "Paper":
    if computer == "Scissors":
    	#computer won
    	print("You lose", computer,"cuts",player)
    else:
    	print("You win!", player, "Covers", computer)

elif player == "Scissors":
    if computer == "Paper":
    	#computer won
    	print("You lose", computer,"smashes",player)
    else:
    	print("You win!", player, "Cuts", computer)

elif player =="Quit":
    exit()

else:
	print("Not a Vailid option, Check again, and check your spelling!\n")

player = False
computer = choices[randint(0,2)]