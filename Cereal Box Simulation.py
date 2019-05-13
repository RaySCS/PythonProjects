import random
import statistics
import numpy as np
import matplotlib.pyplot as plt

def choosePrize():
 numTimesNeeded = 0
 storeNums = []
 all=0
 for x in range(1000):
     numTimesinEach = 0
     cerealBox = []
     notAllPrizes = False
     while notAllPrizes == False:
         prizes = ["a", "b", "c", "d", "e", "f"]#The prizes
         choiceRand = random.randint(0, 5)
         prizeChosen = prizes[choiceRand]#Generating random prizes
         numTimesinEach+=1#Incrementing the value every time, so that we know how many times it took.
         for x in range(len(prizeChosen)):
             cerealBox.append(prizeChosen)
         if "a" in cerealBox and "b" in cerealBox and "c" in cerealBox and "d" in cerealBox and "e" in cerealBox and "f" in cerealBox:
             all=all+numTimesinEach#Using an if in, in order to determine when all the prizes have been accumilated
             notAllPrizes=True
     storeNums.append(numTimesinEach)
 average=all/1000#To get average
 medianall= statistics.median(storeNums)#had to use this python function in  order to get the median of all the trial array.
 print(storeNums)
 print("The average is:", average)
 print("The median is:",medianall)
 plt.hist(storeNums, bins=range(min(storeNums), max(storeNums) + 2), align="mid")
 plt.ylabel('Frequency of Those Boxes')
 plt.xlabel("Number of times needed to get all prizes")
 plt.title('Frequency of Number of Times Needed to Get All Prizes')
 plt.show()

choosePrize()
