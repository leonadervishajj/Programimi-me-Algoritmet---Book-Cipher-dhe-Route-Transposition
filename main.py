from encode import book_cipher_encode

# Ketu e kam marr nje tekst real - paragraf me 3 rreshta

book = """In the quiet village by the river, people lived simple lives and shared their stories every evening. The sun set slowly behind the hills, painting the sky in warm colors. Children played in the fields while elders spoke about the past and the lessons they had learned.  """

book_words = book.lower().split()    #libri kthehet ne nje liste te fjaleve 
text = input("Shkruaj tekstin per encode: ")    #ketu behet input nga useri

result = book_cipher_encode(text, book_words)


import random

BOOK_SOURCE = """
Gjuha shqipe është një gjuhë indoevropiane që flitet nga më shumë se 7 milionë njerëz.
Ajo është gjuha zyrtare e Shqipërisë dhe e Kosovës.
Sistemet e enkriptimit si ky i librit janë përdorur historikisht për siguri të lartë.
"""

def encode_book_cipher(message, book):
    message = message.lower()
    book = book.lower()
    cipher_text = []
    
    for char in message:
        if char == " ":
            cipher_text.append("SPACE")
            continue
            
        indices = [i for i, letter in enumerate(book) if letter == char]
        
        if indices:
            cipher_text.append(str(random.choice(indices)))
        else:
            cipher_text.append(f"NOT_FOUND({char})")
            
    return "-".join(cipher_text)

def decode_book_cipher(cipher_text, book):
    book = book.lower()
    parts = cipher_text.split("-")
    plain_text = ""
    
    for part in parts:
        if part == "SPACE":
            plain_text += " "
        elif "NOT_FOUND" in part:
            plain_text += "?"
        else:
            plain_text += book[int(part)]
            
    return plain_text

def main():
    option = input("1: Enkodim, 2: Dekodim -> ")

    if option == "1":
        msg = input("Mesazhi: ")
        print(encode_book_cipher(msg, BOOK_SOURCE))
    elif option == "2":
        code = input("Kodi: ")
        print(decode_book_cipher(code, BOOK_SOURCE))

if __name__ == "__main__":
    main()