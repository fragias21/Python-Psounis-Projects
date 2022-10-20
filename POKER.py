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

player_1 = []
player_2 = []
for m in range(1,11):
    if m % 2 == 0:
        c1 = randrange(0, len(all_cards))
        player_1.append(all_cards.pop(c1))
    else:
        c2 = randrange(0, len(all_cards))
        player_2.append(all_cards.pop(c2))
player_1.sort()
player_2.sort()
print("Player's 1 cards: " + str(player_1))
print("Player's 2 cards: " + str(player_2))

cnt = 0
for card in player_1:
    if card[0] == 'ace':
        cnt += 1
if cnt == 4: print("ΚΑΡΕ ΤΟΥ ΑΣΣΟΥ Ο ΠΑΙΧΤΗΣ 1")

cnt = 0
for card in player_2:
    if card[0] == 'ace':
        cnt += 1
if cnt == 4: print("ΚΑΡΕ ΤΟΥ ΑΣΣΟΥ Ο ΠΑΙΧΤΗΣ 2")

hand_numbers_1 = []
for card in player_1:
    if card[0] == 'ace':
        hand_numbers_1.append(1)
    elif card[0] == 'jack':
        hand_numbers_1.append(11)
    elif card[0] == 'queen':
        hand_numbers_1.append(12)
    elif card[0] == 'king':
        hand_numbers_1.append(13)
    else:
        hand_numbers_1.append(int(card[0]))
hand_numbers_1.sort()

hand_numbers_2 = []
for card in player_2:
    if card[0] == 'ace':
        hand_numbers_2.append(1)
    elif card[0] == 'jack':
        hand_numbers_2.append(11)
    elif card[0] == 'queen':
        hand_numbers_2.append(12)
    elif card[0] == 'king':
        hand_numbers_2.append(13)
    else:
        hand_numbers_2.append(int(card[0]))
hand_numbers_2.sort()

cnt = 0
for i in range(4):
    if hand_numbers_1[i]+1 == hand_numbers_1[i+1]:
        cnt += 1
if cnt == 5:
    print("ΚΕΝΤΑ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ 1")

for i in range(4):
    if hand_numbers_2[i]+1 == hand_numbers_2[i+1]:
        cnt += 1
if cnt == 5:
    print("ΚΕΝΤΑ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ 2")
    