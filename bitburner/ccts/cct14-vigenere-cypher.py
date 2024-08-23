from pprint import pprint

square = {

}

def rotated(num):
    return chr(ord('A')+num % 26)

for row  in range(26):
    square[chr(ord('A')+row)] = {}
    for column in range(26):
        square[chr(ord('A')+row)][chr(ord('A')+column)] = rotated(row+column)

# pprint(square) #debug

# def 

# inputdata = ["FRAMEMACROSHELLMEDIATRASH", "COMPUTING"]
# inputdata = ["MEDIAVIRUSPRINTMACROENTER", "KEYWORD"]
# inputdata = ["ENTERTRASHEMAILPASTEDEBUG", "COMPUTER"] 
# inputdata = ["LOGINPOPUPMOUSEQUEUESHIFT", "FLOWCHART"] 
# inputdata = ["VIRUSPASTESHELLSHIFTPOPUP", "EXABYTE"] 
# inputdata = ["MEDIAVIRUSLOGINLOGICPRINT", "COMPUTER"]
# inputdata = ["EMAILENTERSHELLDEBUGCLOUD", "PHISHING"] 
inputdata = ["FLASHEMAILLOGINLINUXINBOX", "GRAPHICS"] 
lx = len(inputdata[0])
ly = len(inputdata[1])

ret = []
for x in range(lx):
    row = inputdata[0][x]
    col = inputdata[1][x%ly]
    iz = square[row][col]
    print(f'Trying to fetch cypherletter for ROW: {row} COL: {col}, intermediate result: [{iz}]')
    ret += [iz]

print('---')
fres = ''.join(ret)
print(f'Final result: "{fres}"')