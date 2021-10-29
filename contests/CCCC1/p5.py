import sys
input = sys.stdin.readline
n = int(input())
t = int(input())
di = 0
for i in range(n):
    if i<2:
        di += 9
    else:
        di = (di-7)*3 + 2
        
for i in range(t):
    if int(input())>di:
        print("NO")
    else:
        print("YES")
