inputstr = '11622369109'
# '134414861'

aset = set()

def recur(depth, inp, bc):
    print(f'Depth: {depth} Processing {inp}, bc: [{bc}]')
    if depth==4:
        if len(inp)>0:
            return False
        else:
            ret ='.'.join(bc)
            aset.add(ret)
            return 
    if len(inp)>=1 and int(inp[:1]) in range(255):
        recur(depth+1, inp[1:], bc+[inp[:1]])
    if len(inp)>=2 and int(inp[:2]) in range(255):
        recur(depth+1, inp[2:], bc+[inp[:2]])
    if len(inp)>=3 and int(inp[:3]) in range(255):
        recur(depth+1, inp[3:], bc+[inp[:3]])

recur(0, inputstr, [])

print(list(aset))