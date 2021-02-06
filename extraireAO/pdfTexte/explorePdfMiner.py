from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

from extraireAO.pdfTexte.référentiel import Référentiel

# -- Outils pour le scan du répertoire
import glob
import os
import string

import json
import csv

listeFichiers = os.scandir("Sources");


def nettoieÉtiquette(pÉtiquette) :
        """
            Retirer les bruits qui empêche de reconnaître les étiquettes entre-elles
        """
        chaîne = "";
        
        chaîneNette = pÉtiquette.upper().replace(" ET ", "").replace("ANNEXE", "");
        for lettre in chaîneNette :
            if lettre in string.ascii_letters :
                chaîne += lettre.upper();
        if chaîne == '' :
            return(chaîneNette.strip().upper());
        return(chaîne);

nbAvec = 0;
nbSans = 0;
sans = list();
for fichier in listeFichiers :
    print(fichier);
    if fichier.is_file() :
        description = dict();
        sans.append(description);
        description["fichier"] = fichier;
        fp = open('Sources/{0}'.format(fichier.name), 'rb')
        # Create a PDF parser object associated with the file object.
        parser = PDFParser(fp)
        document = PDFDocument(parser)
        
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        
        try :
            outlines = document.get_outlines();
            nbAvec += 1;
            description["TableDesMatières"] = outlines;
            entrées = list();
            
            for no, (level,title,dest,a,se) in enumerate(outlines):
                entrée = dict();
                entrée["niveau"] = level;
                entrée["title"] = title;
                entrée["hash"] = nettoieÉtiquette(title);
                entrée["dest"] = dest;
                entrée["action"] = a;
                entrée["se"] = se;
                
                entrées.append(entrée);
            description["Entrées"] = entrées;
        except PDFNoOutlines :
            nbSans += 1;
            description = dict();
            
            print("Fichier : {0}\n  Table de matières non trouvée".format(fichier));
        
r = Référentiel();
usage = "SectionAO";
index = list(); # Liste des hash keys
sections = list( ); # liste de dictionnaires
sections.append(['Titre', 'hash', 'Référence']);

print("Résultat sur le contenu des tables des matières : {0} avec {1} sans".format(nbAvec, nbSans));
for no, élément in enumerate(sans) :
    try :
        print(no);
        tableMatières = élément["TableDesMatières"];
        entrées = élément["Entrées"];
        for entrée in entrées :
            if entrée["hash"] not in index :
                sections.append( [ entrée["title"], entrée["hash"], None ] );
                index.append(entrée["hash"]);
            #terme = r.retourneTerme(usage, entrée["hash"]);
            #if terme is None :
            #    r.ajouteTerme(entrée["hash"], usage, entrée["hash"]);
            
    except KeyError :
        print("Sans tables : {0}".format(élément["fichier"]));

with open('Transforme.csv', 'w') as csvfile :
    writer = csv.writer(csvfile, delimiter=";", quotechar = "\"");
    for ligne in sections :
        writer.writerow(ligne);
        
        
from extraireAO.pdfTexte.document import *
d = Document("Sources/700 001 429 Gestion de projets.pdf")
TM = d.table

for entrée in TM :
    nbTrouvé = 0;
    
    for no, paragraphe in enumerate(d.texte) :
      if entrée["hash"] == d.hash(paragraphe) :
         print(paragraphe);
         nbTrouvé += 1;
         if nbTrouvé 

