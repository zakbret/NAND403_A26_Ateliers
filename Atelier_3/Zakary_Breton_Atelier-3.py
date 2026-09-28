from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit, QMessageBox
 
class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        boite_texte = QTextEdit()
        bouton = QPushButton("Enter")
        layout.addWidget(label)
        layout.addWidget(boite_texte)
        layout.addWidget(bouton)
        



    def on_click(self):
        bouton_print = QMessageBox()
        bouton_print.setText()
        bouton_print.show()
        print("on click called")

 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()
 