class Pion:
    def __init__(self, couleur, y):
        self.couleur = couleur
        self.y = y

    def deplacement_valide(self, x_cible, y_cible, plateau):
        if abs(y_cible - self.y) <= 1:
            return True
        return False

    def deplacer(self, y_cible, plateau):
        if self.deplacement_valide(y_cible, plateau):
            self.y = y_cible
        else:
            print("invalid")