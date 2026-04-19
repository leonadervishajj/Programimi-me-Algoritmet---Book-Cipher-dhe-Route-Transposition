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



 **🔄 2. Route Transposition Cipher**

 Route Transposition Cipher është një metodë ku teksti nuk ndryshohet, por rradhitja e shkronjave ndryshohet duke përdorur një grid (tabelë) dhe një rrugë të caktuar leximi.

** Çka është “Route” në Route Transposition Cipher?**

“Route” (rruga) është mënyra e paracaktuar se si lexohet ose shkruhet teksti në një grid (tabelë) gjatë enkriptimit dhe dekodimit.

Në vend që teksti të lexohet normalisht (rresht për rresht), ai lexohet sipas një rruge specifike të zgjedhur më herët, e cila e ndryshon renditjen e shkronjave dhe e bën mesazhin të paqartë pa çelësin.

Route Transposition Cipher është një metodë ku teksti nuk ndryshohet, por rradhitja e shkronjave ndryshohet duke përdorur një grid (tabelë) dhe një rrugë të caktuar leximi.

Route Transposition Cipher është një metodë ku teksti nuk ndryshohet, por rradhitja e shkronjave ndryshohet duke përdorur një grid (tabelë) dhe një rrugë të caktuar leximi.

Kemi lloje të ndryshme të route-s: 
- Kolonë për kolonë (Column-wise route)
- Rresht për rresht (Row-wise route)
- Zig-Zag route
- Spiral route

**Si zhvillohet Enkriptimi(Encoding) ?**

Hapat:
- Fillimisht teksti vendoset në një grid (rreshta × kolona) dhe nëse mungojnë karaktere, përdoret padding (X)
- Pastaj teksti lexohet sipas një route (p.sh. kolonë për kolonë, spiral, zig-zag)

Si për shembull: 
Text: HELLOWORLD

***Grid:***
H E L L
O W O R
L D X X

**Output (kolonë për kolonë):*
HOL EWD LOX LRX

***🔓 Si zhvillohet Dekodimi ?**

Dekodimi te Route Transposition Cipher është procesi i rikthimit të mesazhit origjinal nga një tekst i enkriptuar ku shkronjat janë riorganizuar sipas një rruge (route) në një grid (tabelë).
Qëllimi është të rindërtohet saktë tabela origjinale dhe pastaj të lexohet mesazhi në rend normal.

Hapat për zhvillimin e enkriptimit janë: 
- Së pari e merr ciphertext-in dhe i largon hapësirat duke e pastruar tekstin

HOL EWD LOX LRX largon hapësirat HOLEWDLOXLRX

- Pastaj e përcakton madhësinë e grid-it dhe dikur e krijon një grid fare bosh
Dmth duhet të dihet numri i rreshtave dhe kolonave dhe krijohet një tabelë bosh me të njëjtat dimensione
- E mbush grid-in sipas route të enkriptimit

Nëse enkriptimi ka lexuar kolonë për kolonë, atëherë gjatë dekodimit:
- e mbushim kolonë për kolonë
- nga lart poshtë

Përshembull:
CipherText :  HOLEWDLOXLRX

Kolona 1 → H O L
Kolona 2 → E W D
Kolona 3 → L O X
Kolona 4 → L R X

Dhe në fund grid del kështu:
H E L L
O W O R
L D X X

- Dhe në fund e lexon grid-i në rend normal

Pasi grid-i është i plotë, lexojmë:

- rresht për rresht
- nga e majta në të djathtë dhe në fund: 

***HELLOWORLDXX**

⚠️ Raste të rëndësishme
 Padding (X ose karaktere shtesë)
Përdoren për të mbushur grid-in dhe gjatë dekodimit zakonisht hiqen në fund
