from random import seed
from random import randrange
from datetime import datetime
seed(datetime.now())

numbers = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
types = ["heart", "diamond", "spade", "club"]
i = 1
cardi = []
all_cards = []
for k in numbers:
    for l in types:
        cardi=[k , l]
        all_cards.append(cardi)
        i += 1

PLAYER = []
COMPUTER = []
total_score_player = 0
total_score_computer = 0
score_player = 0   
score_computer = 0
round = 0
next_game = "y"   

def next_card_player():
    fiqs = ["jack", "queen", "king"]
    card_no = randrange(0, len(all_cards))
    PLAYER.append(all_cards.pop(card_no))
    print("Card = " + str(PLAYER[len(PLAYER)-1][0]))            
    if PLAYER[len(PLAYER)-1][0] == "ace":
        y = int(input("It's ACE: 1 or 11?: "))
    elif PLAYER[len(PLAYER)-1][0] in fiqs :
        y = 10
    else: y = int(PLAYER[len(PLAYER)-1][0])
    return y        

def next_card_computer(score_computer):
    fiqs = ["jack", "queen", "king"]
    card_no = randrange(0, len(all_cards))
    COMPUTER.append(all_cards.pop(card_no))
    print("Card = " + str(COMPUTER[len(COMPUTER)-1][0]))          
    if COMPUTER[len(COMPUTER)-1][0] == "ace" and score_computer <=10:
        y = 11
    elif COMPUTER[len(COMPUTER)-1][0] == "ace" and score_computer >= 11:
        y = 1
    elif COMPUTER[len(COMPUTER)-1][0] in fiqs :
        y = 10
    else: y = int(COMPUTER[len(COMPUTER)-1][0])
    return y        

while next_game == "y":
    round += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~ ROUND " + str(round) + " ~~~~~~~~~~~~~~~~~~~~~~~")
    while score_player < 22:
        score_player += next_card_player()
        print("Player's score = " + str(score_player))    
        if score_player == 21:
            break
        elif score_player > 21:
            break
        else:
            x = input("Draw or stop ?: ")
            if x == "stop":
                print("Player's score = " + str(score_player))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
                print("Computer plays now")
                while score_computer <= 16:
                    score_computer += next_card_computer(score_computer)
                    print("Computer's score = " + str(score_computer)) 
                break
            else: 
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")           

    print("========================================================") 
    print("Player's score = " + str(score_player))    
    print("Computer's score = " + str(score_computer))      
    if score_player == 21:
        print("Player BLACK JACK !!    YOU WIN !!!")
        total_score_player += 1
    elif score_player > 21:
        print("You lose... Computer wins !")
        total_score_computer += 1    
    elif score_computer > 21:
        print("YOU WIN !!!")
        total_score_player += 1
    elif score_computer == 21:
        print("Computer BLACK JACK !!    You lose...")
        total_score_computer += 1
    elif score_computer < score_player:
        print("YOU WIN !!!")
        total_score_player += 1
    elif score_computer == score_player:
        print("DRAW ! You lose... Computer wins !")
        total_score_computer += 1
    else:
        print("You lose... Computer wins !")
        total_score_computer += 1
    print("Total score: " + "Player " + str(total_score_player) + " - " + str(total_score_computer) + " Computer")
    next_game = str(input("Do you want to play again? (y-yes or n-no): "))
    
    numbers = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    types = ["heart", "diamond", "spade", "club"]
    i = 1
    cardi = []
    all_cards = []
    for k in numbers:
        for l in types:
            cardi=[k , l]
            all_cards.append(cardi)
            i += 1

    PLAYER = []
    COMPUTER = []
    score_player = 0   
    score_computer = 0
    
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("FINAL score: " + "Player " + str(total_score_player) + " - " + str(total_score_computer) + " Computer")
