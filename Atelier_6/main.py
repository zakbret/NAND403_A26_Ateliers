import os
import sys
import importlib
import Atelier_6.ui as ui
importlib.reload(ui)





#def my_function():
    #absolute_file_path = os.path.abspath(__file__)
    #absolute_folder_path = os.path.dirname(absolute_file_path)

# __file__ = le fichier courant
#absolute_file_path = os.path.abspath(__file__)
#absolute_folder_path = os.path.dirname(absolute_file_path)
#sys.path.append(absolute_folder_path)

#from ui import MyClass




def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = ui.MessageBoard()
    widget.show()
 
main()