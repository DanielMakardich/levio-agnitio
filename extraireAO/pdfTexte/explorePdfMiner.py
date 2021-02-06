from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

# -- Outils pour le scan du répertoire
import glob
import os

listeFichiers = os.scandir("Sources");

for fichier in listeFichiers :
   print(fichier);

fp = open('Sources/AO_CIUSSS_CEMTL-2020-047-Charge-projets-TI.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
document = PDFDocument(parser)

if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

try :
    outlines = document.get_outlines();
except PDFNoOutlines :
    		

for (level,title,dest,a,se) in outlines:
    print (level, title)
