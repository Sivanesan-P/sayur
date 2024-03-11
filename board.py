# Write an app for the follwoing two player game. You have a 6 x 6 board. 
# Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
# who rolled the dice.
# When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
# If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
# The player who gets 5 points first wins the game. 

import random

playerA=0
playerB=0
def main():
    global board
    global board
    global playerB
    global playerA
    row=6
    col=6
    board=[[0 for i in range(0,row)] for j in range(0,col)]
    for i in range(0,100):
        for j in range (0,col):
            if j%2==1:
                dice("A")
                if playerA==6:
                    print("player A wins")
                    return
            elif j%2==0:
                dice("B")
                if playerB==6:
                    print("player B wins")
                    return

def dice(char):
    global board
    global playerB
    global playerA
    dice1=random.randint(1, 6)
    dice2=random.randint(1, 6)
    if board[dice1-1][dice2-1]=="A" and char=="B":
        playerB+=1
    elif board[dice1-1][dice2-1]=="B" and char=="A":
        playerA+=1
    board[dice1-1][dice2-1]=char
       
main()
for row in board:
    for column in row:
        print(column,end=" ")
    print("\n")

print("point of player A:  ",playerA)
print("point of player B:  ",playerB) 