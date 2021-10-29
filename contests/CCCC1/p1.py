n = int(input())
c = int(input())
ans = n//c
if n%c > 0: ans += 1
print(ans)

#one-line solution
#print(-(-n//c))

