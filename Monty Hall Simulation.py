import random
import numpy as np
import matplotlib.pyplot as plt



def assignPrize():
    keepOriginWin = 0#All four possible scenarios
    keepOriginLose = 0
    switchWin = 0
    switchLose = 0
    for x in range (1000):
        comp = []
        user = []
        compareFinal = ["one", "two", "three"]#Three doors
        switchArray = ["yes", "no"]#Decision which is made later on
        same=False
        threeDoors = ["one", "two", "three"]#This array is the one we remove from
        choiceRand = random.randint(0, 2)
        prizeChosenComputer = threeDoors[choiceRand]#Generating the door for player and comp
        comp.append(prizeChosenComputer)
        choiceRandUser = random.randint(0, 2)
        prizeChosenUser = threeDoors[choiceRandUser]
        user.append(prizeChosenUser)
        if threeDoors[choiceRand]==threeDoors[choiceRandUser]:
            threeDoors.remove(prizeChosenUser)
            compareFinal.remove(prizeChosenUser)
            same=True
        else:
            threeDoors.remove(prizeChosenComputer)#Determining which door can be removed
            threeDoors.remove(prizeChosenUser)
            compareFinal.remove(prizeChosenUser)
        if same==True:
            randomnumleft = random.randint(0, 1)
            randomleft = threeDoors[randomnumleft]
            compareFinal.remove(randomleft)
            #print("Door Number: ", randomleft, "doesn't have the prize")#removing the door which doesn’t have the prize
        else:
            randomleft = threeDoors[0]
            compareFinal.remove(randomleft)
      #print("Door Number: ", randomleft, "doesn't have the prize")
  #print("comp: ", prizeChosenComputer)
  #print("user:", prizeChosenUser)

        genSwitch = random.randint(0, 1)
        switchUser = switchArray[genSwitch]#This determines if the user switches or not
        #print(switchUser)
        if switchUser=="yes":
            if compareFinal == comp:
                #print("YOU WIN")
                #print("The Door with the prize was: ", comp)
                switchWin+=1
            else:
                #print("YOU LOST")
                #print("The Door with the prize was: ", comp)
                switchLose+=1
        if switchUser=="no":
            if comp==user:
                #print("YOU WIN!")
                #print("The Door with the prize was: ", comp)
                keepOriginWin+=1
            else:
                #print("YOU LOST!")
                #print("The Door with the prize was: ", comp)
                keepOriginLose+=1
    print("Keep Original Win: ", keepOriginWin)
    print("Keep original Lose: ", keepOriginLose)
    print("Switch Win", switchWin)
    print("Switch Lose", switchLose)
    objects = ('Keep Orig. Win', 'Keep Orig. Lose', 'Switch Win', 'Switch Lose')
    y_pos = np.arange(len(objects))
    performance = [keepOriginWin, keepOriginLose, switchWin, switchLose]
    plt.bar(y_pos, performance, align='center')#Learned how to do this through: https://pythonspot.com/matplotlib-bar-chart/
    plt.xticks(y_pos, objects)#Making an organized bar graph with all four bars labeled
    plt.ylabel('Range')
    plt.xlabel("4 Different Scenarios")
    plt.title('Monty Hall Problem(1000 Times simulated)')
    plt.show()


assignPrize()
