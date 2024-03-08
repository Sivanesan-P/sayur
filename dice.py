# Two player dice game.
# Each player will roll the die (numbers from 1 to 6)
# Points are added to each roll.
# 1 - 1 pt
# 2 - 5 pts
# 3 - 15 pts
# 4 - (-15) pts
# 5 - (-5) pts
# 6 - (-1) pts

# Find which player scores 100 first and how many time they had to roll the die.
# Hint - use random numbers to generate the die (no need to get user input)
# Use Arrays and while loop.
import random

def dice():
    playerA=0
    playerB=0
    cha=0
    while True:
        dice=random.randint(1, 6)
        cha+=1
        if cha%2==1:
            if dice==1:
                playerA+=1
            elif dice==2:
                playerA+=5
            elif dice==3:
                playerA+=15
            elif dice==4:
                playerA-=15
            elif dice==5:
                playerA-=5
            elif dice==6:
                playerA-=1
        elif cha%2==0:
            if dice==1:
                playerB+=1
            elif dice==2:
                playerB+=5
            elif dice==3:
                 playerB+=15
            elif dice==4:
                playerB-=15
            elif dice==5:
             playerB-=5
        elif dice==6:
             playerB-=1
        if playerA==100:
            print("point of a: ",playerA)
            print("point of b: ",playerB)
            print("player A is a winner")
            break
        elif playerB==100:
            print("point of a: ",playerA)
            print("point of b: ",playerB)
            print("player B is a winner")
            break

dice()

