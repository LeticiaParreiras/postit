import tkinter as tk
from assets.icons import criar_icones
from core.functions import toggle_tag, add_bullet

def criar_botoes(frame, estado, text_widget):
    icones = criar_icones()
    botoes = [
        {"img": icones["bold"], "cmd": lambda: toggle_tag("bold", text_widget)},
        {"img": icones["italic"], "cmd": lambda: toggle_tag("italic", text_widget)},
        {"img": icones["list"], "cmd": lambda: add_bullet(text_widget)},
        {"img": icones["highlight"], "cmd": lambda: toggle_tag("highlightline", text_widget)},
    ]
    frame.imagens = []

    for i, btn in enumerate(botoes):
        frame.imagens.append(btn["img"])
        b = tk.Button(
            frame,
            image=btn["img"],
            bg=estado["color"],
            activebackground=estado["color"],
            command=btn["cmd"],
            bd=0,
            relief="flat",
            cursor="hand2",
        )
        b.grid(row=0, column=i)
