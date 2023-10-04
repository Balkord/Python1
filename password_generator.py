from tkinter import *
from random import randint, choice
import string


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    
    
# creer la fenetre
window = Tk()
window.title("Generateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("") # iconne de l'interface graphique
window.config(background='#4065A4')

# creer la frame principale
frame= Frame(window, bg="#4065A4")

#creation d'image
width = 512
height = 512
image = PhotoImage(file="Python/reset-password.png").zoom(35).subsample(25)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creer une sous boite
right_frame = Frame(frame, bg='#4065A4')

#creer un titre
label_tittle = Label(right_frame, text='Mot de passe', font=("Helvetica", 20), bg='#4065A4', fg='white')
label_tittle.pack()

#creer un champ/entrée/input
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

# creer un button
generate_password_button = Button(right_frame, text='Générer', font=("Helvetica", 20), bg='#4065A4', fg='white', command=generate_password)
generate_password_button.pack(fill=X)


# on place la sous boite à droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

# creation de la barre de menue
menu_barre = Menu(window)

# creer un premier menu
file_menu = Menu(menu_barre, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_barre.add_cascade(label="Fichier", menu=file_menu )

# configurer notre fenetre pour ajouter cette menu bar
window.config(menu=menu_barre)

#afficher la fenetre
window.mainloop()