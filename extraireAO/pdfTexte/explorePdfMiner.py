from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

# -- Outils pour le scan du répertoire
import glob
import os
import string

listeFichiers = os.scandir("Sources");


def nettoieÉtiquette(pÉtiquette) :
        """
            Retirer les bruits qui empêche de reconnaître les étiquettes entre-elles
        """
        chaîne = "";
        
        pÉtiquette.replace(" et ", "");
        for lettre in pÉtiquette :
            if lettre in string.ascii_letters :
                chaîne += lettre.upper();
        if chaîne == '' :
            return(pÉtiquette.strip().upper());
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
                entrée["dest"] = dest;
                entrée["action"] = a;
                entrée["se"] = se;
                
                entrées.append(entrée);
            description["Entrées"] = entrées;
        except PDFNoOutlines :
            nbSans += 1;
            description = dict();
            
            print("Fichier : {0}\n  Table de matières non trouvée".format(fichier));
        
sections = list();

print("Résultat sur le contenu des tables des matières : {0} avec {1} sans".format(nbAvec, nbSans));
for no, élément in enumerate(sans) :
    try :
        print(no);
        tableMatières = élément["TableDesMatières"];
        titre = dict();
        sections.append(titre);
        for (level,title,dest,a,se) in tableMatières:
            print("Avec tables : {0} : {1}".format(élément["fichier"], title));
            titre["hash"] = nettoieÉtiquette(title);
            titre["titre"] = title;
        élément["Titres"] = titre;
            
    except KeyError :
        print("Sans tables : {0}".format(élément["fichier"]));
