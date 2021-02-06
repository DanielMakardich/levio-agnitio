# coding: utf8
#!/usr/bin/python3
#
# 
#   Module permettant de traiter un document en particulier et fournir les textes.
#
#   Auteur :        Fabien Tremblay, 2021
#   Modificateur (s) Date       Sujet de la modification
#   ================ ========== ===============================================
#
#


from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LTRect

class Document :
    
    def __init__(self, pFichier) :
        fp = open('{0}'.format(pFichier), 'rb')
        parser = PDFParser(fp)
        self.document = PDFDocument(parser)
        if not self.document.is_extractable:
            raise PDFTextExtractionNotAllowed
            
        self.ressources = PDFResourceManager()
        
        laparams = LAParams()
        device = PDFPageAggregator(ressources, laparams=laparams)
        interpreter = PDFPageInterpreter(ressources, device)
        
        for i, page in enumerate(PDFPage.create_pages(self.document)) :
            interpreter.process_page(page)
            layout = device.get_result()
            for element in layout:
                print(type(element));
                if isinstance(element, LTTextBoxHorizontal) :
                    print(element.get_text())
