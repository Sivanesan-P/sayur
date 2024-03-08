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

def play(dice):
            if dice==1 :
                return 1
            elif dice==2:
                return 5
            elif dice==3:
                return 15
            elif dice==4:
                return -15
            elif dice==5:
                return -5
            elif dice==6:
                return -1
                
def main():
    scores=[0,0]
    rolls=[0,0]
    while True:
        for i in range (2):
            dice=random.randint(1, 6)
            rolls[i] +=1
            score=play(dice)
            scores[i]+=score
            if scores[i]==100:
                 print("player ",i+1,"wins after ",rolls[i],"rolls")
                 return

main()


