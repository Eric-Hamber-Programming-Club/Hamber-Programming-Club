n = int(input())
j, k = map(int, input().split()) 
face = [*"".join([input() for _ in range(k)])]
for i in range(j//2, j*k, j):
    face[i] = face[i]*(n - j)

for i in range(0, j*k, j):
    print("".join(face[i:i+j]))





