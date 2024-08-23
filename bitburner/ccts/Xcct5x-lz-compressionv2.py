def find_best_reference(data, pos):
    """ Find the best reference for the current position """
    max_length = 0
    best_distance = 0
    n = len(data)
    
    for distance in range(1, 10):
        if pos - distance < 0:
            break
        length = 0
        while length < 9 and pos + length < n and data[pos + length] == data[pos + length - distance]:
            length += 1
        if length > max_length:
            max_length = length
            best_distance = distance
    return max_length, best_distance

def lz_compress(data):
    n = len(data)
    pos = 0
    compressed = []
    use_type1 = True
    
    while pos < n:
        if use_type1:
            # Type 1 chunk: Direct copy
            length = min(9, n - pos)
            compressed.append(str(length) + data[pos:pos + length])
            pos += length
        else:
            # Type 2 chunk: Reference to earlier data
            max_length, best_distance = find_best_reference(data, pos)
            if max_length == 0:
                # If no reference found, just skip and switch back to Type 1
                compressed.append("0")
                use_type1 = not use_type1
                continue
            compressed.append(str(max_length) + str(best_distance))
            pos += max_length
        
        # Alternate chunk type
        use_type1 = not use_type1
    
    return "".join(compressed)

# Given input string
input_data = "Qo4hInPWnYe6zg2RcccccCtay6666p666p666pp666pp6pRbuc6SN2iBwDcQ"
output = lz_compress(input_data)
print(output)
