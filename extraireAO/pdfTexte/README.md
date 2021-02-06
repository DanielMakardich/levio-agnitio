Usage du package document.py :

   from extraireAO.pdfTexte.document import Document
   d = Document("Sources/700 001 429 Gestion de projets.pdf")
   texte = d.obtientSection(d.table[1])
   print(texte);
