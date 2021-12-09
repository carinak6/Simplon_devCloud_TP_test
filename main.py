import modele
import controleur
import vue

# Les acteurs MVC sont globaux dans cet exemple 
var_vue = vue.Vue()
var_controleur = controleur.Controleur()
var_modele = modele.Modele()
# on veut récupérer 2 lignes sur l'entrée standard.
# _ est utilisé pour ignorer l'index: https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc
for _ in range(2):
    var_controleur.stockEntree()
# Puis on sauvegarde dans un fichier
var_controleur.sauvegardeChaines()