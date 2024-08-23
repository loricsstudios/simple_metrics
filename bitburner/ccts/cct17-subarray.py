import functools
inp = [-9,2,-5,-1,0,10,9,6,-7,5,3,-7,1,-5,-7,7,-9,-3,4,-8,-8,-2,-2,-4,3,10,-5,6,-8,1,-7,-4,10,-2,-5,10,3,-10,8,0]

max = 0
maxl = []
for b in range(len(inp)):
    for e in range(len(inp)):
        if e>b:
            test = inp[b:e]
            # using reduce to compute sum of list
            # print(f'Testing inp: {test}')
            # print("The sum of the list elements is : ", end="")
            sum = functools.reduce(lambda a, b: a+b, test)
            # print(sum)
            if sum>max:
                max = sum
                maxl = test

print(f'Maximum sum: {max}, coming from subarray: {maxl}')
            
