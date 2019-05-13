import random
import numpy as np
import matplotlib.pyplot as plt
def makeBirthday():
 lowDay = 1
 highDay = 365
 yes=0
 no=0
 for i in range(1000):
     match=False
     genBirthday = np.random.random_integers(lowDay, highDay, 30)#Generating 30 ran. birthdays
     for i in range(30):
         for x in range(i+1,30):
             if genBirthday[i]==genBirthday[x]:
                 match=True#Turning a boolean on, in order to count the yes and nos
     if match==True:
         yes=yes+1#So everytime there is match, we increase the count by one and move to next classroom
     else:
         no=no+1
 print(yes)
 print(no)
 array=[]
 for x in range(yes):
     array.append(0)#Appending each classes result
 for y in range(no):
     array.append(1)
 objects = ('YES', 'NO')
 y_pos = np.arange(len(objects))
 performance = [yes,no]
 plt.bar(y_pos, performance, align='center')#Learned how to do this through: https://pythonspot.com/matplotlib-bar-chart/
 plt.xticks(y_pos, objects)
 plt.ylabel('Number of Classes')
 plt.xlabel('Do they Share Birthdays or not?')
 plt.title("Classes That Have or Don't Have Same Birthdays")
 plt.show()


makeBirthday()
