import random


gameOver = False#signyfying when to keep certain loops running.
gamesWon = 0#Global variables which are used. Others are passed as parameters. Keeps track of win and losses combined.
gamesLost = 0

def displayRules():
 askName = input("Hello, What's your first name?")#Purpose of function: Display general rules
 print("Welcome", askName, "to MasterMind, a game which involves an intellectual mindset or just pure luck!")#Below are rules.
 print("Rules: ")#Purpose of function: Just display rules and call the begin game function
 print("-The computer selects a sequence of four colors out of six, which are red, green, orange, blue, yellow, and purple")
 print("-You input a sequence of FOUR/SIX/EIGHT colors,depending on what mode you choose. (enter full color names)")
 print("-Once you have selected a sequence press return and then you will see how accurate you were")
 print("-If you are told a white peg, then you have the right color, but not the right position for one of the colors")
 print("-If you are told a black peg, then you have the right color, and right position for one of the colors ")
 print("-Format should be as followed, ex: red, green, orange, blue")
 print("-SEQUENCE AND COLORS ARE KEY TO SUCCESS")
 print("")
 beginGame()#Organizing code in order to make sure everything is useful and makes sense


def beginGame():
   compChoice=[]#Purpose of function is to determine what option user wants(1v2). Then that corresponding function is called. Abstracting with functions
   global gameOver
   i=0#Used for while loop increment value
   Attempts=0#Increase the increment every attempt made
   games=10#10 games as increment allows.
   askGameMode = input("Would you like to play one player or two player? Specify one or two")#Two game options available
   if askGameMode=="one":
       onePlayer(Attempts, games, i, compChoice)#The neccessary parameters being passed
   if askGameMode=="two":
       twoPlayer(Attempts, i)

def twoPlayer(Attempts,i):
   print("Rules are still applicable, but now one player will make code, other player guesses")#This function just displays rules for 2 player
   print("Choose one person to be player one, the other player two")#Also, it gets the player 1 entry and calls the scenarios for 2 player
   print("You may choose your own category of things to code and decode")
   askRounds = int(input("How many games would you like to play?"))
   askCat = input("Player One, before you enter the sequence, enter the four possible choices with commas player two may choose")
   catDisplay = askCat.split(",")
   print("Choices Possible: ", catDisplay)#For the 2nd players easeness
   askPlayerOne = input("Player one, input the sequence of four colors you wish to code, remember to make it different from the possibilities")
   playerOneGuess = askPlayerOne.split(",")  # Allows for Letters to be splitted. Gives in an array format. Could split by any character
   global gameOver
   while i<askRounds and gameOver==False:
       i += 1#Incrementing the value everytime the loop ran.
       Attempts += 1
       twoPlayerScenarios(playerOneGuess, Attempts, askRounds)

def twoPlayerScenarios(playerOneGuess, Attempts, askRounds):
   positionCheck1 = False#Purpose of function: It is the function which determines the black and white pegs, the scenarios for 2 player
   positionCheck2 = False
   positionCheck3 = False
   positionCheck4 = False
   global gameOver
   playAgain=False
   BlackPegs = 0
   WhitePegs = 0
   playerOneWon = 0
   playerTwoWon = 0
   askPlayerTwo = input("Player two, input the sequence which you believe is corresponding to player ones sequence")#The other players input
   playerTwoGuess = askPlayerTwo.split(",")#Breaks apart entry
   for a in range(0, len(playerOneGuess)):
       white = False
       for c in range(0, len(playerTwoGuess)):
           if playerOneGuess[a] == playerTwoGuess[c]:
               white = True  # If any match found, boolean is true, white peg is true then
               WhitePegs += 1
   if playerOneGuess[0] == playerTwoGuess[0]:
       positionCheck1 = True#Going through every position 0,3 and turning a boolean on if a certain position matches
   if playerOneGuess[1] == playerTwoGuess[1]:
       positionCheck2 = True#Here took a bit of different approach, as I made sure if a color is a white peg then it is possible for it to be a black peg
   if playerOneGuess[2] == playerTwoGuess[2]:
       positionCheck3 = True
   if playerOneGuess[3] == playerTwoGuess[3]:
       positionCheck4 = True
   if white == True and positionCheck1 == True:
       BlackPegs += 1#So if its white(meaning in both arrays) and in same postiion
   if white == True and positionCheck2 == True:
       BlackPegs += 1
   if white == True and positionCheck3 == True:
       BlackPegs += 1
   if white == True and positionCheck4 == True:
       BlackPegs += 1
   if BlackPegs == 4:
       BlackPegs = 4
       WhitePegs = 4
       print("Player Two, you have won!")#Player 2 wins when he/she guesses right
       playerTwoWon += 1
       print("Player One sequence ", playerOneGuess)
       print("Player One Games Won: ", playerOneWon)
       print("Player Two Games Won: ", playerTwoWon)
       gameOver = True
       playAgain=True
   if Attempts >= askRounds:
       print("Player One, you have won!")#When there are equal attempts, the first user(p1) won
       playerOneWon += 1
       print("Player One sequence ", playerOneGuess)
       print("Player One Games Won: ", playerOneWon)
       print("Player Two Games Won: ", playerTwoWon)
       gameOver = True#Turns on to let loop know to stop
       playAgain=True#Turns on if user wants to play again
   newWhitePeg = WhitePegs - BlackPegs  # In order to avoid duplicate between both white and black
   if gameOver == True:
       askPlayAgain = input("Would you like to go back to the main menu?")
       if askPlayAgain == "yes":
           positionCheck1 = False # Reseting these variables except for the games won and lost as those are kept the same for the user needs to know how many games they won/lost.
           positionCheck2 = False
           positionCheck3 = False
           positionCheck4 = False
           playAgain = False
           BlackPegs = 0
           WhitePegs = 0
           gameOver = False
           beginGame()
       if askPlayAgain=="no":
           print("Have a joyous day")
   print("Black Pegs: ", BlackPegs)
   print("White Pegs: ", newWhitePeg)

def onePlayer(Attempts, games, i, compChoice):
   import random#Purpose of function is to determine what diffculty the user wants
   askLevel = input("Would you like to play easy, medium, or hard?")#Three different category levels
   if askLevel == "hard":
       arrayColors = ["red", "orange", "green", "blue", "yellow", "purple", "gray", "pink"]#LogicFlow-Higher level=more colors
       print("Options to choose from: ", arrayColors)
       print("Disclaimer: There are ARE duplicates")#Hard should be hard, thats why out of eight
       for x in range(0,4):
           compChoice.append(arrayColors[random.randrange(0, len(arrayColors))])
   if askLevel == "medium":
       arrayColors = ["red", "orange", "green", "blue", "yellow", "purple"]
       print("Options to choose from: ", arrayColors)
       print("Disclaimer: There are ARE duplicates")# Medium is medium, thats why out of six
       for x in range(0,4):
           compChoice.append(arrayColors[random.randrange(0, len(arrayColors))])#Generating a random set of colors, possible duplicates as well
   if askLevel == "easy":
       arrayColors = ["red", "orange", "green", "blue"] # Array of colors
       print("Options to choose from: ", arrayColors)
       print("Disclaimer: There are NO duplicates")#since easy game mode, there are no duplicates
       compChoice = random.sample(arrayColors,4)  # This code allows for a random selection of the quantity, ALSO makes an array
   while i<games and gameOver==False:
       i+=1#Loop keeps on going through until the number of games is less than 10 and when the gameOver boolean hasnt turned true.
       Attempts += 1
       scenarios(askLevel,compChoice,Attempts,games)#Passing parameters, abstracting to make functions more useful

def scenarios(askLevel,compChoice,Attempts,games):
   global gameOver#Purpose of Function: Goes through the scenarios possible for one player mode. This is done using a nested for loop(like hangman).
   global gamesWon
   global gamesLost
   playAgain = False
   Black = False
   white = False
   BlackPegs = 0
   WhitePegs = 0
   user = input("What is your guess? ie: red, green, blue, orange")
   userGuess = user.split(",")  # Allows for Letters to be splitted. Gives in an array format.
   i = 0
   for x in range(0, 4):
       if userGuess[i] in compChoice:
           WhitePegs += 1
           i += 1
       else:
           i += 1
   i = 0
   for x in range(0, 4):
       if userGuess[i] == compChoice[i]:
           userGuess.pop(i)
           userGuess.insert(i, '*')
           BlackPegs += 1
           i += 1
       else:
           i+=1
   if BlackPegs == 4:
       BlackPegs=4
       WhitePegs = 4
       print("YOU HAVE WON!!")
       gamesWon+=1
       print("Games Won: ", gamesWon)
       print("Games Lost: ", gamesLost)
       gameOver=True#Just in order to know when to start and finish game
       playAgain=True#So that game is played again by users request
   if Attempts >= games:
       print("YOU HAVE LOST!")
       gamesLost+=1
       print("Computer Choice: ", compChoice)#IF user still hasnt guessed then just showcase answer
       print("Games Won: ", gamesWon)
       print("Games Lost: ", gamesLost)
       gameOver=True
       playAgain=True
   WhitePegs = WhitePegs - BlackPegs  # In order to avoid duplicate between both white and black
   print("Black Pegs: ", BlackPegs)
   print("White Pegs: ", WhitePegs)
   print(compChoice)
   if playAgain==True:
       askPlayAgain = input("Would you like to go the main menu?")#Giving the user a chance to play again
       if askPlayAgain=="yes":
            #Reseting these variables except for the games won and lost as those are kept the same for the user needs to know how many games they won/lost.
           playAgain = False
           BlackPegs = 0
           WhitePegs = 0
           gameOver=False
           beginGame()
       if askPlayAgain=="no":
           print("Have a joyous day!")

displayRules()

