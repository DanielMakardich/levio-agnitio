Agnitio
=======

Consiste à exploiter les appels d'offres publiées par le gouvernement du Québec 
pour ressortir les informations nécessaires 
à la décision d'aller de l'avant avec une proposition ou passer.

Pile logicielle
===============
   1. Python 
   2. Librairies python
      - pdfminer
      - ghostscript
      - activePython
      - spaCy
      - Excalibur
   

Instructions d'installation :
=============================

## Cloner le code

1. Créer un répertoire sur votre ordinateur
2. Installer github
3. Dans le répertoire créer, lancer la commande
      git clone https://github.com/DanielMakardich/levio-agnitio.git
      ... (demander de l'aide)

## Installation des dépendances:

* ### PDFMiner - _outil d'extraction PDF_

  1. python3 -m pip install --upgrade pip
  2. python3 -m pip install pdfminer

* ### spaCy - _librairie NLP_

* ### Excalibur - _interface web avec extraction_ 

  1. Installer ghostscript:
     * Pour Windows utiliser le lien suivant et choisir la version _Ghostscript AGPL Release_ qui convient pour votre OS:
        * [ghostscript installer](https://www.ghostscript.com/download/gsdnld.html)
     * Pour Linux (Ubuntu) roulez la commande:
        * _apt install ghostscript python3-tk_
     * Pour Mac roulez la commande:
        * _brew install ghostscript tcl-tk_

  2. Installer ActivePython 3.8: 
     * [ActivePython 3.8 installer](https://www.activestate.com/products/python/downloads/)
  3. Exécuter la commande: `excalibur initdb`
  4. Exécuter la commande: `excalibur webserver`
  5. Ouvrir l'application sur le web sur `http://localhost:5000`
