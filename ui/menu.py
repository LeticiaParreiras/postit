from tkinter import Menu
from core.color import colors
from core.functions import salvar_arquivo
from core.storage import carregar_postits
from core.storage import salvar_postit
from core.storage import deletar_postit
from tkinter import messagebox


def choose_color(name, text_widget, frame_widget, estado, window, ):
    estado["color"] = name
    text_widget.configure(bg=name)
    frame_widget.configure(bg=name)
    window.configure(bg=name)
    for widget in frame_widget.winfo_children():
        widget.configure(bg=name, activebackground=name)
        
def carregar_postit(menu, text_widget, frame_widget, estado, window, nova_janela):
    """Exibir os Post it salvos no menu."""
    carregar_menu = Menu(menu, tearoff=0)
    postits = carregar_postits()
    
    if postits:
        for postit_item in postits:
            carregar_menu.add_command(
                label=postit_item["conteudo"][:30] + ("..." if len(postit_item["conteudo"]) > 30 else ""),
                command=lambda p=postit_item: carregar_conteudo(menu, text_widget, frame_widget, estado, window, nova_janela, p)
            )
    else:
        carregar_menu.add_command(label="Nenhum post-it salvo", state="disabled")
    
    return carregar_menu

def carregar_conteudo(menu, text_widget, frame_widget, estado, window, nova_janela, postit):
    """Carregar Conteúdo."""
    text_widget.delete("1.0", "end")
    text_widget.insert("1.0", postit["conteudo"])
    estado["id"] = postit["id"]
    estado["color"] = postit["cor"]
    atualizar_menu(menu, text_widget, frame_widget, estado, window, nova_janela)
    
def salvar_atualizar(menu, text_widget, frame_widget, estado, window, nova_janela):
    """Salva ou Atualiza o post-it e atualiza o menu."""
    conteudo = text_widget.get("1.0", "end")
    if conteudo:
        salvar_postit(conteudo, estado)
        atualizar_menu(menu, text_widget, frame_widget, estado, window, nova_janela)
        
def deletar_postit_e_atualizar(estado, text_widget, menu, frame_widget, window, nova_janela):
    """Deleta o post-it e atualiza o menu."""
    response = messagebox.askyesno(
        "Deletar Post-it",
        "Você tem certeza que deseja deletar este post-it?"
    )
    if response:
        deletar_postit(estado, text_widget)
        atualizar_menu(menu, text_widget, frame_widget, estado, window, nova_janela)

def toggle_topmost(window, estado, menu):
    estado["topmost"] = not estado["topmost"]
    window.attributes("-topmost", estado["topmost"])
    if estado["topmost"]:
        menu.entryconfig("Fixar", label="Desafixar")
    else:
        menu.entryconfig("Desafixar", label="Fixar")

def criar_menu(menu, text_widget, frame_widget, estado, window, nova_janela):
    """Cria o menu principal."""
    #Menu de mudar cor
    change_color_menu = Menu(menu, tearoff=0)
    for nome, cor_valor in colors.items():
        change_color_menu.add_command(
            label=nome,
            command=lambda c=cor_valor: choose_color(c, text_widget, frame_widget, estado, window)
        )
    menu.add_cascade(label="Cor", menu=change_color_menu)
    menu.add_command(label="Fixar", command=lambda: toggle_topmost(window, estado, menu))
    # Menu Arquivo
    arquivo_menu = Menu(menu, tearoff=0)
    arquivo_menu.add_cascade(label="Carregar Post-its", menu=carregar_postit(menu, text_widget, frame_widget, estado, window, nova_janela))
    arquivo_menu.add_command(label="Salvar", command=lambda: salvar_atualizar(menu, text_widget, frame_widget, estado, window, nova_janela))
    arquivo_menu.add_separator()
    arquivo_menu.add_command(label="Atualizar",command=lambda: atualizar_menu(menu, text_widget, frame_widget, estado, window, nova_janela))
    # Opção de Deletar só aparece se tem ID
    if estado.get("id"):
        arquivo_menu.add_command(
            label="Deletar",
            command=lambda: deletar_postit_e_atualizar(estado, text_widget, menu, frame_widget, window, nova_janela)
        )
    
    arquivo_menu.add_command(label="Exportar", command=lambda: salvar_arquivo(text_widget))
    menu.add_cascade(label="Arquivo", menu=arquivo_menu)
    menu.add_command(label="Novo Post It", command=nova_janela)

def atualizar_menu(menu, text_widget, frame_widget, estado, window, nova_janela):
    """Refresh the menu by recreating it."""
    # Clear existing menu items
    menu.delete(0, "end")
    
    criar_menu(menu, text_widget, frame_widget, estado, window, nova_janela)