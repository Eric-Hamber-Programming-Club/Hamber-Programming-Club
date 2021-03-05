matrix = []
chr_to_int = dict((chr(x+65), x) for x in range(10))
out_coords = []
equeue = {}

for i in range(10):
    j = input().split()
    k = []
    for pos, val in enumerate(j):
        try:
            n = int(val)
            k.append(n)
        except:
            k.append("*")
            g = (i, pos)
            out_coords.append(g)
            n = [(chr_to_int[c], int(d) - 1) for c, d in val.split("+")]

            equeue[g] = n
    matrix.append(k)

flag = True
while flag:
    flag = False
    delq = []
    for pos, i in enumerate(out_coords):
        b = equeue[i]
        for e, ti in enumerate(b):
            try:
                r, c = ti
                if matrix[r][c] != "*":
                    b[e] = matrix[r][c]
            except: pass
        if all(type(n) == int for n in equeue[i]):

            flag = True
            mc, mr = i
            matrix[mc][mr] = sum(equeue[i])
            delq.append(pos)
    if flag:
        for de in sorted(delq, reverse = True):
            del out_coords[de]
print("\n".join(" ".join(map(str, k)) for k in matrix))

