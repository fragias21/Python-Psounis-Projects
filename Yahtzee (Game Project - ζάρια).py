#randrange
from random import seed
from random import randrange
from datetime import datetime
seed(datetime.now())

#globals
score = [
    {
        "ones": -1,
        "twos": -1,
        "threes": -1,
        "fours": -1,
        "fives": -1,
        "sixes": -1
    },
    {   "ones": -1,
        "twos": -1,
        "threes": -1,
        "fours": -1,
        "fives": -1,
        "sixes": -1
    }
]

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
    print("="*15 + "Roll " + str(cnt) + "="*15)
    print(f"Roll: {Roll}")
    print(f"Choosen dices: {choos_dices}")
    choice = input("Choose 1 dice to keep or pass: ")
    while cnt != 3:
        while choice != "pass":
            choice = int(choice)
            choos_dices.append(choice)
            Roll.remove(choice)
            print("="*15 + "Roll " + str(cnt) + "="*15)
            print(f"Roll: {Roll}")
            print(f"Choosen dices: {choos_dices}")
            choice = input("Choose 1 dice to keep or pass: ")
        Roll = roll_dices(Roll)
        cnt += 1
        print("="*15 + "Roll " + str(cnt) + "="*15)
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
            print(key, end=", ")
            picks += [key]
    while True:
        choice = input("\npick a choice: ")
        if choice not in picks:
            print("Wrong choice!")
            continue
        else:
            key_val = translate_name(choice)
            score[player][choice] = dice.count(key_val) * key_val
            return

#player's round
dice = player_turn()

#player's final choices
player_picks(0, dice)
print("\n" + "="*25 + " Player's Score " + "="*25)
print(score)

#main game
