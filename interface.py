from tkinter import *
import webbrowser

def open_graven_channel():
    webbrowser.open_new("http://youtube.com")

#crer une premiere fenêtre
window = Tk()

# personaliser cette fenêtre
window.title("My application")
window.geometry("300x300")
window.minsize(480, 360)
window.iconbitmap("") # logo dans le coin de l'interface
window.config(background='#41B77F')

# creer la fram
frame = Frame(window, bg='#41B77F')

# ajouter un premier texte
Label_title = Label(frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#41B77F', fg="white")
Label_title.pack()

# ajouter un second texte
Label_subtitle = Label(frame, text="Hey salut a tous", font=("Courrier", 25), bg='#41B77F', fg="white")
Label_subtitle.pack()

# ajouter un premier bouton
yt_button = Button(frame, text="Ouvrire youtube", font=("Courier", 25), bg='white', fg='#41B77F', command=open_graven_channel)
yt_button.pack(pady=25, fill=X)

#ajouter
frame.pack(expand=YES)

# afficher
window.mainloop()