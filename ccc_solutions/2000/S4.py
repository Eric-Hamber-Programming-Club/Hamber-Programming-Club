#code by Andy Liang

d = int(input())
n = int(input())
clubs = []
for x in range(n):
    clubs.append(int(input()))
    
l = [0 for i in range(d+1)]
 
for i in range(1, len(l)):
    for club in clubs:
        if i-club<0 or l[i-club]==-1:
            continue
        strokes = l[i-club]+1
        if(strokes<l[i] and l[i]>0) or l[i]==0:
            l[i] = strokes
    if l[i]==0:
        l[i] = -1
 
if(l[d]==-1):
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in "+str(l[d])+" strokes.")
