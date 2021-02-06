from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

# -- Outils pour le scan du répertoire
import glob
import os

listeFichiers = os.scandir("Sources");

nbAvec = 0;
nbSans = 0;
for fichier in listeFichiers :
    print(fichier);
    if fichier.is_file() :
        fp = open('Sources/{0}'.format(fichier.name), 'rb')
        # Create a PDF parser object associated with the file object.
        parser = PDFParser(fp)
        document = PDFDocument(parser)
        
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        
        try :
            outlines = document.get_outlines();
            nbAvec += 1;
            for (level,title,dest,a,se) in outlines:
                print (level, title)
        except PDFNoOutlines :
            nbSans += 1;
            print("Fichier : {0}\n  Table de matières non trouvée".format(fichier));
    
