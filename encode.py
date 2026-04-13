
def book_cipher_encode(text, book_words):
    result = []
    words = text.lower().split()

    for word in words:
        if word in book_words:
            result.append(str(book_words.index(word)))
        else:
            result.append("?")

    return " ".join(result)    # Ky modul implementon funksionin per enkriptimin e mesazheve duke perdorur Book Cipher