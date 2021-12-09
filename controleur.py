import modele
import vue

# Le controleur fait le lien entre la vue et le modèle en effectuant des traitements sur la donnée
class Controleur:
    # Le controleur demande à la vue de récupérer une chaine de caractères sur l'entrée standard, et ensuite demande au modèle 
    # de le stocker
    def stockEntree(self):
        self.chaine = vue.Vue.entree()
        modele.Modele.ajouter(self.chaine.upper())

    # Le controleur récupère les chaînes du modèle et va écrire dans un fichier
    def sauvegardeChaines(self):
        self.chaines = modele.Modele.recupererChaines()
        with open('test.txt', 'w') as f:
            for chaine in self.chaines:
                f.write(chaine)