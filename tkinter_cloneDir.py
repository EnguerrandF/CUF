from cProfile import label
from re import L
from tkinter import *
from tkinter import dialog
from tkinter import filedialog
from tkinter.filedialog import askdirectory, askopenfilename
from master import run
from tkinter.ttk import *

#ma fenêtre
window = Tk()
window.title("CloneDir")
window.geometry("500x334")
window.minsize(600, 334)
window.maxsize(1100, 334)
window.config(background="#666666")

#style
style = Style()
style.configure('W.TButton', 
                font=("Courrier", 13),
                foreground = '#666666',
                background = '#FFE1A8',
                activeforeground = '',
                activebackground = '',            
                )

style.configure('label_title.TLabel',
                font=("Courrier", 32), 
                background="#666666",
                foreground = '#FFE1A8',
                )
style.configure('label_paragraphe.TLabel',
                font=("Courrier", 10), 
                background="#666666",
                foreground = '#FFE1A8',
                )

#ajouter un texte 
label_title = Label(window, text="CloneDir", style='label_title.TLabel')
label_paragraphe = Label(window, text="Sélectionne le dossier de destination et dossier source:", style='label_paragraphe.TLabel')
label_dossier_travail = Label(window, text="", style='label_paragraphe.TLabel')
label_dossier_clone = Label(window, text="", style='label_paragraphe.TLabel')

#button
button_dossier_travail = Button(window, text="Dossier de source", style= 'W.TButton', command= lambda: dossier("travaille"))
button_dossier_clone = Button(window, text="Dossier destination", style= 'W.TButton', command= lambda: dossier("clone"))
button_run_clone = Button(window, text="Lancer le clone", style= 'W.TButton', command= lambda: lancerClone(info_dossier_travail, info_dossier_clone))



#variable des chemins
info_dossier_travail = ""
info_dossier_clone = ""

#recuperer le chemin d'un dossier
def dossier(name_lien):
    global label_dossier_travail, label_dossier_clone, info_dossier_clone, info_dossier_travail
    name_dossier = filedialog.askdirectory()

    if name_lien == "travaille":
        label_dossier_travail.config(text=name_dossier)
        info_dossier_travail = name_dossier + "/"
    elif name_lien == "clone":
        label_dossier_clone.config(text=name_dossier)
        info_dossier_clone = name_dossier + "/"
    print(info_dossier_travail, info_dossier_clone )
        
def lancerClone(dossier1, dossier2):
    run(dossier1, dossier2)


#pack
label_title.pack()
label_paragraphe.pack()
button_dossier_travail.pack(pady= 8, padx= 12)
label_dossier_travail.pack()
button_dossier_clone.pack(pady= 8, padx= 12)
label_dossier_clone.pack()
button_run_clone.pack(pady= 8, padx= 12)

#afficher la fenetre
window.mainloop()

