import random

#GOal is to: Make sure that each person gets an attribute in the three categories of average, power, speed
#Also, THe goal is to make sure that the user is happy with the team they are alloted
#Each persons hits and types of hits should be kept track of. Along with lifetime, so season throughout
def playBall():
    baseBallSelectionPlayers()

def baseBallSelectionPlayers():
  names = ["Bob  ", 'Joe  ', 'Steve', 'Mike ', 'Luke ', 'Mark ', 'John ', 'Aaron', 'James']#Random names

  class Player(object):
      def __init__(self):
          self.name = random.choice(names)#Classes, the idea of classes allows us to use one variable in a certain place which has a value for multiple things.
          self.average = random.randint(1, 100)#Giving characterisitcs one through one hundred instead of 1-3
          self.power = random.randint(1, 100)
          self.speed = random.randint(1, 100)
          self.HTS = 0
          self.single = 0#Each persons type of hits
          self.double = 0
          self.triple = 0
          self.homerun = 0
          self.HTSA = 0#The A at the end, represents the other teams(away) indidvual players scores.
          self.singleA = 0
          self.doubleA = 0
          self.tripleA = 0
          self.homerunA = 0

      def displayPlayer(self):
          print(self.name, " ", self.average, " ", self.power, " ", self.speed)  # Using the information

      def displayStats(self):
          print(self.name, "  ",  self.single,  "  ", self.double, "  ", self.triple, "  ", self.homerun, "   ", self.HTS)
      def displayStatsA(self):
          print(self.name, "  ",  self.singleA,  "  ", self.doubleA, "  ", self.tripleA, "  ", self.homerunA, "   ", self.HTSA)

      def AddHits(self):
          self.HTS = self.HTS + 1
      def AddSingle(self):
          self.single+=1#THese defs keep track of each persons hits types
      def AddDouble(self):
          self.double+=1
      def AddTriple(self):
          self.triple+=1
      def AddHomeRun(self):
          self.homerun+=1
      def AddHitsA(self):
          self.HTSA = self.HTSA + 1
      def AddSingleA(self):
          self.singleA+=1
      def AddDoubleA(self):
          self.doubleA+=1
      def AddTripleA(self):
          self.tripleA+=1
      def AddHomeRunA(self):
          self.homerunA+=1#Above are all the functions in order to keep track of a players track

  class Team(object):
      def __init__(self):
          self.players = []#Array of each players stats, scores

      def add_players(self):
          for i in range(0, 9):
              self.players.append(Player())
              self.players[i].displayPlayer()

      def show_Stats(self):
          for i in range(0, 9):
              self.players[i].displayStats()

      def show_StatsA(self):
          for i in range(0, 9):
              self.players[i].displayStatsA()

  print("Oponent Team:")
  print("Name    AV  PW  SD")#AV=Average, PW=Power, SD = Speed
  team2 = Team()
  team2.add_players()
  response = "0"
  print("Your team can be:")
  print("Name    AV  PW  SD")
  while response == "0":
      team1 = Team()
      team1.add_players()
      response = input("Do you wish to draft these players? 0 for no, 1 for yes")#Allowing the user to keep rolling until they are content
  askTeamName = input("What would you like for the name of the home team(your team) to be? Make it four letters please.")
  playBaseball(team1, team2, names, askTeamName)#Passing parameters which can be used in the function below


def playBaseball(team1, team2, names, askTeamName):
    homeScore = []  # In order to keep track of each teams scores(runs)
    awayScore = []
    possession = 1
    innings = 10
    hitsTotalHome = 0
    hitsTotalAway = 0
    counter = 0
    homeTeamWins = 0
    awayTeamWins = 0
    maxSingle = []
    maxDouble = []
    maxTriple = []
    maxHomeRun = []
    maxHits = []
    for y in range(0, 10):#simulate whole 10 times
        for x in range(1, innings): # loops 9 times for the 9 innings. IF tie occurs, then innings is added
            counter+=1
            BasesArrayHome = [False, False, False, False, False, False, False]  # Need a total of 7 spots first three represent the bases and then the rest equal the other possibilities
            BasesArrayAway = [False, False, False, False, False, False, False]#Seperate arrays for both teams
            hitsHome = 0
            hitsAway = 0  # These variables need to be reset as if not they keep on adding upon each other.
            runsHome = 0
            runsAway = 0
            if possession == 1:
                outs = 0
                while outs != 3:
                    playerNumber = random.randint(0, 8)
                    playerArray = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                    randomPlayer = playerArray[playerNumber]
                    playerArray.remove(randomPlayer)#This allows us to chose a random person, and making sure that person is not chosen again
                    determineHit = random.randint(1, 100)#This determines if they hit the ball or not, firstly
                    if determineHit >= team1.players[randomPlayer].average:
                        outs += 1#If the player doesn't get a number higher than the random generated num, then they are out. Else the code below runs(Selection)
                    if determineHit <= team1.players[randomPlayer].average:
                        hitSingle = False#The code above tells if the player got a hit or not.
                        hitDouble = False
                        hitTriple = False
                        hitHomeRun = False
                        nothingElse = False
                        if team1.players[randomPlayer].average > 10 and team1.players[randomPlayer].average <50 and nothingElse==False:
                            hitSingle = True#THese numbers above represent what requirements a certain player has to meet in order to get a certain hit. And also need to make sure that they are not hitting another hit as well.
                            hitsHome += 1#Scores are ranging between(0-20)
                            hitsTotalHome+=1
                            nothingElse = False
                        if team1.players[randomPlayer].speed > 20 and team1.players[randomPlayer].speed < 80 and nothingElse==False:
                            hitDouble = True#All turning true
                            hitsHome += 1
                            hitsTotalHome+=1
                            nothingElse = False
                        if team1.players[randomPlayer].speed >= 40 and team1.players[randomPlayer].speed >= 0 and nothingElse==False:
                            hitTriple = True
                            hitsHome += 1
                            hitsTotalHome+=1
                            nothingElse = False
                        if team1.players[randomPlayer].power > 1 and team1.players[randomPlayer].power < 20 and nothingElse==False:
                            hitHomeRun = True
                            hitsHome += 1#As shown the chances of getting a homerun are hard
                            hitsTotalHome+=1
                            nothingElse = False

                        if hitSingle == True:
                            for x in range(1, -1, -1):
                                BasesArrayHome[x + 1] = BasesArrayHome[x]  # NEED TO DO -1,-1 in order to go from front to back of array.
                            BasesArrayHome[0] = True  # Single means first spot is true
                            team1.players[randomPlayer].AddSingle()
                            team1.players[randomPlayer].AddHits()
                            for a in range(3, 7):
                                if BasesArrayHome[a] == True:
                                    runsHome += 1
                                    BasesArrayHome[a] = False
                            hitSingle = False
                        if hitDouble == True:
                            for x in range(1, -1, -1):
                                BasesArrayHome[x + 2] = BasesArrayHome[x]#Base runners move the same distance as hitters
                            BasesArrayHome[1] = True  # Double means second spot is true
                            team1.players[randomPlayer].AddDouble()
                            team1.players[randomPlayer].AddHits()
                            for a in range(3, 7):
                                if BasesArrayHome[a] == True:
                                    runsHome += 1
                                    BasesArrayHome[a] = False
                            hitDouble = False#turning false so that other hits are possible
                        if hitTriple == True:
                            for x in range(1, -1, -1):
                                BasesArrayHome[x + 3] = BasesArrayHome[x]
                            BasesArrayHome[2] = True  # Triple means third spot is true
                            team1.players[randomPlayer].AddTriple()
                            team1.players[randomPlayer].AddHits()
                            for a in range(3, 7):
                                if BasesArrayHome[a] == True:
                                    runsHome += 1  # Going through position 3 to 6 and adding the run if base is true
                                    BasesArrayHome[a] = False
                            hitTriple = False
                        if hitHomeRun == True:
                            for x in range(1, -1, -1):
                                BasesArrayHome[x + 4] = BasesArrayHome[x]  # HOME RUN means advance four
                            BasesArrayHome[3] = True  # HOME RUN means fourth spot is true
                            team1.players[randomPlayer].AddHomeRun()#Home run is added to the players attributes
                            team1.players[randomPlayer].AddHits()
                            for a in range(3, 7):
                                if BasesArrayHome[a] == True:
                                    runsHome += 1  # Going through position 3 to 6 and adding the run if base is true
                                    BasesArrayHome[a] = False
                            hitHomeRun = False
                    possession = 2#Alternating possessions
            if possession == 2:
                outs = 0
                while outs != 3:
                    playerNumber = random.randint(0, 8)
                    playerArray = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                    randomPlayer = playerArray[playerNumber]
                    playerArray.remove(randomPlayer)#Ensuring each player goes once. And the array is reset every time, this allowing for a problem not to be caused.
                    determineHit = random.randint(1, 100)#This determines if they hit the ball or not, firstly
                    if determineHit >= team2.players[randomPlayer].average:
                        outs += 1
                    if determineHit <= team2.players[randomPlayer].average:
                        hitSingle = False#The code above tells if the player got a hit or not.
                        hitDouble = False
                        hitTriple = False
                        hitHomeRun = False
                        nothingElse = False
                        if team2.players[randomPlayer].average > 10 and team2.players[randomPlayer].average <50 and nothingElse==False:
                            hitSingle = True#THese numbers above represent what requirements a certain player has to meet in order to get a certain hit. And also need to make sure that they are not hitting another hit as well.
                            hitsAway += 1
                            hitsTotalAway+=1
                            nothingElse = False
                        if team2.players[randomPlayer].speed > 80 and team2.players[randomPlayer].speed < 40 and nothingElse==False:
                            hitDouble = True#All turning true
                            hitsAway += 1
                            hitsTotalAway += 1
                            nothingElse = False
                        if team2.players[randomPlayer].speed >= 40 and team2.players[randomPlayer].speed >= 0 and nothingElse==False:
                            hitTriple = True
                            hitsAway += 1
                            hitsTotalAway += 1
                            nothingElse = False
                        if team2.players[randomPlayer].power > 1 and team2.players[randomPlayer].power < 20 and nothingElse==False:
                            hitHomeRun = True
                            hitsAway += 1
                            hitsTotalAway += 1
                            nothingElse = False
                        if hitSingle == True:
                            for x in range(1, -1, -1):
                                BasesArrayAway[x + 1] = BasesArrayAway[x]  # NEED TO DO -1,-1 in order to go from front to back of array.
                            BasesArrayAway[0] = True  # Single means first spot is true. Put the person on base after you have moved players
                            team2.players[randomPlayer].AddSingleA()
                            team2.players[randomPlayer].AddHitsA()
                            for a in range(3, 7):
                                if BasesArrayAway[a] == True:
                                    runsAway += 1
                                    BasesArrayAway[a] = False
                            hitSingle = False
                        if hitDouble == True:
                            for x in range(1, -1, -1):
                                BasesArrayAway[x + 2] = BasesArrayAway[x]
                            BasesArrayAway[1] = True  # Double turns the second spot true
                            team2.players[randomPlayer].AddDoubleA()
                            team2.players[randomPlayer].AddHitsA()
                            for a in range(3, 7):
                                if BasesArrayAway[a] == True:
                                    runsAway += 1
                                    BasesArrayAway[a] = False
                            hitSingle = False
                        if hitTriple == True:
                            for x in range(1, -1, -1):
                                BasesArrayAway[x + 3] = BasesArrayAway[x]
                            BasesArrayAway[2] = True  # Triple means the third spot is true
                            team2.players[randomPlayer].AddTripleA()
                            team2.players[randomPlayer].AddHitsA()
                            for a in range(3, 7):
                                if BasesArrayAway[a] == True:
                                    runsAway += 1
                                    BasesArrayAway[a] = False
                            hitSingle = False
                        if hitHomeRun == True:
                            for x in range(1, -1, -1):
                                BasesArrayAway[x + 4] = BasesArrayAway[x]
                            BasesArrayAway[3] = True  # Home run means fourth spot is true.
                            team2.players[randomPlayer].AddHomeRunA()
                            team2.players[randomPlayer].AddHitsA()
                            for a in range(3, 7):
                                if BasesArrayAway[a] == True:
                                    runsAway += 1
                                    BasesArrayAway[a] = False
                            hitSingle = False
                    possession = 1#Alternating possessions 9 times.
        if runsHome == runsAway:
            innings += 1#IF there is a tie, then simply add one more game
        if runsHome>runsAway:
            homeTeamWins+=1
        homeScore.append(runsHome)#Adding the amount of runs in that inning in order to display nicely
        awayScore.append(runsAway)
        home_print1 = ""
        away_print2 = ""
    #print("        1  2  3  4  5  6  7  8  9   F ")  # Label innings and the finals
    #for i in range(0, 9):
       # home_print1 = home_print1 + " " + " " + str(homeScore[i])  # create inning string
        #away_print2 = away_print2 + " " + " " + str(awayScore[i])
    #print("Home :" + home_print1 + ": " + str(sum(homeScore)))
    #print("Away :" + away_print2 + ": " + str(sum(awayScore)))#The amt. of runs show
    #print("Home Team Total Hits:", hitsTotalHome,"H")#H represents the teams total hits
    #print("Away Team Total Hits:", hitsTotalAway,"H")
    print("Stats of your drafted team, the", askTeamName,  "throughout the season")
    print("Name     S    D    T    H    Hits")#Representing the Single, Double, Triple, Homeruns
    team1.show_Stats()
    print("Stats of the opponents team throughout the season")
    print("Name     S    D    T    H    Hits")
    team2.show_StatsA()
    print("The", askTeamName, "Team has won: ", homeTeamWins, "games")
    print("The Away Team has won: ", 10-homeTeamWins, "games")#10 games season
    maxS = 0#In order to determine who is the best in a category
    secondS = 0#Determine who is the second best
    thirdS = 0#Determine who is the third best
    maxD = 0
    secondD = 0
    thirdD = 0
    maxT = 0
    secondT = 0
    thirdT = 0
    maxH = 0
    secondH = 0
    thirdH = 0
    maxHT = 0
    secondHT = 0
    thirdHT = 0
    for x in range(0,8):#go through all players
        maxSingle.append(team1.players[x].single)
        maxSingle.append(team2.players[x].singleA)
        player = random.randint(0,8)
        hitter = names[player]
        for i in maxSingle:
            if i > maxS:
                maxS = i#Working! Basically, going through every persons single runs in the 10 game season in order to find out who is the best.
                maxSingle.remove(maxS)#In order to get thr top three, I am removing the highest score and doing the for loop which finds the highest value again.
        player = random.randint(0, 8)
        hitter2 = names[player]
        for y in maxSingle:
            if y > secondS:
                secondS = y
                maxSingle.remove(secondS)
        player = random.randint(0, 8)
        hitter3 = names[player]
        for r in maxSingle:
            if r > thirdS:
                thirdS = r
                maxSingle.remove(thirdS)
    print("The Best in the Category of Singles is: ",hitter , "with", maxS, "singles")#Displaying the person who is the best
    print("The Second Best in the Category of Singles is: ",hitter2 , "with", secondS, "singles")#Displaying second best
    print("The Second Best in the Category of Singles is: ",hitter3 , "with", thirdS, "singles")#Displaying third best
    for j in range(0,8):
        maxDouble.append(team1.players[j].double)
        maxDouble.append(team2.players[j].doubleA)
        player1 = random.randint(0,8)
        hitter1 = names[player]
        for y in maxDouble:
            if y > maxD:
                maxD = y
                maxDouble.remove(maxD)
        player = random.randint(0, 8)
        hitter2 = names[player]
        for y in maxDouble:
            if y > secondD:
                secondD = y
                maxDouble.remove(secondD)
        player = random.randint(0, 8)
        hitter3 = names[player]
        for r in maxDouble:
            if r > thirdD:
                thirdD = r
    print("The Best in the Category of Doubles is: ",hitter1 , "with", maxD, "doubles")#Displaying the person who is the best
    print("The Second Best in the Category of Doubles is: ",hitter2 , "with", secondD, "doubles")
    print("The Third Best in the Category of Doubles is: ",hitter3 , "with", thirdD, "doubles")
    for o in range(0,8):
        maxTriple.append(team1.players[o].triple)
        maxTriple.append(team2.players[o].tripleA)
        player2 = random.randint(0,8)
        hitter1 = names[player2]
        for z in maxTriple:
            if z>maxT:
                maxT = z
                maxTriple.remove(maxT)
        player = random.randint(0, 8)
        hitter2 = names[player]
        for y in maxTriple:
            if y > secondT:
                secondT = y
                maxTriple.remove(secondT)
        player = random.randint(0, 8)
        hitter3 = names[player]
        for r in maxTriple:
            if r > thirdT:
                thirdT = r
    print("The Best in the Category of Triples is: ", hitter1, "with", maxT, "triples")
    print("The Second Best in the Category of Triples is: ", hitter2, "with", secondT, "triples")
    print("The Third  Best in the Category of Triples is: ", hitter3, "with", thirdT, "triples")
    for e in range(0,8):
        maxHomeRun.append(team1.players[e].homerun)
        maxHomeRun.append(team2.players[e].homerunA)
        player3 = random.randint(0,8)
        hitter1 = names[player3]
        for a in maxHomeRun:
            if a >maxH:
                maxH = a
                maxHomeRun.remove(maxH)
        player = random.randint(0, 8)
        hitter2 = names[player]
        for y in maxHomeRun:
            if y > secondH:
                secondH = y
                maxHomeRun.remove(secondH)
        player = random.randint(0, 8)
        hitter3 = names[player]
        for r in maxHomeRun:
            if r > thirdH:
                thirdH = r
    print("The Best in the Category of Home Runs is: ", hitter1, "with", maxH, "home runs")
    print("The Second Best in the Category of Home Runs is: ", hitter2, "with", secondH, "home runs")
    print("The Third Best in the Category of Home Runs is: ", hitter3, "with", thirdH, "home runs")
    for q in range(0,8):
        maxHits.append(team1.players[q].HTS)
        maxHits.append(team2.players[q].HTSA)
        player4 = random.randint(0,8)
        hitter1 = names[player4]#LEFT OFF
        for b in maxHits:
            if b>maxHT:
                maxHT = b
                maxHits.remove(maxHT)
        player = random.randint(0, 8)
        hitter2 = names[player]
        for y in maxHits:
            if y > secondHT:
                secondHT = y
                maxHits.remove(secondHT)
        player = random.randint(0, 8)
        hitter3 = names[player]
        for r in maxHits:
            if r > thirdHT:
                thirdHT = r
    print("The Best in the Category of Hits is: ", hitter1, "with", maxHT, "hits")
    print("The Second Best in the Category of Hits is: ", hitter2, "with", secondHT, "hits")
    print("The Third Best in the Category of Hits is: ", hitter3, "with", thirdHT, "hits")

    ask = input("Would you like to play again with the same stats? Enter 'yes' or 'no'")#Post Game simulation, allows the user to play again.
    if ask=="yes":
        print("The scores below are the second game which you are allowing to be played")#user choice dependent
        playBaseball(team1, team2, names, askTeamName)
    if ask == "no":
        print("Have an extravagant day")




playBall()


