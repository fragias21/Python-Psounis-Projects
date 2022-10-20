board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def board():
    print("+---+---+---+                +---+---+---+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |                | 1 | 2 | 3 |")
    print("+---+---+---+                +---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |                | 4 | 5 | 6 |")
    print("+---+---+---+                +---+---+---+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |                | 7 | 8 | 9 |")
    print("+---+---+---+                +---+---+---+")
    print("")

round = 1
for k in range(1,9):
    X = str(input("ΓΥΡΟΣ " + str(round) + ": " + "ΠΑΙΖΕΙ Ο ΠΑΙΧΤΗΣ Χ, ΔΙΑΛΕΞΕ ΘΕΣΗ= "))
    print("")
    if X == "1" and board[2][0] != " ":
        X = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif X == "1" and board[2][0] == " ":
        board[2][0] = "X"
    if X == "2" and board[2][1] != " ":
        X = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif X == "2" and board[2][1] == " ":
        board[2][1] = "X"
    if X == "3" and board[2][2] != " ":
        X = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif X == "3" and board[2][2] == " ":
        board[2][2] = "X"
    if X == "4" and board[1][0] != " ":
        X = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif X == "4" and board[1][0] == " ":
        board[1][0] = "X"
    if X == "5" and board[1][1] != " ":
        X = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif X == "5" and board[1][1] == " ":
        board[1][1] = "X"
    if X == "6" and board[1][2] != " ":
        X = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif X == "6" and board[1][2] == " ":
        board[1][2] = "X"
    if X == "7" and board[0][0] != " ":
        X = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif X == "7" and board[0][0] == " ":
        board[0][0] = "X"
    if X == "8" and board[0][1] != " ":
        X = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif X == "8" and board[0][1] == " ":
        board[0][1] = "X"
    if X == "9" and board[0][2] != " ":
        X = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif X == "9" and board[0][2] == " ":
        board[0][2] = "X"
    board()
    if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ Χ")
        break
    if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ Χ")
        break
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ Χ")
        break
    if board[2][0] == "X" and board[1][0] == "X" and board[0][0] == "X":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ Χ")
        break
    if board[2][1] == "X" and board[1][1] == "X" and board[0][1] == "X":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ Χ")
        break
    if board[2][2] == "X" and board[1][2] == "X" and board[0][2] == "X":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ Χ")
        break
    if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ Χ")
        break
    if board[2][2] == "X" and board[1][1] == "X" and board[0][0] == "X":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ Χ")
        break
    round += 1
    if round == 10:
        print("!! ΙΣΟΠΑΛΙΑ !!")
        break

    O = str(input("ΓΥΡΟΣ " + str(round) + ": " + "ΠΑΙΖΕΙ Ο ΠΑΙΧΤΗΣ Ο, ΔΙΑΛΕΞΕ ΘΕΣΗ= "))
    print("")
    if O == "1" and board[2][0] != " ":
        O = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif O == "1" and board[2][0] == " ":
        board[2][0] = "O"
    if O == "2" and board[2][1] != " ":
        O = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif O == "2" and board[2][1] == " ":
        board[2][1] = "O"
    if O == "3" and board[2][2] != " ":
        O = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif O == "3" and board[2][2] == " ":
        board[2][2] = "O"
    if O == "4" and board[1][0] != " ":
        O = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif O == "4" and board[1][0] == " ":
        board[1][0] = "O"
    if O == "5" and board[1][1] != " ":
        O = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif O == "5" and board[1][1] == " ":
        board[1][1] = "O"
    if O == "6" and board[1][2] != " ":
        O = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif O == "6" and board[1][2] == " ":
        board[1][2] = "O"
    if O == "7" and board[0][0] != " ":
        O = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif O == "7" and board[0][0] == " ":
        board[0][0] = "O"
    if O == "8" and board[0][1] != " ":
        O = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif O == "8" and board[0][1] == " ":
        board[0][1] = "O"
    if O == "9" and board[0][2] != " ":
        O = str(input("ΔΙΑΛΕΞΕ ΑΛΛΗ ΘΕΣΗ= "))
    elif O == "9" and board[0][2] == " ":
        board[0][2] = "O"
    board()
    if board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ O")
        break
    if board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ 0")
        break
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ 0")
        break
    if board[2][0] == "O" and board[1][0] == "O" and board[0][0] == "O":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ 0")
        break
    if board[2][1] == "O" and board[1][1] == "O" and board[0][1] == "O":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ 0")
        break
    if board[2][2] == "O" and board[1][2] == "O" and board[0][2] == "O":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ 0")
        break
    if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ 0")
        break
    if board[2][2] == "O" and board[1][1] == "O" and board[0][0] == "O":
        print("ΝΙΚΗ ΓΙΑ ΤΟΝ ΠΑΙΧΤΗ 0")
        break
    round += 1
    if round == 10:
        print("!! ΙΣΟΠΑΛΙΑ !!")
        break
