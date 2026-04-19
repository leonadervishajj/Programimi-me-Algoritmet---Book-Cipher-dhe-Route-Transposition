import math

def build_matrix(text, key):
    text = text.replace(" ", "").upper()
    rows = math.ceil(len(text) / key)
    text = text.ljust(rows * key, 'X') # Mbushja me X
    return text, rows
