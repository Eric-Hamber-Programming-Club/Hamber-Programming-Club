n, s = map(int, input().split())
b = [*map(int, input().split())]

lmax = 0
rmax = 2*s
pins = int((s+1)*(s/2))
p = pins

for i in b:
    if i < s:
        lmax = max(lmax, i)
    elif i > s:
        rmax = min(rmax, i)
    else:
        pins = 0

if pins:
    pl = [0,0]

    if lmax in b:
       pins -= int((lmax+1)*(lmax/2))
       pl[0]=1

    if rmax in b:
        rmax = (2*s)-rmax
        pins -= int((rmax+1)*(rmax/2))
        pl[1]=1

    if all(pl):
        base = s - (rmax+lmax)
        if base < 0:
            base = abs(base)
            pins += int((base+1)*(base/2))

print(p-pins)







