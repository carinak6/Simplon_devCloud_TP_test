class Modele: 
    def __init__(self):
        self.chaines = []

    # Ajoute une chaine dans la liste
    def ajouter(self, chaine):
        self.chaines.append(chaine)

    # Retourne le liste de chaînes.
    def recupererChaines(self):
        return self.chaines