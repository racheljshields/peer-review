# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Rachel Shields
# Creation Date: 23SEP2023
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time


def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
    while cave !="1" and cave !='2':
        #Correct the indentations
        #while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()
      
    return cave
    #Correct 'caves' to the correct variable 'cave'
    #return caves

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
      print('Gobbles you down in one bite')  
      #Add parentheses to the print function
      #print 'Gobbles you down in one bite!'

displayIntro()
caveNumber=chooseCave()
#Correct 'choosecave()' to 'chosenCave'
#caveNumber = choosecave()
checkCave(caveNumber)
    
print("Thanks for playing")