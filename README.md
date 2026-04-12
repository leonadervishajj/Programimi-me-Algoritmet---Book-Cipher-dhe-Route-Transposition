# Programimi-me-Algoritmet---Book-Cipher-dhe-Route-Transposition

Ky projekt implementon dy metodat klasike të kriptografisë : 
- **Book Cipher** **(Enkriptim me libër)*
- **Route Transposition*** *(Enkriptim me rrugë në grid)***

Qëllimi i projektit është që të tregojë si mund të enkriptohen dhe dekriptohen mesazhet dke përdorur teknikat bazë të zëvendësimit dhe riorganizimit të tekstit.

**Book Cipher** është një metodë klasike e kriptografisë(enkriptimit), ku një tekst i zakonshëm(libër, artikull, paragraf), përdoret si çelës sekret për të fshehur një mesazh. 

Në vend që mesazhi të dërgohet si tekst i lexueshëm, ai shndërrohet në një seri numrash që përfaqësojnë pozicionet e fjalëve në librin e zgjedhur.
  
 
  📌 **PARIMI I FUNKSIONIMIT**

Ideja  është që çdo fjalë në mesazh zëvendësohet me një pozicion(index) nga një tekst referencë, që quhet ***book text***

 -**Ideja kryesore është:**

  Që vetëm personi që ka të njëjtin libër mund të kuptojë mesazhin.


**Si zhvillohet Enkriptimi (Encoding)?**

🔐 Enkodimi te Book Cipher bazohet në këtë koncept: 

- Krijohet një listë fjalësh nga një libër(psh book_words)
- Çdo fjalë në mesazh kërkohet në atë listë
- Në vend të fjalës, ruhet pozita e saj në libër
- Nëse fjala nuk gjendet, mund të përdoret si simbol ***?

*Shembull*: 
 - *Text*** : "I love python"
 - *Book*** : ["I", "love", "python"]
 - *Output*** : **0 , 1 , 2**


 **Si zhvillohet Dekriptimi (Decoding)?**

 🔐 Dekodimi te Book Cipher është procesi i kundërt i enkriptimit.
 -  Në vend që fjalët të kthehen në numra, këtu numrat (indekset) kthehen në fjalë duke përdorur të njëjtën listë referencë (book_words).
 - Fillimisht e merr tekstin e enkriptuar
 - E ndan tekstin në pjesë(tokens) - Teksti ndahet sipas hapësirave
 - E kthen çdo numër në index
 - E merr fjalën nga book_words
 - Dhe mandej ndërtohet mesazhi final