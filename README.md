Agnitio
=======

Consiste à exploiter les appels d'offres publiées par le gouvernement du Québec 
pour ressortir les informations nécessaires 
à la décision d'aller de l'avant avec une proposition ou passer.

Pile logicielle
===============
   1. Python
   2.   - pdfminer ?
   3.   - ...
   

Instructions d'installation :
=============================
1. Créer un répertoire sur votre ordinateur
2. Installer github
3. Dans le répertoire créer, lancer la commande
      git clone https://github.com/DanielMakardich/levio-agnitio.git
      ... (demander de l'aide)
      
3. python3 -m pip install --upgrade pip
4. python3 -m pip install pdfminer

5. Installer ghostscript:
   1. Pour Windows utiliser le lien suivant et choisir la version _Ghostscript AGPL Release_ qui convient pour votre OS:
      * [ghostscript installer](https://www.ghostscript.com/download/gsdnld.html)
   2. Pour Linux (Ubuntu) roulez la commande:
      * _apt install ghostscript python3-tk_
   3. Pour Mac roulez la commande:
      * _brew install ghostscript tcl-tk_

6. Installer ActivePython 3.8: 
   * [ActivePython 3.8 installer](https://www.activestate.com/products/python/downloads/)
7. Exécuter la commande: `excalibur initdb`
8. Exécuter la commande: `excalibur webserver`
9. Ouvrir l'application sur le web sur _http://localhost:5000_