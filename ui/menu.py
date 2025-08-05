from tkinter import Menu
from core.color import colors
from core.functions import salvar_arquivo


def choose_color(name, text_widget, frame_widget, estado, window):
    estado["color"] = name
    text_widget.configure(bg=name)
    frame_widget.configure(bg=name)
    window.configure(bg=name)
    for widget in frame_widget.winfo_children():
        widget.configure(bg=name, activebackground=name)

def toggle_topmost(window, estado, menu):
    estado["topmost"] = not estado["topmost"]
    window.attributes("-topmost", estado["topmost"])
    if estado["topmost"]:
        menu.entryconfig("Fixar", label="Desafixar")
    else:
        menu.entryconfig("Desafixar", label="Fixar")

def criar_menu(menu, text_widget, frame_widget, estado, window, nova_janela):
    change_color_menu = Menu(menu, tearoff=0)
    for nome, cor_valor in colors.items():
        change_color_menu.add_command(
            label=nome,
            command=lambda c=cor_valor: choose_color(c, text_widget, frame_widget, estado, window)
        )
    menu.add_cascade(label="Mudar cor", menu=change_color_menu)
    menu.add_command(label="Fixar", command=lambda: toggle_topmost(window, estado, menu))
    menu.add_command(label="Salvar", command=lambda: salvar_arquivo(text_widget))
    menu.add_command(label="Novo", command=nova_janela)
