pyr = [
  [8],
  [7,7],
  [3,3,5],
  [1,7,3,3],
  [4,3,6,5,7],
  [2,2,6,7,3,7],
  [9,6,6,4,4,6,6],
  [7,1,7,7,2,5,8,1],
  [7,1,5,4,6,7,1,4,2],
  [9,5,3,4,1,1,3,7,5,3]
]

col = 0 
row = 0
pyr2 = []
for row in range(len(pyr)):
    if row==0:
        pyr2.append([pyr[row][0]])
    else:
        pyr2.append([pyr2[row-1][0]+pyr[row][0]])
        for col in range(len(pyr[row])):
            if col>0:
                app = 0
                min = pyr2[row-1][col-1]
                min2 = 0
                try:
                    min2 = pyr2[row-1][col]
                    if min2<min:
                        min = min2
                except:
                    min = min
                finally: 
                    pyr2[row].append(min+pyr[row][col])

print(pyr2)
       

