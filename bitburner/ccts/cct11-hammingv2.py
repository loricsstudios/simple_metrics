def int_to_hamming_code(n):
    # Convert the integer to binary without leading zeros
    binary = bin(n)[2:]

    # Determine the number of parity bits needed
    m = len(binary)  # Number of data bits
    r = 0  # Number of parity bits
    while (2 ** r) < (m + r + 1):
        r += 1

    # Total length of the Hamming code (data bits + parity bits)
    total_length = m + r

    # Create an array to store the hamming code with '-' as placeholders for parity bits
    hamming_code = ['-'] * total_length

    # Fill the hamming code with data bits
    j = 0  # Index for data bits
    for i in range(total_length):
        if (i + 1) & i == 0:  # If the position is a power of two (parity bit positions)
            hamming_code[i] = 'P'
        else:
            hamming_code[i] = binary[j]
            j += 1

    # Function to calculate the parity for a given position
    def calculate_parity(position):
        parity = 0
        i = position
        while i < total_length:
            # Consider bits in blocks of (position + 1)
            block_size = position + 1
            block = hamming_code[i:i + block_size]
            for bit in block:
                if bit == '1':
                    parity ^= 1
            i += 2 * block_size
        return parity

    # Insert the parity bits into their positions
    for i in range(r):
        parity_pos = 2 ** i - 1
        parity = calculate_parity(parity_pos)
        hamming_code[parity_pos] = str(parity)

    # Calculate and set the overall parity bit at position 0
    overall_parity = 0
    for bit in hamming_code:
        if bit == '1':
            overall_parity ^= 1
    hamming_code[0] = str(overall_parity)

    return ''.join(hamming_code)

# Given integer
n = 40931232545266

# Get the Hamming code
encoded_hamming_code = int_to_hamming_code(n)
print(encoded_hamming_code)
