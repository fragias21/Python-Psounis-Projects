from random import seed
from random import randrange
from datetime import datetime 
seed(datetime.now())

source = ["tree", "dog", "car", "children", "ball", "human", "computer"]
hidden_word = source[randrange(len(source))]
max_rounds = 10
tries = 1
round = 1
print("")
#print(hidden_word + " #test only")    #test only

len_hidden_word = len(hidden_word)
games_word = ("_")*len_hidden_word
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessed_letters = []
print("")
print("Let's play KREMALA ! You have " + str(max_rounds) + " tries !","\n")

while games_word.find("_") != -1 and tries < max_rounds+1:
    print("~"*40 + " " + "ROUND " + str(round) + " " + "~"*40,"\n")
    print("Tries left: " + str(max_rounds-(tries-1)),"\n")
    print("Used letters: " + str(guessed_letters),"\n")
    print("Available letters: " + str(alphabet),"\n")
    print("Game's word: " + games_word,"\n")
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess)!=1:
            print("ERROR. Please give ONE letter !")
        elif not guess.isalpha():
            print("ERROR. Please give LETTER !")
            
        elif guess in guessed_letters:
            print("ERROR ! You have already used this letter !")
        else:
            break
    print("")
    guessed_letters.append(guess)
    alphabet.remove(guess)            
    if guess in hidden_word:
        pos = -1
        pos_list = []
        lpos = hidden_word.rfind(guess)
        while pos != lpos:
            pos = hidden_word.find(guess, pos+1)
            pos_list.append(pos)
        print("The letter " + guess + " exists " + str(len(pos_list)) + " times !","\n")
        for i in pos_list:
            games_word = games_word[:i] + guess + games_word[i+1:]
    else:
        print(str(guess) + " doesn't exist !","\n")
        tries += 1
    round += 1
if tries == 11:
    print("You didn't won...  :( ")        
else:    
    print("C O N G R A T U L A T I O N S !!!  You won with " + str(tries-1) + " wrongs !")
  
