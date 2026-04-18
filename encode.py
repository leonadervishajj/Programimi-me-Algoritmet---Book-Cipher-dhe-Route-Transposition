import random

def book_cipher_encode(text, book_words):
    result = []
    words = text.lower().split()
    
    for word in words:
        # Gjen të gjitha pozicionet ku ndodhet fjala në "libër"
        indices = [i for i, w in enumerate(book_words) if w.lower() == word]
        
        if indices:
            result.append(str(random.choice(indices)))
        else:
            result.append("?")
            
    return " ".join(result)