import tkinter as tk
from tkinter import filedialog

def toggle_tag(tag_name, text_widget):
    try:
        start = text_widget.index("sel.first")
        end = text_widget.index("sel.last")
        if tag_name in text_widget.tag_names("sel.first"):
            text_widget.tag_remove(tag_name, start, end)
        else:
            text_widget.tag_add(tag_name, start, end)
    except tk.TclError:
        pass

def add_bullet(text_widget):
    try:
        start_line = text_widget.index("insert linestart")
        if not text_widget.get(start_line, f"{start_line}+2c") == "• ":
            text_widget.insert(start_line, "• ")
    except tk.TclError:
        pass

def salvar_arquivo(text_widget):
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text_widget.get("1.0", tk.END))
