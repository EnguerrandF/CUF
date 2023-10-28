from tkinter import filedialog, Tk, Label, Button
from tkinter.ttk import *

from controleur.copy_file import Clone

# Winwdow
window = Tk()
window.title("CUF")
window.geometry("500x270")
# window.minsize(300, 334)
# window.maxsize(1100, 334)
window.config(background="#666666")

# style
style = Style()
style.configure('W.TButton',
                font=("Courrier", 13),
                foreground='#666666',
                background='#FFE1A8',
                activeforeground='',
                activebackground='',
                )

style.configure('label_title.TLabel',
                font=("Courrier", 32),
                background="#666666",
                foreground='#FFE1A8',
                )
style.configure('label_paragraphe.TLabel',
                font=("Courrier", 10),
                background="#666666",
                foreground='#FFE1A8',
                )

# Label text
label_title = Label(window,
                    text="CUF",
                    style='label_title.TLabel')
label_paragraphe = Label(
    window,
    text="Sélectionne le dossier Source et de destination :",
    style='label_paragraphe.TLabel')
label_folder_source = Label(
    window,
    text="",
    style='label_paragraphe.TLabel')
label_folder_destination = Label(
    window,
    text="",
    style='label_paragraphe.TLabel')

# button
button_folder_source = Button(
    window,
    text="Dossier source",
    style='W.TButton',
    command=lambda: take_path_name("source"))
button_folder_destination = Button(
    window,
    text="Dossier de destination",
    style='W.TButton',
    command=lambda: take_path_name("destination"))
button_run_clone = Button(
    window,
    text="Lancer",
    style='W.TButton',
    command=lambda: Clone(path_folder_source, path_folder_destination))

path_folder_source = ""
path_folder_destination = ""


def take_path_name(name_lien):
    # recuperer le chemin d'un dossier
    global label_folder_source, label_folder_destination, path_folder_source, path_folder_destination

    name_folder = filedialog.askdirectory()

    if name_lien == "source":
        label_folder_source.config(text=name_folder)
        path_folder_source = name_folder + "/"
    elif name_lien == "destination":
        label_folder_destination.config(text=name_folder)
        path_folder_destination = name_folder + "/"


# pack
label_title.pack()
label_paragraphe.pack()
button_folder_source.pack(pady=8, padx=12)
label_folder_source.pack()
button_folder_destination.pack(pady=8, padx=12)
label_folder_destination.pack()
button_run_clone.pack(pady=8, padx=12)
