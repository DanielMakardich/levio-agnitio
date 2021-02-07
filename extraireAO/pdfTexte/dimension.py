# coding: utf8
#!/usr/bin/python3
#
# 
#   Module permettant de charger le dictionnaire des terminologies utilisées
#
#   Auteur :        Fabien Tremblay, 2021
#   Modificateur (s) Date       Sujet de la modification
#   ================ ========== ===============================================
#
#

import csv
from extraireAO.pdfTexte.référentiel import Référentiel

r = Référentiel("dictionnaires/référentiel.json");

def chargerDictionnaire(pRéférentiel, pUsage, pNomFichier) :
    try :
        ref = pRéférentiel;
        
        # -- Voir si on doit initer le référentiel --
        réserve = ref.retourneTerme(pÉtiquette="Réserve", pUsage=pUsage);
        if réserve is None :
            réserve = ref.ajouteTerme(pCléUnique="Réserve", pUsage=pUsage, pPréféré="Réserve");
            
        # -- Débuter le chargement --
        entête = None;
        
        with open(pNomFichier) as csvFile :
            occurrences = csv.reader(csvFile, delimiter=";", quotechar='"');
            for noLigne, ligne in enumerate(occurrences) :
                tailleLigne = len(ligne);
                
                if noLigne == 0 :
                    entête = ligne;
                elif tailleLigne > 1 :
                    terme = ref.retourneTerme(pÉtiquette=ligne[1], pUsage=pUsage);
                    if terme is None :
                        # -- Il faut voir si on a précisé quelque chose que nous préférons.  Sinon, c'est que c'est sans importance...
                        if tailleLigne > 2 and len(ligne[2]) > 0 :
                            terme = ref.retourneTerme(pÉtiquette=ligne[2], pUsage=pUsage);
                            if terme is None :
                                terme = ref.ajouteTerme(pCléUnique=ligne[2], pUsage=pUsage, pPréféré=ligne[2]);
                            terme["Étiquettes"]["Équivalentes"].append(ligne[1]);
                        else :
                            # -- Mettre le terme dans la "réserve"
                            réserve["Étiquettes"]["Équivalentes"].append(ligne[1]);
                            
    except FileNotFoundError :
        None;
        


