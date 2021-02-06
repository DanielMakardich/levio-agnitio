# coding: utf8
#!/usr/bin/python3
#
# 
#   Module permettant de traiter un sujet en particulier à partir des textes susceptibles de révéler l'information.
#
#   Auteur :        Fabien Tremblay, 2021
#   Modificateur (s) Date       Sujet de la modification
#   ================ ========== ===============================================
#
#


class sujet :
    """
        Le sujet désigne le thème qui est visé.  Le thème visé est représenté par un attribut que le système
        doit repérer.  
        
        La classe regroupe :
            - les textes d'intérêts et détermine la meilleure heuristique pour trouver.
    """
    
    def __init__(self, pAttribut, pSections) :
        self.attribut = pAttribut
        self.sections = pSections
        

