def book_cipher_decode(encoded_text, book_words):
    result = []
    tokens = encoded_text.split()

    for token in tokens:
        if token == "?":
            result.append("?")
        else:
            try:
                index = int(token)
                if 0 <= index < len(book_words):
                    result.append(book_words[index])
                else:
                    result.append("?")
            except (ValueError, IndexError):
                result.append("?")

    return " ".join(result)