import os

c = ["0" for i in range(49)]

def check4():
    for i in range(7):
        row = "".join(c[i*7:i*7+7])
        col = "".join(c[i::7])
        if "1111" in row or "1111" in col or "2222" in row or "2222" in col:
            return True

def printboard():
    os.system("cls")
    h = ["-", "@", "O"]
    print(c)
    for i in range(7):
        row = c[i*7:i*7+7]
        for j in row:
            print(h[int(j)], end="    ")
        print()

    print("*"*31)
    print(*range(1, 8), sep="    ")
        

player = 1
printboard()
while True:
    col = input(f"Player {player}'s turn: ")
    # validate input
    if col not in ["1", "2", "3", "4", "5", "6", "7"]:
        printboard()
        print("Invalid input! Try again.")
        continue

    # mathematically derive 
    col = 41 + int(col)
    fl = True

    # drop in game piece to highest unoccupied column
    while c[col] != '0':
        col -= 7
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


