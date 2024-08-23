 
inp = "5aaabb450723abb"
expected = "aaabbaaababababaabb"
inp2 = "306D81149866vQ8el6624A762AQ469QjnuSUQ1D160921h69"


tmpo = ""
ofs=0
count = 0
cycle = 0

while len(inp)>0:
    cycle +=1
    count=int(inp[0])

    if count== 0:
        print('ending chunk')
        inp = inp[1:]
        continue
    elif ord(inp[1]) in range(ord('1'),ord('9')):
        print('repeating ..')
        ofs=len(tmpo)-1
        for x in range(count):
            tmpo+=tmpo[ofs-count:ofs-count+1]
            ofs +=1
        inp = inp[2:]
    else:
        print('adding raw')
        tmpo+=inp[1:ofs+count+1]
        inp = inp[len(tmpo)+1:]
    # ofs=len(tmpo)    
    
    print(f'CYcle: {cycle} tmpo: {tmpo}')    

print(f"Expected : {expected}")
print(f"Extracted: {tmpo}")


def lz_decompress(compressed):
    decompressed = ""
    i = 0
    copy_mode = True

    while i < len(compressed):
        length = int(compressed[i])
        i += 1

        if length == 0:
            copy_mode = not copy_mode
            continue

        if copy_mode:
            decompressed += compressed[i:i+length]
            i += length
        else:
            offset = int(compressed[i])
            i += 1
            for _ in range(length):
                decompressed += decompressed[-offset]

        copy_mode = not copy_mode

    return decompressed

print(lz_decompress(inp2))