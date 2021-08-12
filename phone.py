from tkinter import*
from tkinter.font import*
from os import chdir,getcwd
from tkinter.messagebox import*
from time import strftime
import tkcalendar
import pygame
from PIL import ImageTk,Image
from tkinter import filedialog
import os
from tkcalendar import*
import glob
fichier = "c:/repertoire"
chdir(fichier)


################################## programme repertoire #################################

#####fonction pour enregistrer un contact
def Ecriture():
    fen2 = Toplevel(fen1)
    fen2.geometry("250x250+250+150")
    fen2.title("ENREGISTRER CONTACT")
    contenu =Canvas(fen2)
    fontlabel = "arial 12 bold"
    fontentre = "arial 11 bold"
    #creation de label et button
    nom = Label(fen2,text="Nom :",font = fontlabel,fg="black",bg="white")
    prenom = Label(fen2,text="Prenom :",font = fontlabel,fg="black",bg="white")
    numero = Label(fen2,text="Numero :",font = fontlabel,fg="black",bg="white")
    btenregistrer=Button(fen2,text="ENREGISTRER",command=Enregistrer,fg="red",bg="grey")
    btquitter=Button(fen2,text="QUITTER",command=fen2.destroy,fg="red",bg="grey")
    #creation d'espace de saisie
    no = StringVar()
    pre = StringVar()
    num = IntVar()
    global nomEntre
    global prenomEntre
    global numeroEntre
    nomEntre = Entry(fen2,text=fontentre,textvariable=no)
    prenomEntre = Entry(fen2,text=fontentre,textvariable=pre)
    numeroEntre = Entry(fen2,text=fontentre,textvariable=num)

    #positionement des labels, des espaces de saisie et du bouttonnomEntre.grid(row=0,column=1,padx=5,pady=5)
    nom.grid(row = 0,column=0,sticky=E,padx=5,pady=5)
    prenom.grid(row = 1,column=0,sticky=E,padx=5,pady=5)
    numero.grid(row = 2,column=0,sticky=E,padx=5,pady=5)

    nomEntre.grid(row=0,column=1,padx=5,pady=5)
    prenomEntre.grid(row=1,column=1,padx=5,pady=5)
    numeroEntre.grid(row=2,column=1,padx=5,pady=5)
    btenregistrer.grid(row=4,column=1,sticky=E)
    btquitter.grid(row=4,column=0,sticky=E,)
    
def Enregistrer():
    ecrire = getcwd()
    ecrire = open("contact.txt","a")
    if nomEntre.get() and prenomEntre.get() and numeroEntre.get() :
        nom = nomEntre.get()
        prenom = prenomEntre.get()
        numero = numeroEntre.get()
        ecrire.write(nom +" "+prenom+" "+ str(numero)+"\n")
        ecrire.close()
        nomEntre.delete(0,END)
        prenomEntre.delete(0,END)
        numeroEntre.delete(0,END)
        showinfo(title="enregistrement reussi",message="Le contact a ete enregistrer")
    else:
        showerror(message="Contact non valide")

##############AFFICHAGE DE LA LISTE DES CONTACTS
def Afficher():
    global lb
    global l
    n=0
    fen3 = Toplevel(fen1)
    fen3.title("Liste contact")
    fen3.geometry("300x300+250+150")
    affiche = getcwd()
    affiche = open("contact.txt","r")
    contenu = Frame(fen3,width=200,height=200)
    contenu.pack()
    con = Frame(fen3,width=50,height=50,relief=GROOVE)

    #ajout du scrollbar
    scroll =Scrollbar(contenu,orient=VERTICAL)
    con.pack(expand="1",fill=BOTH)

    #creation de la liste
    lb = Listbox(contenu,width=30,activestyle="none",selectmode="single",cursor="hand2",yscrollcommand=scroll.set)
    for line in affiche:
        lb.insert(END,line)
    l = Label(con,text="")

    #affichage des elements
    lb.bind("<<ListboxSelect>>",select)
    l.pack(anchor= CENTER) 
    # configuration scrollbar
    scroll.config(command=lb.yview)
    scroll.pack(side=RIGHT,fill=Y)
    lb.pack(pady=15)

    btquitter = Button(fen3,text="QUITTER",command=fen3.destroy)
    btquitter.pack(padx=10,pady=10)


#################RECHERCHE DES CONTACTS
def select(event):
    sel = lb.selection_get()
    l.configure(text=sel)
    

def Rechercher():
    global fen4
    global nmEntre
    fen4 =Toplevel(fen1)
    no = StringVar()
    fen4.geometry("300x250+250+150")
    fontlabel = "arial 12 bold"
    fontentre = "arial 11 bold"
    nm = Label(fen4,text="saisir ici :",font = fontlabel,fg="black",bg="white")
    nmEntre = Entry(fen4,text=fontentre,textvariable=no)
    nm.grid(row = 0,column=0,sticky=E,padx=5,pady=5)
    nmEntre.grid(row=0,column=1,padx=5,pady=5)
    btcherche=Button(fen4,text="RECHERCHER",command=Recherche,fg="red",bg="grey")
    btcherche.grid(row=2 ,column=1,sticky=E,padx=10,pady=10)
    btquitter=Button(fen4,text="QUITTER",command=fen4.destroy,fg="red",bg="grey")
    btquitter.grid(row=2,column=0,sticky=W,padx=10,pady=10)

def Recherche():
    fichier = "c:/repertoire"
    chdir(fichier)
    cherche = getcwd()
    cherche = open("contact.txt", "r")
    nom = " "  
    for line in cherche:
        if nmEntre.get():
            nom = nmEntre.get()
            if nom in line :
                con =Label (fen4,text=line,fg="blue")
                con.grid(row =6,column=1) 
                nmEntre.delete(0,END)
        else:
            showerror(message="Veuillez indiquer un nom")  


#############creation de l'appli de musique
def ajouterson():
    son = filedialog.askdirectory()
    fichier=os.chdir(son)
    music = os.listdir()
    for m in music :
        musicbox.insert(END,m)

def play():
    music = musiquebox.get(ACTIVE)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=0)    

def stop():
    music = musiquebox.get(ACTIVE)
    pygame.mixer.music.load(music)
    pygame.mixer.music.stop()

def pause():
    music = musiquebox.get(ACTIVE)
    pygame.mixer.music.load(music)
    pygame.mixer.music.pause() 

def resumer():
    music = musiquebox.get(ACTIVE)
    pygame.mixer.music.load(music)
    pygame.mixer.music.unpause()           

def musique():
    global musiquebox
    fen6 = Toplevel(fen1)
    fen6.title("Music player")
    fen6.geometry("500x500+250+150")
    firstmenu = Menu(fen6)
    fen6.config(menu=firstmenu)
    ajoutson = Menu(firstmenu)
    firstmenu.add_cascade(label="Ajouter du son",menu=ajoutson)
    ajoutson.add_command(label="choisir le dossier ",command=ajouterson)
    contenu = Frame(fen6,width=200,height=200,bg="sky blue")
    contenu.pack(fill=X,padx=1,pady=1)
    pygame.mixer.init()

    scroll =Scrollbar(contenu,orient=VERTICAL)
    musiquebox=Listbox(contenu,fg="black",width=200,activestyle="none",selectmode="single",cursor="hand2",yscrollcommand=scroll.set)
    for i in glob.glob('/Users/TOTO/Desktop/2TO MUSIC/*.*'):
        musiquebox.insert(END,i)
        

    scroll.config(command=musiquebox.yview)
    scroll.pack(side=RIGHT,fill=Y)
    musiquebox.pack(padx=20)

    control = Frame(fen6,width=200,height=50,bg="sky blue")
    control.pack(fill=X,padx=2,pady=2)

    btplay =Button(control,width=7,height=2,text="PLAY",command=play,foreground="blue")
    btpause =Button(control,width=7,height=2,text="PAUSE",command=pause,foreground="blue")
    btresume =Button(control,width=10,height=2,text="RESUME",command=resumer,foreground="blue")
    btstop =Button(control,width=7,height=2,text="STOP",command=stop,foreground="blue")

    btplay.pack(side=LEFT,padx=30)
    btpause.pack(side=LEFT,padx=30)
    btstop.pack(side=RIGHT,padx=30)
    btresume.pack(side=RIGHT,padx=30)

    btquitter =Button(fen6,text="QUITTER",command=fen6.destroy)
    btquitter.pack(anchor=CENTER,pady=50)


######### appli video
def ajouterdeo():
    deo = filedialog.askdirectory()
    fichier=os.chdir(deo)
    videos = os.listdir()
    for m in videos :
        videobox.insert(END,m)

def playdeo():
    deos = videobox.get(ACTIVE)
    os.startfile(deos)

def video():
    global videobox
    fen7 = Toplevel(fen1)
    fen7.title("Video player")
    fen7.geometry("500x500+250+150")
    firstmenu = Menu(fen7)
    fen7.config(menu=firstmenu)
    ajoutdeo = Menu(firstmenu)
    firstmenu.add_cascade(label="Ajouter du video",menu=ajoutdeo)
    ajoutdeo.add_command(label="choisir le dossier video",command=ajouterdeo)
    contenu = Frame(fen7,width=200,height=200)
    contenu.pack(fill=X,padx=1,pady=1)
    contenu.pack()
    scroll = Scrollbar(contenu,orient=VERTICAL)
    videobox = Listbox(contenu,fg="black",width=200,activestyle="none",selectmode="single",cursor="hand2",yscrollcommand=scroll.set)

    for i in glob.glob('/Users/TOTO/Desktop/films/*.*'):
        videobox.insert(END,i)

    scroll.config(command=videobox.yview)
    scroll.pack(side=RIGHT,fill=Y)
    videobox.pack(padx=20)
    videobox.bind("<Double-Button>",playdeo)
    control = Frame(fen7,width=200,height=50)
    control.pack(fill=X,padx=2,pady=2)
    btplay = Button(control,text="PLAY",fg="blue",command=playdeo)
    btplay.pack()
    btquitter=Button(fen7,text="QUITTER",command=fen7.destroy)
    btquitter.pack(anchor=CENTER,pady=20)


######################## CREATION DE LA FENETRE PRINCIPALE ET SES COMPOSANTS
fen1 = Tk()
fen1.geometry("800x800+350+20")
fen1.title("phone")



#creation des conteneur
frme0 = Frame(fen1,bg = "#d0d0ff",width=200,height=100,relief=FLAT,border=4)
frme0.pack(pady = 10,padx=10,fill=BOTH)
frme1 =Frame(fen1,width=50,height=50,border=10)
frme1.pack(anchor=CENTER,fill=Y)


#creation du menu
firstmenu = Menu(fen1)
phonebook = Menu(firstmenu)
firstmenu.add_cascade(label ="Phonebook",menu=phonebook)
phonebook.add_command(label ="Enregistrer un contact",command =Ecriture)
phonebook.add_command(label ="Afficher contacts",command =Afficher)
phonebook.add_command(label ="Rechercher un contact",command =Rechercher)


media = Menu(firstmenu)
firstmenu.add_cascade(label ="Media",menu =media)
media.add_command(label="Musique",command=musique)
media.add_command(label="Video",command=video)
fen1.config(menu = firstmenu)

########creation de l'horloge

horlo = Label(frme0,font=("arial",80),foreground="blue")
horlo.pack(anchor="center")
def horloge():
    string = strftime("%H:%M:%S")
    horlo.config(text=string)
    horlo.after(1000,horloge)
horloge()

########creation des bouttons contact et musique

imgmusic = Image.open("/Users/TOTO/Desktop/code_python/music.png")
imgmus = imgmusic.resize((200,200),Image.ANTIALIAS)
imgmu =  ImageTk.PhotoImage(imgmus)
btmusic = Button(frme1,image=imgmu,command= musique)
btmusic.pack(side=LEFT,padx = 10,pady=10)

imgcontact = Image.open("/Users/TOTO/Desktop/code_python/contact.png")
imgcont = imgcontact.resize((200,200),Image.ANTIALIAS)
imgcon = ImageTk.PhotoImage(imgcont)

btcontact = Button(frme1,image=imgcon,command=Afficher)
btcontact.pack(side=RIGHT,padx = 10,pady=10)


########creation du calendrier
cal = Calendar(frme1,year =2021,month=8,day=11)
cal.pack(side = RIGHT,padx=10,pady=10)

#creation de la galerie
photoliste = [ ]
for i in glob.glob('/Users/TOTO/Desktop/photo/*.*'):
    img = Image.open(i)
    tof  = img.resize((500,400),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(tof)
    photoliste.append(photo)
photoLabel= Label(fen1,bg="sky blue")
j = 0
def diapo():
    global j
    try :
       photoLabel.config(image=photoliste[j])
       fen1.after(2000,diapo)
       j = j +1
    except:
       j = j+1

    if j == len(photoliste):
        j=0   

photoLabel.pack(fill=BOTH)
fen1.after(100,diapo) 

fen1.mainloop()
