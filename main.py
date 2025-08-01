import tkinter as tk
from tkinter import font, filedialog
import random

def choose_color():
    """Escolhe uma cor de fundo aleatória."""
    return random.choice(["yellow2", "maroon2", "purple2", "skyblue2", "green3", "orange2", "snow"])

def salvar_arquivo(text_widget):
    """Abre uma caixa de diálogo para salvar o conteúdo do Text."""
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text_widget.get("1.0", tk.END))

def toggle_tag(tag_name, text_widget):
    """Aplica ou remove a tag de formatação ao texto selecionado."""
    try:
        start = text_widget.index("sel.first")
        end = text_widget.index("sel.last")
        if tag_name in text_widget.tag_names("sel.first"):
            text_widget.tag_remove(tag_name, start, end)
        else:
            text_widget.tag_add(tag_name, start, end)
    except tk.TclError:
        pass  # Nenhuma seleção

def add_bullet(text_widget):
    """Adiciona um bullet (•) no início da linha atual, se ainda não tiver."""
    try:
        start_line = text_widget.index("insert linestart")
        if not text_widget.get(start_line, f"{start_line}+2c") == "• ":
            text_widget.insert(start_line, "• ")
    except tk.TclError:
        pass

def criar_botoes(frame, color, text_widget):
    """Cria e posiciona os botões com suas funcionalidades."""
    botoes = [
        {"text": "N", "cmd": lambda: toggle_tag("bold", text_widget)},
        {"text": "I", "cmd": lambda: toggle_tag("italic", text_widget)},
        {"text": "•", "cmd": lambda: add_bullet(text_widget)},
        {"text": "H", "cmd": lambda: toggle_tag("highlightline", text_widget)},
        {"text": "Save", "cmd": lambda: salvar_arquivo(text_widget)},
    ]

    for i, btn in enumerate(botoes):
        b = tk.Button(
            frame,
            text=btn["text"],
            bg=color,
            activebackground=color,
            command=btn["cmd"],
            bd=0,
            highlightthickness=0,
            relief="flat",
            cursor="hand2",
            font=("Arial", 14),
            width=6 if btn["text"] == "Save" else 3,
            height=1
        )
        b.grid(row=0, column=i, padx=5)

def main():
    window = tk.Tk()
    window.title("Post It")

    color = choose_color()
    window.configure(bg=color)

    bold_font = font.Font(weight="bold")
    italic_font = font.Font(slant="italic")

    text_widget = tk.Text(window,
                          bg=color,
                          font=("Arial", 14),
                          height=10,
                          width=30,
                          pady=10)
    text_widget.pack()

    text_widget.tag_configure("bold", font=bold_font)
    text_widget.tag_configure("italic", font=italic_font)
    text_widget.tag_configure('highlightline', background='yellow', relief='raised')

    frame = tk.Frame(window, bg=color)
    frame.pack()

    criar_botoes(frame, color, text_widget)

    window.attributes("-topmost", True)
    window.geometry("300x300")
    window.mainloop()

if __name__ == "__main__":
    main()
