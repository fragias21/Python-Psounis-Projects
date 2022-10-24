#randrange
from random import seed
from random import randrange
from datetime import datetime
seed(datetime.now())

#globals
score = [{  "ones": -1,
            "twos": -1,
            "threes": -1,
            "fours": -1,
            "fives": -1,
            "sixes": -1 },
        {   "ones": -1,
            "twos": -1,
            "threes": -1,
            "fours": -1,
            "fives": -1,
            "sixes": -1 }]

dices = [1,2,3,4,5,6]
Roll = []

#functions
def roll_dices(Roll):
    if len(Roll) == 0:
        dif = 5
    else: 
        dif = len(Roll)
        Roll.clear()
    for i in range(dif):
        pos = randrange(len(dices))
        Roll.append(dices[pos])
    Roll.sort()
    return Roll

def player_turn():
    choos_dices = []
    Roll = []
    Roll = roll_dices(Roll)
    cnt = 1
    print("\n" + "="*15 + " Roll " + str(cnt) + " " + "="*15)
    print(f"Roll: {Roll}")
    print(f"Choosen dices: {choos_dices}")
    choice = input("Choose 1 dice to keep or pass: ")
    while cnt != 3:
        while choice != "pass":
            choice = int(choice)
            choos_dices.append(choice)
            Roll.remove(choice)
            print("="*15 + " Roll " + str(cnt) + " " + "="*15)
            print(f"Roll: {Roll}")
            print(f"Choosen dices: {choos_dices}")
            choice = input("Choose 1 dice to keep or pass: ")
        if len(choos_dices) == 5:
            choos_dices.sort()
            break
        Roll = roll_dices(Roll)
        cnt += 1
        print("="*15 + " Roll " + str(cnt) + " " + "="*15)
        print(f"Roll: {Roll}")
        print(f"Choosen dices: {choos_dices}")
        if cnt == 3:
            choos_dices += Roll
            choos_dices.sort()
        else:
            choice = input("Choose 1 dice to keep or pass: ")
    print(f"\nFinal dices: {choos_dices}")
    return choos_dices

def translate_name(s):
    if s=="ones":
        return 1
    elif s=="twos":
        return 2
    elif s=="threes":
        return 3
    elif s=="fours":
        return 4
    elif s=="fives":
        return 5
    elif s=="sixes":
        return 6

def player_picks(player, dice):
    print("You can store your dices as: ", end="")
    picks = []
    for key, value in score[player].items():
        if value == -1:
            if key == "sixes": 
                print(key, end=". ")
                picks += [key]
            else:
                print(key, end=", ")
                picks += [key]
    while True:
        choice = input("\nPick a choice: ")
        if choice not in picks:
            print("Wrong choice!")
            continue
        else:
            key_val = translate_name(choice)
            score[player][choice] = dice.count(key_val) * key_val
            return

def total_score(player):
    ts = 0
    for key, value in score[player].items():
        if score[player][key] == -1:
            score[player][key] = 0
    for key, value in score[player].items():
        ts += score[player][key]
    return ts
    
def print_card(player):
    print(f"PLAYER's {player + 1} CARD")
    if score[player]["ones"] == -1:
        print("ones: " )
    else:
        print(f"ones: {score[player]['ones']}")
    
    if score[player]["twos"] == -1:
        print("twos: " )
    else:
        print(f"twos: {score[player]['twos']}")
    
    if score[player]["threes"] == -1:
        print("threes: " )
    else:
        print(f"threes: {score[player]['threes']}")
        
    if score[player]["fours"] == -1:
        print("fours: " )
    else:
        print(f"fours: {score[player]['fours']}")
        
    if score[player]["fives"] == -1:
        print("fives: " )
    else:
        print(f"fives: {score[player]['fives']}")
        
    if score[player]["sixes"] == -1:
        print("sixes: " )
    else:
        print(f"sixes: {score[player]['sixes']}\n")
    
#main
print("~"*20 + " Let's play Yahtzee !! " + "~"*20)
for round in range(1,13):
    if round%2 == 1:
        player = 0
        player_p = 1
    else:
        player = 1
        player_p = 2
    print("\n" + "~"*25 + " Round " + str(round) + ": Player's " + str(player_p) + " turn ! " + "~"*25)

#player's round
    dice = player_turn()

#player's final choices
    player_picks(player, dice)
    
#print scores + winner
    if round==12:
        t_s_1 = total_score(0)
        t_s_2 = total_score(1)
        print("\n" + "="*25 + " Final Score " + "="*25)
        print_card(0)
        print("Player's 1 Total Score = " + str(t_s_1) + "\n")
        print_card(1)
        print("Player's 2 Total Score = " + str(t_s_2) + "\n")
        if t_s_1 > t_s_2:
            print("Player 1 WINS !")
        elif t_s_1 < t_s_2:
            print("Player 2 WINS !")
        else:
            print("DRAW !!!")
    else:
        print("\n" + "="*25 + " Score " + "="*25)
        print_card(0)
        print("")
        print_card(1)      
