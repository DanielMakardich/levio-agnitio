# coding: utf8
#!/usr/bin/python3
#
# 
#   Module permettant de traiter le dictionnaire des terminologies utilisées
#
#   Auteur :        Fabien Tremblay, 2021
#   Modificateur (s) Date       Sujet de la modification
#   ================ ========== ===============================================
#
#

import json

class Référentiel :
    """
        Le référentiel décrit les notions et les associe à l'usage.
            Code : Code attribué à la notion
            Étiquette : Liste divisée entre "préférée" ou "équivalente"
            Usage : Usage où est utilisé cette notion.
        
        Le fichier est toujours créer à partir de la racine d'exécution courante dans le sous-répertoire ETL
    """
    référentiel = list();
    _codeRéférentiel = 0;
    _nomFichier = "référentiel.json"
    
    def __init__(self, pNomFichier = "référentiel.json") :
        """
            Charge les fichiers de références
        """
        self._nomFichier = pNomFichier;
        
        try :
            with open(self._nomFichier) as data_file:
                self.référentiel = json.load(data_file)
        except FileNotFoundError :
            self.référentiel = list();
            
        self.trouveDernierCode();
    
    def triUsage(self, e) :
        """
            Définit le tri pour l'environnement technologique
        """
        return e[e["CléUnique"]]
        
    def consolideTermes(self, pUsage) :
        liste = list();
        for élément in self.référentiel :
            if élément["Usage"] == pUsage :
                liste.append(élément);
        liste.sort(key = self.triUsage);
        
        return(liste);
    
    def trouveDernierCode(self) :
        """
            Détermine le dernier code de référentiel
        """
        for item in self.référentiel :
            if item["Code"] > self._codeRéférentiel :
                self._codeRéférentiel = item["Code"];
           
    def retourneTerme(self, pUsage, pÉtiquette) :
        """
            Retrouve le terme s'il est déjà défini.
        """
        termes = self.référentiel;
        for terme in termes :
            if terme["Usage"] == pUsage and pÉtiquette in terme["Étiquettes"]["Équivalentes"] :
                return(terme);
        return(None);
        
    def ajouteTerme(self, pCléUnique, pUsage, pPréféré) :
        """
            Ajouter un terme à l'index et au référentiel
            
            Retourne :
                L'entrée du référentiel.
        """
        # -- Initier un nouvel élément au référentiel
        self._codeRéférentiel = self._codeRéférentiel + 1;
        entrée = dict();
        entrée["Code"] = self._codeRéférentiel;
        entrée["Étiquettes"] = dict();
        entrée["Étiquettes"]["Préférée"] = pPréféré;
        entrée["Étiquettes"]["Équivalentes"] = list();
        entrée["Étiquettes"]["Équivalentes"].append(pPréféré);
        entrée["Usage"] = pUsage;
        entrée["CléUnique"] = pCléUnique;
        self.référentiel.append(entrée);
        return(entrée);
        
    def enregistreJson(self) :
        with open(self._nomFichier, 'w', encoding='utf-8') as f:
            json.dump(self.référentiel, f, ensure_ascii=False, indent=4);

