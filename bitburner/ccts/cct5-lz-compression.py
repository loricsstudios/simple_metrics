def lz_compress(s):
    result = []
    i = 0
    is_type1 = True

    while i < len(s):
        if is_type1:
            # Type 1 chunk (direct copy)
            length = min(9, len(s) - i)
            result.append(str(length) + s[i:i+length])
            i += length
        else:
            # Type 2 chunk (reference)
            best_length = 0
            best_offset = 0
            for offset in range(1, i + 1):
                for length in range(1, min(10, len(s) - i + 1)):
                    if s[i:i+length] == s[i-offset:i-offset+length]:
                        if length > best_length:
                            best_length = length
                            best_offset = offset
                    else:
                        break
            if best_length > 0:
                result.append(str(best_length) + str(best_offset))
                i += best_length
            else:
                result.append('0')

        is_type1 = not is_type1

    # Handle trailing '0' if present
    if result[-1] == '0':
        result.pop()
        if len(result[-1]) == 2:  # If last chunk is type 2
            result[-1] = str(int(result[-1][0]) + 1) + result[-1][1]
        else:  # If last chunk is type 1
            result.append('1' + s[-1])

    return ''.join(result)

# The input string
# input_string = "c35BCla66xZm6xZm6xZm6fHWghrK2ZprICY5sppppppppp0LSvmE4DI7XV0dUNza0dUNzaaaaaaaX8iva"
input_string= "c35BCla66xZm6xZm6xZm6fHWghrK2ZprICY5sppppppppp0LSvmE4DI7XV0dUNza0dUNzaaaaaaaX8iva"
input_pairs = [
    ["abracadabra","7abracad47"],["mississippi","4miss433ppi"],["aAAaAAaAaAA","3aAA53035"],["2718281828","627182844"],["abcdefghijk","9abcdefghi02jk"],["aaaaaaaaaaaa","3aaa91"],["aaaaaaaaaaaaa","1a91031"],["aaaaaaaaaaaaaa","1a91041"],
]

# Compress the input
for pair in input_pairs:
    compressed = lz_compress(pair[0])
    if (compressed == pair[1]):
        print('matches\n')
    else:
        print('does not match!\n')

# print(f"Input: {input_string}")
# print(f"Compressed: {compressed}")
# print(f"Compressed length: {len(compressed)}")