#problem adapted from https://codeforces.com/contest/1427/problem/A

n = int(input())

for i in range(n):
    k = input()
    a = list(map(int, input().split()))
    
    if sum(a)==0:
        print(-1)
        continue
    
    o = [elem for elem in a if elem>0]
    p = [elem for elem in a if elem<0]

    if sum(a) > 0:
        ans = o+p+[0 for z in range(a.count(0))]
        print(" ".join(map(str, ans)))
        
    elif sum(a) < 0:
        ans = p+o+[0 for z in range(a.count(0))]
        print(" ".join(map(str, ans)))
