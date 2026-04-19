from route_utils import build_matrix
def encrypt(text, key=4):
    text, rows = build_matrix(text, key)
    cipher = ""
    for col in range(key):
        for row in range(rows):
            cipher += text[row * key + col]
    return cipher