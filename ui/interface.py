from core.color import choose_random_color
import tkinter as tk
from tkinter import Menu, font
from ui.menu import criar_menu
from ui.buttons import criar_botoes

def criar_interface():
    estado = {"color": choose_random_color(), "topmost": False}
    window = tk.Tk()
    window.title("Post It")
    window.configure(bg=estado["color"])

    text_widget = tk.Text(window, bg=estado["color"], font=("Arial", 14), height=10, width=30, pady=10)
    text_widget.pack()

    bold_font = font.Font(weight="bold")
    italic_font = font.Font(slant="italic")
    text_widget.tag_configure("bold", font=bold_font)
    text_widget.tag_configure("italic", font=italic_font)
    text_widget.tag_configure("highlightline", background="yellow", relief="raised")

    menu_bar = Menu(window)
    window.config(menu=menu_bar)
    frame = tk.Frame(window, bg=estado["color"])
    frame.pack()
    
    criar_menu(menu_bar, text_widget, frame, estado, window, nova_janela)
    criar_botoes(frame, estado, text_widget)

    window.attributes("-topmost", estado["topmost"])
    window.geometry("300x300")
    window.mainloop()

def nova_janela():
    estado = {"color": choose_random_color(), "topmost": False}
    window = tk.Tk()
    
    window.title("Post It")
    window.configure(bg=estado["color"])

    text_widget = tk.Text(window, bg=estado["color"], font=("Arial", 14), height=10, width=30, pady=10)
    text_widget.pack()

    bold_font = font.Font(weight="bold")
    italic_font = font.Font(slant="italic")
    text_widget.tag_configure("bold", font=bold_font)
    text_widget.tag_configure("italic", font=italic_font)
    text_widget.tag_configure("highlightline", background="yellow", relief="raised")

    menu_bar = Menu(window)
    window.config(menu=menu_bar)
    frame = tk.Frame(window, bg=estado["color"])
    frame.pack()
    
    criar_menu(menu_bar, text_widget, frame, estado, window, nova_janela)
    criar_botoes(frame, estado, text_widget)

    window.attributes("-topmost", estado["topmost"])
    window.geometry("300x300")
    window.mainloop()