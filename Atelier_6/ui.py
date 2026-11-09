from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit, QMessageBox
 

class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        self.boite_texte = QTextEdit()
        bouton = QPushButton("Enter")
        bouton.clicked.connect(self.on_click)
        layout.addWidget(label)
        layout.addWidget(self.boite_texte)
        layout.addWidget(bouton)