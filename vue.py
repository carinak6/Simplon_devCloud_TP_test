import sys
#import time

# La vue se charge de récupérer l'action utilisateur qui est de taper une ligne de texte sur l'entrée standard
class Vue:
    def entree(self):
        #time.sleep(4)
        return sys.stdin.readline()