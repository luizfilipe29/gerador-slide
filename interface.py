import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter.colorchooser import askcolor
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import logic

def on_submit(song_name_entry, lyrics_text_box, font_size_var, font_color_var, bg_color_var, lines_per_slide_var, color_dict):
    song_name = song_name_entry.get().strip()
    lyrics = lyrics_text_box.get("1.0", tk.END).strip()
    font_size = font_size_var.get()
    font_color = color_dict[font_color_var.get()]
    bg_color = bg_color_var.get()
    max_lines_per_slide = lines_per_slide_var.get()
    
    if not song_name:
        messagebox.showerror("Erro", "O campo 'Nome da música' não pode estar vazio.")
        return
    if not lyrics:
        messagebox.showerror("Erro", "A caixa de texto da letra não pode estar vazia.")
        return
    
    logic.generate_slides_from_lyrics(lyrics, song_name, font_size, font_color, bg_color, max_lines_per_slide)
    messagebox.showinfo("Sucesso", f"O arquivo {song_name}.pptx foi salvo com sucesso.")
    
    clear_text_boxes(song_name_entry, lyrics_text_box)

def clear_text_boxes(song_name_entry, lyrics_text_box):
    song_name_entry.delete(0, tk.END)
    lyrics_text_box.delete("1.0", tk.END)

def update_selected_color(color_label, color):
    color_label.config(bg=color)

def create_interface():
    root = tk.Tk()
    root.title("Gerador de Slides de Letras de Música")
    root.geometry("800x600")

    colors = [
        ("Preto", (0, 0, 0)),
        ("Branco", (255, 255, 255)),
        ("Vermelho", (255, 0, 0)),
        ("Verde", (0, 255, 0)),
        ("Azul", (0, 0, 255)),
        ("Amarelo", (255, 255, 0)),
        ("Ciano", (0, 255, 255)),
        ("Magenta", (255, 0, 255))
    ]
    color_dict = {name: rgb for name, rgb in colors}

    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)

    song_name_label = tk.Label(root, text="Nome da música:", font=("Arial", 14))
    song_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    song_name_entry = tk.Entry(root, width=50, font=("Arial", 12))
    song_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    lyrics_label = tk.Label(root, text="Letra da música:", font=("Arial", 14))
    lyrics_label.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

    lyrics_text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Arial", 12))
    lyrics_text_box.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    font_size_label = tk.Label(root, text="Tamanho da fonte:", font=("Arial", 14))
    font_size_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    font_size_var = tk.IntVar(value=50)
    font_size_menu = tk.OptionMenu(root, font_size_var, *range(12, 102, 2))
    font_size_menu.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    font_color_label = tk.Label(root, text="Cor da fonte:", font=("Arial", 14))
    font_color_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    font_color_var = tk.StringVar(value="Preto")
    font_color_menu = tk.OptionMenu(root, font_color_var, *color_dict.keys())
    font_color_menu.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    bg_color_label = tk.Label(root, text="Cor do fundo:", font=("Arial", 14))
    bg_color_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    bg_color_var = tk.StringVar(value="Branco")
    bg_color_menu = tk.Button(root, text="Selecionar Cor", command=lambda: select_bg_color(bg_color_var, selected_color_display, color_dict))
    bg_color_menu.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    selected_color_label = tk.Label(root, text="Cor selecionada:", font=("Arial", 14))
    selected_color_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    selected_color_display = tk.Label(root, width=10, height=5)
    selected_color_display.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    lines_per_slide_label = tk.Label(root, text="Linhas por slide:", font=("Arial", 14))
    lines_per_slide_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    lines_per_slide_var = tk.IntVar(value=4)
    lines_per_slide_menu = tk.OptionMenu(root, lines_per_slide_var, *list(range(1, 11)))
    lines_per_slide_menu.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    generate_slides_button = tk.Button(root, text="Gerar Slides", command=lambda: on_submit(song_name_entry, lyrics_text_box, font_size_var, font_color_var, bg_color_var, lines_per_slide_var, color_dict), font=("Arial", 12), padx=10, pady=5)
    generate_slides_button.grid(row=7, column=1, padx=10, pady=20, sticky="e")

    root.mainloop()

def select_bg_color(bg_color_var, selected_color_display, color_dict):
    color = askcolor()[1]
    if color:
        bg_color_var.set(color)
        update_selected_color(selected_color_display, color)

def update_selected_color(color_label, color):
    color_label.config(bg=color)

if __name__ == "__main__":
    root = create_interface()    
