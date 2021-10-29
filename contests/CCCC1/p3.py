N = int(input())
k = input()
ans = 0
for i in range(N-1):
    if k[i]==k[i+1]:
        ans+=1

print(ans)
