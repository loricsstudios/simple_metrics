cols = 3
rows = 5

paths = 0

def dive(c, r, bc):
    global paths
    if c<cols:
        dive(c+1, r, bc+'r')
    if r<rows:
        dive(c, r+1, bc+'d')
    if c==cols and r==rows:
        print(bc)
        paths+=1

dive(1,1,'')
print(f'Unique paths: {paths}')
