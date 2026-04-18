import random
from encode import book_cipher_encode
from decode import book_cipher_decode

BOOK_SOURCE = """
Gjuha shqipe eshte pasuria jone me e madhe. Ne kete projekt 
kemi implementuar algoritmet per sigurimin e komunikimit. 
Python eshte gjuha me e mire per perpunimin e tekstit.
"""

def main():
    print("\n" + "="*40)
    print("      SISTEMI I SIGURISE SE TE DHENAVE")
    print("="*40)
    print("1. Enkripto (Book Cipher)")
    print("2. Dekripto (Book Cipher)")
    print("3. Dil")
    
    while True:
        zgjedhja = input("\nZgjidhni opsionin (1/2/3): ")
        
        if zgjedhja == "1":
            teksti = input("Shkruaj mesazhin: ")
            kodi = book_cipher_encode(teksti, BOOK_SOURCE)
            print(f"\n[SUKSES] Kodi i gjeneruar: \n{kodi}")
            
        elif zgjedhja == "2":
            kodi_hyrje = input("Ngjitni numrat per dekriptim: ")
            mesazhi = book_cipher_decode(kodi_hyrje, BOOK_SOURCE)
            print(f"\n[SUKSES] Mesazhi i zbuluar: \n{mesazhi}")
            
        elif zgjedhja == "3":
            print("Duke u mbyllur...")
            break
        else:
            print("[GABIM] Ju lutem zgjidhni 1, 2 ose 3.")

if __name__ == "__main__":
    main()
    