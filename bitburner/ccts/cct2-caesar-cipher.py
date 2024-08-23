# inp = ["FLASH CLOUD LOGIN TRASH LINUX", -12]
# inp = ["MEDIA MACRO CLOUD TRASH LOGIC", -7]
# inp = ["CLOUD FLASH SHELL QUEUE LOGIN", -17] #17
# inp = ["VIRUS ARRAY LINUX TABLE SHELL", -20]
# inp = ["QUEUE ARRAY PASTE DEBUG CACHE", -8]
inp =  ["ARRAY MOUSE PRINT MACRO SHELL", -8]

alphabet = list(map(lambda x: chr(x), range(ord('A'), ord('Z') + 1)))

la = len(alphabet)
modd = inp[1] % la
if modd<0:
    modd += la
outp = ''
for i in range(0,len(inp[0])):
    if (inp[0][i] == ' '):
        new = ord(' ')
    else:
        new = ord(inp[0][i])+modd
        if new>ord('Z'):
            new -= la
        if new<ord('A'):
            new += la
    outp += chr(new)
print(outp)
    

