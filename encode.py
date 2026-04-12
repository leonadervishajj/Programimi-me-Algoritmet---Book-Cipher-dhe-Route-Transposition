
def book_cipher_encode(text, book_words):
    result = []
    words = text.lower().split()

    for word in words:
        try:
            index = book_words.index(word)
            result.append(str(index))
        except ValueError:
            result.append("?")

    return " ".join(result)   # Ky modul implementon funksionin per enkriptimin e mesazheve duke perdorur Book Cipher