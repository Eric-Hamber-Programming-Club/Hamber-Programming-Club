 n = int(input())

for i in range(n):
    c = int(input())
    if not c%11 or not c%111:
        print("YES")
    else:
        while c > 111:
            c -= 111
            if not c%11:
                print("YES")
                break
        else:
            print("NO")
