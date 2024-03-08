# Problem #1
# Play the game Rock Papar Scissors with the computer.
# Play it three times and best of three wins. 
# If you win, print your name in color (look for a python package to do this)
# Hint - Use random number generation
import random

list=["Rock","Paper","Scissors"]
bot=random.choice(list)
count=0
count1=0
you=" "
while True:
    print('1.rock')
    print("2.paper")
    print("3.scissors")
    print("4.exit")
    opt=int(input("enter your choice: "))
    if opt==1:
        you=list[0]
    elif opt==2:
        you=list[1]
    elif opt==3:
        you=list[2]
    else:
        break
    if ((you=="Rock" and bot=="Scissors") or (you=="Paper" and bot=="Rock") or (you=="Scissors" and bot=="Paper") ):
        print("you:",you)
        print("bot:",bot)
        print("you win")
        count+=1
    elif you==bot:
        print("you:",you)
        print("bot:",bot)
        print("draw")
    else:
        print("you:",you)
        print("bot:",bot)
        print("bot win")
        count1+=1
    if count==3:
        print("you have win the game")
    elif count1==3:
        print("bot have wine the game")