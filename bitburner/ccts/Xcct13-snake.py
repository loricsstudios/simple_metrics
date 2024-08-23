inp = [
        [31,13,42,34,22,24],
        [44,10,29,19,21,16],
        [46, 1,44,35,36,46],
        [32,21,38, 5,18,34],
        [ 8, 4,14,46,50,10],
        [39,21,46,24, 5,31],
        [40,17,40,21, 5,18],
        [41,27,39,43,48,14],
        [24,24,15,33,30,27],
        [43,42, 3,30,23,21],
        [23,23,45,35,14,38],
    ]
inp3 = [
    [1, 2, 3, 4 ],
    [5, 6, 7, 8 ],
    [9, 10,11,12],
    [13,14,15,16]
]

inp4 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rows = len(inp)
cols = len(inp[0])

print(f'Rows: {rows} cols: {cols}')

out = []

minx = 0
miny = 0
maxx = cols-1
maxy = rows-1

visited = set()
allvis=False
vis = ()

while (allvis==False):
    for i in range(minx, maxx+1):
        vis = (miny,i)
        print(f'right visiting: {vis}')
        if vis in visited:
            print('crossing detected')
            allvis = True
            break
        out += [inp[vis[0]][vis[1]]] # topleft right
        visited.add(vis)
    miny+=1
    for i in range(miny,maxy+1):
        vis = (i, maxx)
        print(f'down visiting: {vis}')
        if vis in visited:
            print('crossing detected')
            allvis = True
            break
        out += [inp[vis[0]][vis[1]]] # topright down
        visited.add(vis)
    maxx-=1
    for i in range(minx, maxx+1-minx):
        vis = (maxy,maxx-i)
        print(f'left visiting: {vis}')
        if vis in visited:
            print('crossing detected')
            allvis = True
            break
        out += [inp[vis[0]][vis[1]]] # bottomright left
        visited.add(vis)
    maxy-=1
    for i in range(miny,maxy+1-miny):
        vis = (maxy-i, minx)
        print(f'up visiting: {vis}')
        if vis in visited:
            print('crossing detected')
            allvis = True
            break
        out += [inp[vis[0]][vis[1]]] # bottomleft up
        visited.add(vis)
    minx+=1

print(out)