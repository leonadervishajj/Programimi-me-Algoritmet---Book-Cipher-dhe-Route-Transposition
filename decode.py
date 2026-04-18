def book_cipher_decode(encoded_text, book_words):
    result = []
    tokens = encoded_text.split() 
    
    for token in tokens:
        if token == "?":
            result.append("?")
        else:
            try:
                index = int(token)
                result.append(book_words[index])
            except (ValueError, IndexError):
                result.append("?")
    
    return " ".join(result)