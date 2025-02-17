import random

print("rock ....")
print("paper ....")
print("scissor ....")

commove=""
Player1_score=0
Player2_score=0

while True:
    com=random.randint(1,3)
    if com==1:
        commove="rock"
    elif com==2:
        commove="scissor"
    elif com==3:
        commove="paper"

    print(f"Player One : {Player1_score} || Player two : {Player2_score}")
    print("-------------------------------------")
    Player1=input("Player 1 Enter Your Choise : ")
    print("Player 2 Enter Your Choise :",commove)


    if Player1 =="q" or commove =="q":
        break
    elif Player1==commove:
        print("Draw....")
    elif Player1=="rock" and commove=="paper":
        print("Player 2 Wins....")
        Player2_score+=1
    elif Player1=="rock" and commove=="scissor":
        print("Player 1 Wins....")
        Player1_score+=1
    elif Player1=="paper" and commove=="rock":
        print("Player 1 Wins....")
        Player1_score+=1
    elif Player1=="paper" and commove=="scissor":
        print("Player 2 Wins....")
        Player2_score+=1
    elif Player1=="scissor" and commove=="rock":
        print("Player 2 Wins...")
        Player2_score+=1
    elif Player1=="scissor" and commove=="paper":
        print("Player 1 Wins....")
        Player1_score+=1
    if Player1_score == 3:
        print("Player 1 Win The Game!!!!!")
        break
    elif Player2_score==3:
        print("Player 2 Win The Game!!!!!")
        break

print("-------------------------------------")
print(f"Player One : {Player1_score} || Player two : {Player2_score}")