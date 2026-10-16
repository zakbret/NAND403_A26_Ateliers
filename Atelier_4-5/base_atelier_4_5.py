import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QSpinBox,
    QSpinBox,
    QLabel
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()

     #fonction pour créer les spin box parce qu'aussi non c'était vraiment trop long les faire a la main
    def make_spinbox(self, minimum, maximum):
        spin = QSpinBox()
        spin.setRange(minimum, maximum)
        spin.setValue(0)
        return spin
            
        
    
    def build_ui(self):

        #crée la grille et l'ajoute au layout
        grille = QGridLayout()
        layout = QVBoxLayout(self)
        layout.addLayout(grille)

        #crée les spinbox pour entrer les valeurs
        self.number_objects = self.make_spinbox(0, 1000)
        self.position_x_min = self.make_spinbox(-1000, 1000)
        self.position_x_max = self.make_spinbox(-1000, 1000)
        self.position_y_min = self.make_spinbox(-1000, 1000)
        self.position_y_max = self.make_spinbox(-1000, 1000)
        self.position_z_min = self.make_spinbox(-1000, 1000)
        self.position_z_max = self.make_spinbox(-1000, 1000)
        self.scale_min = self.make_spinbox(0, 1000)
        self.scale_max = self.make_spinbox(0, 1000)

        #place la grille
        grille.addWidget(QLabel("Numbers of objects"), 0, 1)
        grille.addWidget(self.number_objects, 0 ,2)
        grille.addWidget(QLabel("Min"), 1, 2)
        grille.addWidget(QLabel("Max"), 1, 3)
        grille.addWidget(QLabel("Position en X"), 2, 1)
        grille.addWidget(self.position_x_min, 2, 2)
        grille.addWidget(self.position_x_max, 2, 3)
        grille.addWidget(QLabel("Position en Y"), 3, 1)
        grille.addWidget(self.position_y_min, 3, 2)
        grille.addWidget(self.position_y_max, 3, 3)
        grille.addWidget(QLabel("Position en Z"), 4, 1)
        grille.addWidget(self.position_z_min, 4, 2)
        grille.addWidget(self.position_z_max, 4, 3)
        grille.addWidget(QLabel("Scale"), 5, 1)
        grille.addWidget(self.scale_min, 5, 2)
        grille.addWidget(self.scale_max, 5, 3)

        #crée le bouton et l'ajouter au layout
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
        
        
      

        #crée le bon nombre d'item avec des formes random
        for i in range(self.number_objects.value()):
            forme = random.choice(["cube", "cylindre", "sphere"])
            if forme == "cube":
                objet = cmds.polyCube()[0]
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
            else:
                objet = cmds.polySphere()[0]

            # mets une valeur random dans la position x,y,z
            x_random_value = random.uniform(self.position_x_min.value(), self.position_x_max.value())
            y_random_value = random.uniform(self.position_y_min.value(), self.position_y_max.value())
            z_random_value = random.uniform(self.position_z_min.value(), self.position_z_max.value())
            cmds.move(x_random_value, y_random_value, z_random_value, objet)

            # mets une valeur random dans le scale
            scale = random.uniform(self.scale_min.value(), self.scale_max.value())
            cmds.scale(scale, scale, scale, objet)

        

        


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()