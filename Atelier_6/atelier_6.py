from maya import cmds

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QSpinBox,
    QDoubleSpinBox,
    QLabel
)

class generateur_cloture(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generateur de cloture")
        self.build_ui()

    #fonction pour créer les spinbox
    def make_spinbox(self, minimum, maximum):
        champ = QDoubleSpinBox()
        champ.setRange(minimum, maximum)
        return champ


    def build_ui(self):

        #création de la grille et ajout au layout
        grille = QGridLayout()
        layout = QVBoxLayout(self)
        layout.addLayout(grille)

        #création spinbox
        self.longueur = self.make_spinbox(1, 1000)
        self.hauteur = self.make_spinbox(0.5, 100)

        #création d'un spinbox simple vus que le nombre de barreaux est un nombre entier
        self.nombre_barreaux = QSpinBox()
        self.nombre_barreaux.setRange(1, 10)

        self.nombre_poteaux = QSpinBox()
        self.nombre_poteaux.setRange(2, 100)
        

        #setup la grille
        grille.addWidget(QLabel("Longueur"), 0, 0)
        grille.addWidget(self.longueur, 0, 1)
        grille.addWidget(QLabel("Nombre de poteaux"), 1, 0)
        grille.addWidget(self.nombre_poteaux, 1, 1)
        grille.addWidget(QLabel("Hauteur"), 2, 0)
        grille.addWidget(self.hauteur, 2, 1)
        grille.addWidget(QLabel("Nombre de barreaux"), 3, 0)
        grille.addWidget(self.nombre_barreaux, 3, 1)

        #crée le bouton
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.cree_cloture)
        layout.addWidget(self.create_button)

    def cree_cloture(self):
        #stock les valeurs spinbox dans des variables
        longueur = self.longueur.value()
        hauteur = self.hauteur.value()
        nombre_barreaux = self.nombre_barreaux.value()
        nombre_poteaux = self.nombre_poteaux.value()

        #espacement entre les poteaux
        espacement = longueur / (nombre_poteaux - 1)

        

        #poteaux
        for i in range(nombre_poteaux):
            #crée le poteau
            poteau = cmds.polyCube(width=0.3, height=hauteur, depth=0.3)
            #place le poteau au bonne endroit
            cmds.move(i * espacement, hauteur / 2, 0, poteau)
            

        #barreaux
        for i in range(nombre_barreaux):
            #crée le barreaux
            barreau = cmds.polyCube(width=longueur, height=0.15, depth=0.15)
            #définie l'espace entre chaque barreau
            taille_espace = hauteur / (nombre_barreaux + 1)
            #définie la hauteur du barreau en fonction de quelle barreau c'est (si c'est le premier, le deuxieme, le troisieme, etc)
            hauteur_barreau = (i + 1) * taille_espace 
            #mets le barreau au bonne endroit
            cmds.move(longueur / 2, hauteur_barreau, 0, barreau)

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = generateur_cloture()
    tool_window.show()

main()

