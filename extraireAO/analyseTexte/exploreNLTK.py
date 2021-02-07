from _typeshed import NoneType
import spacy

from spacy import displacy
from terminaltables import AsciiTable
from extraireAO.pdfTexte.document import Document

nlp = spacy.load("fr_core_news_sm")

# Dictionnaire utilisé pour élargir la définition du mot-clé

motCle = {'client': ['client, publié par, ministère, Revenu Québec'], 'contrat': [
    'appel d\'offre, offre, soumission']}

# EXTRAIRE LE TEXTE À ÉVALUER

def obtenirTexte(path, num_section):
    doc = Document(path)    
    if doc.table is not None:
        texte = doc.obtientSection(doc.table[num_section])    
        print(texte)
        return texte
    return None

# UTILITÉS

def chercheDict(dictionaire, valeur):
    for k in dictionaire:
        for v in dictionaire[k].upper():
            if valeur.upper() in v:
                return k
    return None

# OBTENIR LES CLIENTS

def obtenirClient(texte, num_section):
    # Initialiser une table pour la sortie et le récupérer le texte
    table_client = [ ['Nom Client', 'Lab)el', 'Phrase', 'Index phrase', 'Index section'] ]
   
    # Tokeniser le texte
    texte = nlp(texte)
  
    # Loop sur phrase et par mot pour retourner les entités détectés
    num_phrase = 0
    for phrase in texte.sents:
        num_phrase = + 1
        for mot in phrase.ents:
            if (mot.label_ == "" or chercheDict(motCle, mot) != None):
                table_client.append([mot, phrase.text, mot.label_, num_phrase, num_section])
    table = AsciiTable(table_client)
    print(table.table)

# OBTENIR LES OBJECTIFS/BUTS


# OBTENIR LES DATES IMPORTANTES
for phrase in texte.sents:
    for mot in phrase:
        if (mot.lemma_ == "heure"):
            print(phrase)


displacy.serve(texte, style="dep", page="true")
