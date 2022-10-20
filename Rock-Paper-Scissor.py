from random import seed
from random import randrange
from datetime import datetime
from re import M # all 3 at the beginning
seed(datetime.now()) # once, before randit call

list = ("rock", "paper", "scissor")
wins_pl = 0
wins_pc = 0

while wins_pl != 3 and wins_pc != 3:
    x = str(input("Παίζει ο παίχτης: "))
    while x != "rock" and x != "paper" and x != "scissor":
        x = str(input("Παίχτη, δώσε σωστή επιλογή: "))
    for k in range(1):
        m = randrange(len(list))
        y = list[m]
    print("Παίζει ο υπολογιστής: " + str(y))
    if x == "rock" and y == "paper":
        wins_pc += 1
        print("Νίκη για τον ΥΠΟΛΟΓΙΣΤΗ !")
    elif x == "rock" and y == "scissor":
        wins_pl += 1   
        print("Νίκη για τον ΠΑΙΧΤΗ !")
    elif x == "rock" and y == "rock":    
        print("ΙΣΟΠΑΛΙΑ !")    
    elif x == "paper" and y == "rock":
        wins_pl += 1   
        print("Νίκη για τον ΠΑΙΧΤΗ !")
    elif x == "paper" and y == "scissor":
        wins_pc += 1
        print("Νίκη για τον ΥΠΟΛΟΓΙΣΤΗ !")
    elif x == "paper" and y == "paper":    
        print("ΙΣΟΠΑΛΙΑ !")   
    elif x == "scissor" and y == "rock":
        wins_pc += 1
        print("Νίκη για τον ΥΠΟΛΟΓΙΣΤΗ !")
    elif x == "scissor" and y == "paper":
        wins_pl += 1   
        print("Νίκη για τον ΠΑΙΧΤΗ !")
    elif x == "scissor" and y == "scissor":    
        print("ΙΣΟΠΑΛΙΑ !")
    print("ΣΚΟΡ: Παίχτης " + str(wins_pl) + " - " + str(wins_pc) + " Υπολογιστής")

if wins_pl > wins_pc:
    print("Τελικός νικητής ο ΠΑΙΧΤΗΣ !!!")
else:
    print("Τελικός νικητής ο ΥΠΟΛΟΓΙΣΤΗΣ !")