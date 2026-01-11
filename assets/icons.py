import tkinter as tk
import os
import sys
def get_resource_path(relative_path):
    """Obtém o caminho correto dos recursos, tanto para desenvolvimento quanto para executável."""
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Se não estiver rodando como executável, usa o caminho normal
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    return os.path.join(base_path, relative_path)

def criar_icones():
    return {
    "bold": tk.PhotoImage(file=get_resource_path("assets/images/bold.png")),
    "italic": tk.PhotoImage(file=get_resource_path("assets/images/italic.png")),
    "list": tk.PhotoImage(file=get_resource_path("assets/images/list.png")),
    "highlight": tk.PhotoImage(file=get_resource_path("assets/images/highlighter.png")),
}