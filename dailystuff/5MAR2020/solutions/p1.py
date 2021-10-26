dp = [[[-1 for i in range(130)]for j in range(250)]for k in range(250)]

def phi(a, b, c):
    if b==1: return 1
    if dp[a][b][c] != -1: return dp[a][b][c]
    print(a, b, c)
    dp[a][b][c] = sum(phi(a-u, b-1, u) for u in range(c, a//b))
    return dp[a][b][c]

n, k = (int(input()) for i in range(2)) 
print(phi(n, k, 1))
