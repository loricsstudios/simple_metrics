def check_parity(bits, position):
    count = 0
    for i in range(position, len(bits), position * 2):
        count += sum(int(b) for b in bits[i:i+position])
    return count % 2 == 0

def decode_hamming(encoded):
    # Step 1: Identify parity and data bits
    n = len(encoded)
    
    # Step 2: Check parity and locate error
    error_pos = 0
    for i in range(1, n):
        if i & (i - 1) == 0:  # if i is a power of 2
            if not check_parity(encoded, i):
                error_pos += i
    
    # Check overall parity
    if sum(int(b) for b in encoded) % 2 != 0:
        error_pos += 1
    
    # Step 3: Correct the error
    if error_pos > 0:
        encoded = encoded[:error_pos-1] + str(1 - int(encoded[error_pos-1])) + encoded[error_pos:]
    
    # Step 4: Extract data bits
    data = ''
    for i in range(1, n):
        if i & (i - 1) != 0:  # if i is not a power of 2
            data += encoded[i-1]
    
    # Step 5: Convert to decimal
    return int(data, 2)

# Test with the given encoded string
# encoded = '1010110000101111110101100011100101011111010111010001001111011000'
# encoded = '11110000' #expecting 8
encoded = '1001101010' #expecting 21 (after parity correction)
        #    
result = decode_hamming(encoded)
print(result)