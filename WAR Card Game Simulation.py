import random
import statistics
import numpy as np
import matplotlib.pyplot as plt
def choose():
   numinEach = 0#Just so we can use this to find out mean and median
   flipsArray = []#a blank array which stores how many flips were necessary to
   for x in range(100):
       turn = 0
       cards=[1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]#Deck of 52 cards.
       player1score=26
       player2score = 26#Each person has 26 carsd to start out with
       player1=[]
       player2=[]
       total=52#Amount of cards necessary to win
       for i in range(26):
           num1=random.randrange(0,total)#Dealing the cards
           deal1=cards[num1]#Card has been obtained
           cards.remove(deal1)#Removing that specific "card" from the array
           total=total-1
           player1.append(deal1)
           num2=random.randrange(0,total)
           deal2=cards[num2]
           cards.remove(deal2)
           player2.append(deal2)#Appending each players random card
           total=total-1
           #Below the while loop will keep on running until a person has 52 cards
       while player1score!=52 and player2score!=52:
           numinEach += 1
           randnum1=random.randrange(0,len(player1))#So basically keep on running code below until one player doesn't have 52 cards or whole deck(winner)
           move1 = player1[randnum1]
           randnum2=random.randrange(0,len(player2))
           move2 = player2[randnum2]
           if move1>move2:
               player1score=player1score+1#Depedning on who won that "round", they get their own card and the other players card. Vice versa for the other person
               player2score=player2score-1#other player loses that card they put down
               player1.append(move2)#person who won gets the card
               player2.remove(move2)#peson who lost loses the card
               turn+=1#in order to know how many flips were taken.
           if move2>move1:
               player2score=player2score+1
               player1score=player1score-1
               player1.remove(move1)
               player2.append(move1)
               turn+=1
           if move1==move2:
               flipCoin=random.randrange(1,2)#when there is a tie, we do a coin flip in order to determine who the winner is
               if flipCoin==1:
                   player1.append(move2)
                   player2.remove(move2)
                   player1score+=1
                   player2score=player2score-1
                   turn+=1
               if flipCoin==2:
                   player2.append(move1)
                   player1.remove(move1)
                   player1score=player1score-1
                   player2score =player2score+1
                   turn+=1
               if player1score == 52 or player2score == 52:
                   if len(player1) == 0:
                       player1score = 0#if any of the player has reached 52, then the other person loses automatically
                       player2score = 52
                   if len(player2) == 0:
                       player2score = 0
                       player1score = 52
       flipsArray.append(turn)
   numMedian = statistics.median(flipsArray)  # Gets the median(middle)
   numMean = numinEach/100
   endgame(turn,player1score,player2score, player1, player2, flipsArray, numMean, numMedian)#calling the print function basically


def endgame(turn,player1score,player2score, player1, player2, flipsArray, numMean, numMedian):
   print("Flips Array: ", flipsArray)
   print("Player One Array: ", player1)#just to show who obtained all 52 cards
   print("Player Two Array: ", player2)
   print("Median is: ", int(numMedian))
   print("Mean is: ", int(numMean))

   objects = ('MEDIAN', 'MEAN')
   y_pos = np.arange(len(objects))
   performance = [numMedian, numMean]
   plt.bar(y_pos, performance, align='center')#Learned how to do this through: https://pythonspot.com/matplotlib-bar-chart/
   plt.xticks(y_pos, objects)
   plt.ylabel('# 0-1000')
   plt.xlabel("Meadian and Mean")
   plt.title('Medin, Mean')
   plt.show()


choose()

