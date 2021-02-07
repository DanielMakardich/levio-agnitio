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

import string

from extraireAO.pdfTexte.référentiel import Référentiel


class Document :
    """
        Classe qui encapsule le document PDF lu.  Il offre différents services pour extraire le texte, la table 
        des matières, ainsi que les sections utiles à analyser.  
        
        Le pricipal facteur de performant de cette classe tient au fait que toutes les sections du document n'ont
        pas le même intérêt.  La classe vérifie dans le référentiel quelles sont les notions qui doivent attirer 
        notre attention.
        
        Attributs importants :
        ----------------------
            texte - un tableau ordonné des lignes de textes extraits du fichier pdf.
            table - La table des matières.
            
        Méthodes importantes :
        ----------------------
            hash                - Permet de "passer à la moulinex" une chaîne de caractère de manière 
                                  à la rendre "comparable"
            obtientSection      - Obtenir le texte d'une section en fonction d'une entrée de la table des matières.
            
        D'autres attributs et méthodes sont également disponibles, mais idéalement les considérer privés.
    """
    USAGE = "Table des matières";
    
    def __init__(self, pFichier) :
        # -- Charger le référentiel
        self.référentiel = Référentiel("dictionnaires/référentiel.json");
        
        # -- Procédons à l'extraction du document en mémoire et au traitement de l'information qui nous intéresse.
        fp = open('{0}'.format(pFichier), 'rb')
        parser = PDFParser(fp)
        self.document = PDFDocument(parser)
        if not self.document.is_extractable:
            raise PDFTextExtractionNotAllowed
            
        self.ressources = PDFResourceManager()
        self.hashIndex = list();
        
        # TODO : Extraire le dictionnaire des sections utiles...  Cela pourrait être une solution pour accroître la performance.
        self.texte = self.extraitTexte();
        self.table = self.extraitTableMatières();
    
    def hash(self, pÉtiquette) :
        """
            Retirer les bruits qui empêche de reconnaître les étiquettes entre-elles
        """
        chaîne = "";
        
        chaîneNette = pÉtiquette.strip().upper().replace(" ET ", "").replace("ANNEXE", "");
        for lettre in chaîneNette :
            if lettre in string.ascii_letters :
                chaîne += lettre.upper();
        if chaîne == '' :
            return(chaîneNette.strip().upper());
        return(chaîne);
        
    def étiquetteEntréeTableMatière(self, entréeTableMatières, entréeHashée) :
        """
            Recherche l'étiquette de l'entrée de la table des matières.  Si on la retrouve pas produire une question
            que l'humain devra répondre pour apprendre et procéder, la prochaine fois, automatiquement à l'occurrence.
        """
        étiquette = None;
        
        termes = self.référentiel.retourneTerme(pÉtiquette=entréeHashée, pUsage=Document.USAGE);
        if termes is not None :
            étiquette = termes["Étiquettes"]["Préférée"];
        else :
            # TODO : Énoncer une question pour apprendre et procéder la prochaine fois au traitement automatique de l'entrée.
            self.référentiel.indiquerTermeAClasser(entréeTableMatières, entréeHashée);
            
        return(étiquette);
        
    def devineTablematières(self) :
        """
            À défaut que le fichier PDF n'ait définit formellement une table des matières... on devine quand même.
        """
        entrées = list();
        
        # TODO : Partir du référentiel et rechercher les éléments dans les 
        
        
        return(entrées);
        
    def exploiteTableMatièresFormelle(self) :
        """
            Des fois, les gens génèrent une table des matières formelles lorsqu'ils génère des PDF...
        """
        entrées = list();
        
        try :
            outlines = self.document.get_outlines();
            
            for no, (level,title,dest,a,se) in enumerate(outlines):
                entrée = dict();
                entrée["no"] = no;
                entrée["niveau"] = level;
                entrée["title"] = title;
                entrée["hash"] = self.hash(title);
                
                # --- Obtenons le libellé préféré (ou formellement reconnu) du dictionnaire.
                entrée["étiquette"] = self.étiquetteEntréeTableMatière(entrée["title"], entrée["hash"]);
                
                entrée["dest"] = dest;
                entrée["action"] = a;
                entrée["se"] = se;
                entrée["emplacements"] = list();
                
                for no, paragraphe in enumerate(self.texte) :
                    if entrée["hash"] == self.hash(paragraphe) :
                        entrée["emplacements"].append(no);
                        
                entrées.append(entrée);
        except PDFNoOutlines :
            entrées = None;
            
        return(entrées);
        
    def extraitTableMatières(self) :
        """
            Extrait la table des matières du document lorsque disponible.
        """
        # -- Donnons la chance à ceux qui ont fait une belle table des matières formelle dans leur PDF.
        entrées = self.exploiteTableMatièresFormelle();
        # -- S'ils n'ont pas fait le travail ... alors devinons..
        if entrées is None :
            entrées = devineTablematières();
            
        return(entrées);
            
    def extraitTexte(self) :
        """
            Extrait le texte de tout le document.
        """
        if not self.document.is_extractable:
            raise PDFTextExtractionNotAllowed
            
        texte = list();
        
        laparams = LAParams()
        device = PDFPageAggregator(self.ressources, laparams=laparams)
        interpreter = PDFPageInterpreter(self.ressources, device)
        for i, page in enumerate(PDFPage.create_pages(self.document)) :
            interpreter.process_page(page)
            layout = device.get_result()
            for element in layout:
                if isinstance(element, LTTextBoxHorizontal) :
                    hâchage = self.hash(element.get_text());
                    if len(hâchage) > 0:
                        texte.append(element.get_text().replace("\n", ""))
                        if hâchage not in self.hashIndex :
                            self.hashIndex.append(hâchage);
        return(texte);
        
    def _trouveMaxEmplacement(self, entréeChoisie) :
        """
            Retourne la valeur maximale pour trouver l'emplacement de la section de l'entrée à la table des matières.
        """
        maxEntrée = 0;
        for entrée in entréeChoisie["emplacements"] :
                if maxEntrée < entrée :
                    maxEntrée = entrée
        return(maxEntrée);
        
    def obtientSection(self, entréeTableMatière) :
        """
            Retourne le "texte" de la section indiquée par une entrée de la table des matières
        """
        sectionSuivante = self.table[entréeTableMatière["no"] + 1];
        
        if len(entréeTableMatière["emplacements"]) > 0 and len(sectionSuivante["emplacements"]) > 0 :
            maxEntréeDébut = self._trouveMaxEmplacement(entréeTableMatière);
            maxEntréeFin = self._trouveMaxEmplacement(sectionSuivante);
            texte = "";
            for paragraphe in self.texte[maxEntréeDébut:maxEntréeFin] :
                texte += paragraphe;
            return(texte)
        else :
            return (None);
