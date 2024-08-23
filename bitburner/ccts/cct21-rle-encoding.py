def rle_compress(input_str):
    if not input_str:
        return ""

    result = []
    current_char = input_str[0]
    current_length = 1

    for char in input_str[1:]:
        if char == current_char and current_length < 9:
            current_length += 1
        else:
            result.append(f"{current_length}{current_char}")
            current_char = char
            current_length = 1

    result.append(f"{current_length}{current_char}")

    return "".join(result)

# input_str = "Q5HHH1LLTTTTTTTTTTTThhPCCOO1111111UUUUUUUHxlvvvvYyyyyy55555555555JJYFFFFFFFFFFJJddddddd"
input_str = "Gaaaaaaa66666J66f3OOOOOOOOOO2222222222222bb66KKSSOOPPrrrrrr0ddzIIIIIIIIIIIz"
print(rle_compress(input_str))
