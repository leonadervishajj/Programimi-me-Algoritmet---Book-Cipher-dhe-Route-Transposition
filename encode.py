def book_cipher_encode(text, book_words):
    result = []
    book_lower = [w.lower() for w in book_words]
    
    words = text.lower().split()

    for word in words:
        if word in book_lower:
         
            pozicioni = book_lower.index(word)
            result.append(str(pozicioni))
        else:
            result.append("?")
            
    return " ".join(result)