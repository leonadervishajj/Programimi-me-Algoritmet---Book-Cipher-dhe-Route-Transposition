import random

# LIBRI (Burimi i shkronjave për enkodim)
BOOK_SOURCE = """
Gjuha shqipe është një gjuhë indievropiane që flitet nga më shumë se 7 milionë njerëz.
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
            index = int(part)
            plain_text += book[index]
            
    return plain_text

def main():
    print("\n--- SISTEMI I ENKRIPTIMIT (BOOK CIPHER) ---")
    print("1: Enkripto Mesazhin")
    print("2: Dekripto Kodin")
    
    zgjedhja = input("\nZgjidh opsionin -> ")
    
    if zgjedhja == "1":
        mesazhi = input("Shkruaj tekstin: ")
        kodi = encode_book_cipher(mesazhi, BOOK_SOURCE)
        print(f"\nKodi i gjeneruar:\n{kodi}")
    elif zgjedhja == "2":
        kodi_hyrje = input("Ngjit kodin këtu: ")
        teksti_fituar = decode_book_cipher(kodi_hyrje, BOOK_SOURCE)
        print(f"\nMesazhi i dekriptuar: {teksti_fituar}")
    else:
        print("Gabim! Zgjidh 1 ose 2.")

if __name__ == "__main__":
    main()