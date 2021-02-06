import spacy

from spacy import displacy
from terminaltables import AsciiTable
from extraireAO.pdfTexte.document import Document

nlp = spacy.load("fr_core_news_sm")
d = Document("Sources/700 001 429 Gestion de projets.pdf")

texte = d.obtientSection(d.table[10])
print(texte)

# Dictionnaire utilisé pour définir 
texte = nlp(texte)


table_data = [
    ['Mot', 'lemma', 'pos', 'dep', 'isStop']
]

# Récupérer le mot, lemma, pos du mot et si le mot est un stop word
for phrase in texte.sents:
    for mot in phrase:
        table_data.append([mot, mot.lemma_, mot.pos_, mot.dep_, mot.is_stop])
        if (mot.lemma_.upper == "heure"):
            print (phrase)


# index=0
# chunk = ""
# previousChunk = " "

# for chunk in texte_durée.noun_chunks:
#     index += 1
#     print(chunk.text)
#     if(table_data[index][4] == "False" and chunk != previousChunk):
#         table_data[index].append(chunk.text)
#         print("CURR CHUNK: " + chunk.text)
#         print("PREV CHUNK: " + previousChunk.text)

#     previousChunk = chunk
    

    
table = AsciiTable(table_data)

print(table.table)

displacy.serve(texte, style="dep")