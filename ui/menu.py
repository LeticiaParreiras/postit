from tkinter import Menu
from core.color import colors
from core.functions import salvar_arquivo
from core.storage import carregar_postits
from core.storage import salvar_postit


def choose_color(name, text_widget, frame_widget, estado, window, ):
    estado["color"] = name
    text_widget.configure(bg=name)
    frame_widget.configure(bg=name)
    window.configure(bg=name)
    for widget in frame_widget.winfo_children():
        widget.configure(bg=name, activebackground=name)
        
def carregar_postit(window, estado, menu, text_widget):
    """Load saved post-its into a menu."""
    carregar_menu = Menu(menu, tearoff=0)
    postits = carregar_postits()
    
    if postits:
        for postit_item in postits:
            carregar_menu.add_command(
                label=postit_item["conteudo"][:30] + ("..." if len(postit_item["conteudo"]) > 30 else ""),
                command=lambda p=postit_item: carregar_conteudo(text_widget, p["conteudo"])
            )
        carregar_menu.add_separator()
        carregar_menu.add_command(
            label="Atualizar",
            command=lambda: atualizar_menu(window, estado, menu, text_widget, carregar_menu)
        )
    else:
        carregar_menu.add_command(label="Nenhum post-it salvo", state="disabled")
        carregar_menu.add_separator()
        carregar_menu.add_command(
            label="Atualizar",
            command=lambda: atualizar_menu(window, estado, menu, text_widget, carregar_menu)
        )
    
    return carregar_menu

def carregar_conteudo(text_widget, conteudo):
    """Load content into text widget, replacing existing content."""
    text_widget.delete("1.0", "end")
    text_widget.insert("1.0", conteudo)

def atualizar_menu(window, estado, menu, text_widget, carregar_menu):
    """Refresh the menu by recreating it."""
    # Clear existing menu items
    carregar_menu.delete(0, "end")
    
    # Reload post-its
    postits = carregar_postits()
    if postits:
        for postit_item in postits:
            carregar_menu.add_command(
                label=postit_item["conteudo"][:30] + ("..." if len(postit_item["conteudo"]) > 30 else ""),
                command=lambda p=postit_item: carregar_conteudo(text_widget, p["conteudo"])
            )
        carregar_menu.add_separator()
        carregar_menu.add_command(
            label="Atualizar",
            command=lambda: atualizar_menu(window, estado, menu, text_widget, carregar_menu)
        )
    else:
        carregar_menu.add_command(label="Nenhum post-it salvo", state="disabled")

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
    menu.add_cascade(label="Cor", menu=change_color_menu)
    menu.add_command(label="Fixar", command=lambda: toggle_topmost(window, estado, menu))
    arquivo_menu = Menu(menu, tearoff=0)
    arquivo_menu.add_cascade(label="Carregar Post-its", menu=carregar_postit(window, estado, menu, text_widget))
    arquivo_menu.add_command(label="Salvar", command=lambda: salvar_postit(text_widget.get("1.0", "end-1c"), estado))
    arquivo_menu.add_command(label="Exportar", command=lambda: salvar_arquivo(text_widget))
    menu.add_cascade(label="Arquivo", menu=arquivo_menu)
    
    menu.add_command(label="Novo Post It", command=nova_janela)
