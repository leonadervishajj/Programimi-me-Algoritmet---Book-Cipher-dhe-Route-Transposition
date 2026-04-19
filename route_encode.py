from route_utils import build_matrix

def encrypt(text, key=4):
    key = max(1, int(key))
    
 
    if not text:
        return ""

    text, rows = build_matrix(text, key)
    cipher = ""
    
   
    for col in range(key):
        for row in range(rows):
            index = row * key + col
            if index < len(text):
                cipher += text[index]
            
    return cipher