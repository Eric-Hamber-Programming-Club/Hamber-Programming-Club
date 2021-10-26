import os

c = ["0" for i in range(56)]
c[7::8] = ["$"]*7

def check4():
    for i in range(7):
        row = "".join(c[i*8:i*8+7])
        col = "".join(c[i::8])
        if "1111" in row or "1111" in col or "2222" in row or "2222" in col:
            return True
        diag1 = "".join(c[i::7])
        diag2 = "".join(c[i::9])

        if "1111" in diag1 or "1111" in diag2 or "2222" in diag1 or "2222" in diag2:
            return True

def printboard():
    os.system("cls")
    h = ["-", "@", "O"]
    for i in range(7):
        row = c[i*8:i*8+8]
        for j in row[:-1]:
            print(h[int(j)], end="    ")
        print()

    print("*"*31)
    print(*range(1, 8), sep="    ")
        

player = 1
printboard()
while True:
    col = input(f"Player {player}'s turn: ")
    if col not in ["1", "2", "3", "4", "5", "6", "7"]:
        printboard()
        print("Invalid input! Try again.")
        continue

    col = 47 + int(col)
    fl = True

    while c[col] != '0':
        col -= 8
        if col < 0:
            printboard()
            print("Invalid input!")
            break
    else:
        fl = False

    if fl:
        continue

    c[col] = str(player)
    printboard() 

    if check4():
        print(f"Player {player} wins!")
        break

    if player==1: player=2
    else: player=1


