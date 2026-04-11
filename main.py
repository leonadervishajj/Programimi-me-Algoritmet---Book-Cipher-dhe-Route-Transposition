from encode import book_cipher_encode

# Ketu e kam marr nje tekst real - paragraf me 3 rreshta

book = """In the quiet village by the river, people lived simple lives and shared their strories every evening. The sun set slowly behind the hills, painting the sky in warm colors. Children played in the fields while elders spoke about the past and the lessons they had learned.   """

book_words = book.lower().split()    #libri kthehet ne nje liste te fjaleve 
text = input("Shkruaj tekstin per encode: ")    #ketu behet input nga useri

result = book_cipher_encode(text, book_words)