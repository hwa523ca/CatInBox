import random #Import the random library.

def nBoxGame(n:int): #The nBoxGame() function with n (required to be an integer) being the number of boxes.
    boxList = ["Empty"] * n #Add a number of boxes to the list of boxes.
    catBox = random.randint(0,n-1) #Choose a box for the cat to hide in.
    boxList[catBox] = "Cat" #Put the Cat in the box.
    catFound = False #Boolean variable initially set to be false since the Cat hasn't been found yet.
    while catFound == False: #While the cat hasn't been found yet.
        boxNum = int(input(f"Pick a number between 1 and {n}.\nWhere do you think it is?\n")) #Ask the player to choose a box to open.
        while boxNum < 1 or boxNum > n: #While the player has chosen an invalid box.
            boxNum = int(input(f"That's not a valid box!\nPick a number between 1 and {n}.\nWhere do you think it is?\n")) #Keep asking the player to pick a valid box.
        if boxList[boxNum - 1] == "Cat": #If the cat was found in the box the player chose.
            print("You found the cat!") #Tell the player they have found the cat.
            catFound = True #Set the catFound boolean variable to True.
        else: #Otherwise.
            print("The cat is not there!") #Tell the player the cat is not there.
            boxList[catBox] = "Empty" #Move the cat out of the box.
            if catBox == 0: #If the cat was in the leftmost box.
                boxList[1] = "Cat" #Move the cat to the box on the right.
                catBox = 1 #Set the catBox variable to 1 since the cat has move to the right of the previous box.
            elif catBox == (n-1): #Otherwise, if the cat was in the rightmost box.
                boxList[n-2] = "Cat" #Move the cat to the box on the left.
                catBox = n-2 #Set the catBox variable one less since the cat has move to the left of the previous box.
            else: #Otherwise.
                oneOrTwo = random.randint(0,1) #Choose a box for the cat to move in with 0 being the box to the left and 1 being the box to the right.
                if oneOrTwo == 0: #If oneOrTwo returns 0.
                    boxList[catBox - 1] = "Cat" #Move the cat to the box on the left.
                    catBox = catBox - 1 #Decrement the catBox variable since the cat has moved to the left of the previous box.
                elif oneOrTwo == 1: #Otherwise, if oneOrTwo returns 1.
                    boxList[catBox + 1] = "Cat" #Move the cat to the box on the right.
                    catBox = catBox + 1 #Increment the catBox variable since the cat has moved to the right of the previous box.

def playGame(): #The playGame() function that asks the player if they would like to play, and how many boxes they would like to play with.
    try: #Exception handling.
        toPlay = input("Welcome to \"Cat In The Box\"!\nThe Objective of the Game is the find the cat in one of five boxes.\nHere's a hint:\nThe cat can only move to adjacent boxes.\nWould you like to play? Type either \"Y\" or \"Yes\" to play.\n").capitalize() #Asks the player if they would like to play. Y or Yes allows the player to play; another response does not.
        if toPlay == "Yes" or toPlay == "Y": #If the player wants to play.
            while toPlay == "Yes" or toPlay == "Y": #While the player wants to keep on playing.
                numBox = int(input("Let's play!\nHow many boxes would you like to play with?\n3, 4, or 5?\n")) #Ask the player how many boxes they would like to play with. The current options are 3, 4, or 5.
                while numBox < 3 or numBox > 5: #If the player chooses an invalid number.
                    numBox = int(input("That is not a valid number!\nHow many boxes would you like to play with?\n3, 4, or 5?\n")) #Keep asking them for a valid number.  
                nBoxGame(numBox) #Play the game with the nBoxGame() function with the number of boxes (represented by the variable numBox) as input.
                toPlay = input("Would you like to play again?\n").capitalize() #Ask the player if they would like to play again.
            print("Thanks for playing!") #Thank the user for playing.
        else: #Otherwise
            print("No worries!") #Tell the user not to worry.
    except: #If an error is found.
        print("ERROR!") #Print out ERROR! to let the player know there is an error.

playGame() #Play the game.