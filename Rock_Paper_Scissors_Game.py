#Basic Rock,Paper,Scissors game using python
import random
computer_points=0
player_points=0
chances=5
choices=['rock','paper','scissors']
print("Let's start rock,paper,scissors game.")
while(chances>0):
    computer_choice=random.choice(choices)
    player_choice=input("Enter Ur choice: ")
    if player_choice not in choices:
	    print("Enter valid choice!!")
	    continue
    if computer_choice==player_choice:
        print("It's a Tie.")
        chances-=1 
        continue
    if computer_choice=='rock' and player_choice=='paper':
        player_points+=1
        print("You won this turn")
    elif computer_choice=='paper' and player_choice=='scissors':
        player_points+=1
        print("You won this turn")
    elif computer_choice=='scissors' and player_choice=='rock':
        player_points+=1
        print("You won this turn")
    elif player_choice=='rock' and computer_choice=='paper':
        computer_points+=1
        print("You lost this turn")
    elif player_choice=='paper' and computer_choice=='scissors':
        computer_points+=1
        print("You lost this turn")
    elif player_choice=='scissors' and computer_choice=='rock':
        computer_points+=1
        print("You lost this turn")
    chances-=1 
if computer_points==player_points:
    print("The Game is a Tie")
elif player_points>computer_points:
    print("Hurray!! You Won the Game.")
else:
    print("Oops!! You Lost the Game.\nBetter Luck Next Time.")