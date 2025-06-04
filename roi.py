class Roi:
    def __init__(self, couleur, x, y):
        self.couleur = couleur
        self.x = x
        self.y = y

    def deplacement_valide(self, x_cible, y_cible, plateau):
        if abs(x_cible - self.x) <= 1 and abs(y_cible - self.y) <= 1:
            return True
        return False

    def deplacer(self, x_cible, y_cible, plateau):
        if self.deplacement_valide(x_cible, y_cible, plateau):
            self.x = x_cible
            self.y = y_cible
        else:
            print("invalid")