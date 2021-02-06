from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

fp = open('mypdf.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
document = PDFDocument(parser)

if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
    
outlines = document.get_outlines()
for (level,title,dest,a,se) in outlines:
    print (level, title)
