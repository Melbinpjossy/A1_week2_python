from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors", "quit"]
player_life = 3;
computer_life = 3;
#assign a random play to the computer
computer = t[randint(0,2)]

#define a wiin or lose function instead of proedural way
def winorlose(status):

    print("called the win or lose function")
    print("***********************************")
    print("You", status, "!", "Would you like to play again?")
    choice = input ("Y / N; ")

    if choice == "Y" or choice == "y":


         global player_life
         global computer_life
         global player
         global computer

         player_life = 3
         computer_life = 3
         player = False
         computer = choices[randint(0,2)]
    elif choice == "N" or choice =="n" :
         print("You Chose to quit")
         exit()
 
#set player to False
player = False
while player == False:
    print("===================================")
    print("Player Lives: ", player_life, "/3", " Computer lives: ", computer_life, "/3")
    print("===================================")
    print("Choose your weapon!\n")
    player = input("Rock, Paper, Scissors?\n")
    print("Computer Chooses: ", computer)

    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            player_life = player_life - 1;
        else:
            print("You win!", player, "smashes", computer)
            computer_life = computer_life - 1;
        print("Computer life = ", computer_life, "\n Player life = ", player_life)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            player_life = player_life - 1;
        else:
            print("You win!", player, "covers", computer)
            computer_life = computer_life - 1;
        print("Computer life = ", computer_life, "\n Player life = ", player_life)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            player_life = player_life - 1;
        else:
            print("You win!", player, "cut", computer)
            computer_life = computer_life - 1;
    elif player == "quit":
        exit()
    else:
        print("That's not a valid play. Check your spelling!")
    print("{Quit anytime by typing - quit}\n")
    
    if player_life is 0:
        winorlose("lost")

    if computer_life is 0:
      winorlose("Win")

    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)] 