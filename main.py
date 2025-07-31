import tkinter as tk
from tkinter import font
import random

def choose_color():
    return random.choice(["yellow2", "maroon2", "purple2"])

def toggle_tag(tag_name):
    try:
        start = text.index("sel.first")
        end = text.index("sel.last")
        # Verifica se o texto selecionado já tem a tag
        if tag_name in text.tag_names("sel.first"):
            text.tag_remove(tag_name, start, end)
        else:
            text.tag_add(tag_name, start, end)
    except tk.TclError:
        pass  # Nenhuma seleção feita
    
    
def add_bullet():
    try:
        start_line = text.index("insert linestart")
        if not text.get(start_line, f"{start_line}+2c") == "• ":
            text.insert(start_line, "• ")
    except tk.TclError:
        pass

    

# Criação da janela
window = tk.Tk()
window.title("Post It")
color = choose_color()
window.configure(bg=color)

# Fontes
bold_font = font.Font(weight="bold")
italic_font = font.Font(slant="italic")

# Widget de texto
text = tk.Text(window,
               bg=color,
               font=("Arial", 14),
               height=15,
               width=60,
               padx=10,
               pady=10)
text.pack()

# Tags de formatação
text.tag_configure("bold", font=bold_font)
text.tag_configure("italic", font=italic_font)
text.tag_configure('highlightline', background='yellow', relief='raised')

# Botões
frame = tk.Frame(window, bg=color)
frame.pack(pady=10)

bold_button = tk.Button(frame, text="N",  bg=color, activebackground=color, command=lambda: toggle_tag("bold"))
bold_button.grid(row=0, column=0, padx=5)

italic_button = tk.Button(frame, text="I", bg=color, activebackground=color,  command=lambda: toggle_tag("italic"))
italic_button.grid(row=0, column=1, padx=5)

bullet_button = tk.Button(frame, text="•", bg=color, activebackground=color, command=add_bullet)
bullet_button.grid(row=0, column=2, padx=5)

highlightline_button = tk.Button(frame, text="H", bg=color, activebackground=color,  command=lambda: toggle_tag('highlightline'))
highlightline_button.grid(row=0, column=3, padx=5)

window.geometry("400x400")
window.mainloop()
