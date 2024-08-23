inp = [0,0,0,0,
0,0,0,0,
0,0,1,0,
1,0,0,0,
0,0,0,1,
0,0,0,0,
0,0,1,0,]

cols = 4
rows=7

out = [1]

for i in range(len(inp)):
    ret = 0
    curcol = i % cols
    if inp[i]==0:
        if curcol>0:
            if inp[i-1]==0 and out[i-1]>0:
                ret += out[i-1] if out[i-1] else 1
        else:
            out
        if i>cols:
            if inp[i-cols]==0 and out[i-cols]>0:
                ret += out[i-cols] if out[i-cols] else 1
        else:
    out += [ret]

print(out)