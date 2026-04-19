def decrypt(cipher, key=4):
    rows = len(cipher) // key
    plain_text = [''] * (rows * key)
    char_index = 0
    for col in range(key):
        for row in range(rows):
            plain_text[row * key + col] = cipher[char_index]
            char_index += 1
    return "".join(plain_text).rstrip('X')