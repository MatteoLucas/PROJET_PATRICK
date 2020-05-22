"""-------- IMPORTATION DES BIBLIOTHEQUES --------"""
from tkinter import *
import threading
from tkinter import simpledialog
import os
from PIL import ImageTk
import time




"""-------- CREATION DES CLASSES POUR CHAQUE BLOC --------"""
class Print:
    id = 1
    entry = ""
    display = 'Valeur à afficher (entre "" pour string)'
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgPrint)
    def getEntry(self):
        return self.entry
    def getGenId(self):
        return self.bId

class endOfLoop:
    id = 5
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgEndOfLoop)
    def getGenId(self):
        return self.bId

class If:
    id = 2
    entry = ""
    display = "Condition à remplir (a == true)"
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgIf)
    def getEntry(self):
        return self.entry
    def getGenId(self):
        return self.bId

class Else:
    id = 3
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgElse)
    def getGenId(self):
        return self.bId

class While:
    id = 4
    entry = ""
    display = "Condition à remplir (a <= 4)"
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgWhile)
    def getEntry(self):
        return self.entry
    def getGenId(self):
        return self.bId

class For:
    id = 6
    entry = ""
    display = "Nombre de fois à répéter"
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgFor)
    def getEntry(self):
        return self.entry
    def getGenId(self):
        return self.bId

class Variable:
    id = 7
    entry = ""
    display = "Directement retranscrit en python"
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgVar)
    def getEntry(self):
        return self.entry
    def getGenId(self):
        return self.bId

class Debut:
    id = 8
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgDeb)
    def getGenId(self):
        return self.bId

class Delay:
    id = 9
    entry = ""
    display = "Temps à attendre en secondes :"
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgDelay)
    def getEntry(self):
        return self.entry
    def getGenId(self):
        return self.bId

class Random:
    id = 10
    entry1 = ""
    entry2 = ""
    entry3 = ""
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgRandom)
    def getEntry1(self):
        return self.entry1
    def getEntry2(self):
        return self.entry2
    def getEntry3(self):
        return self.entry3
    def getGenId(self):
        return self.bId

class Input:
    id = 11
    entry = ""
    display = "Variable a renseigner :"
    def __init__(self):
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=imgInput)
    def getEntry(self):
        return self.entry
    def getGenId(self):
        return self.bId




"""-------- CREATION DES FONCTION POUR LE DEPLACEMENT DES BLOCS --------"""
class Colision(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global ordre
        self.running = True
        while self.running :

            nbCarreActuel = nbCarre
            listeColision = []

            for n in range(0, nbCarreActuel) :
                listeColision.append(list())
                listeColision[n].append(n)

            for n in range(0, nbCarreActuel) :
                [Xmin, Ymin] = Canevas.coords(Carre[n])
                colision = Canevas.find_overlapping(Xmin, Ymin, Xmin + L, Ymin + H)

                # Colision de 3 blocs
                if len(colision) == 3 :
                    [xmin1, ymin1] = Canevas.coords(Carre[colision[0] - 1])
                    [xmin2, ymin2] = Canevas.coords(Carre[colision[1] - 1])
                    [xmin3, ymin3] = Canevas.coords(Carre[colision[2] - 1])

                    if colision[0]-1 == n :
                        if ymin2 > ymin3 :
                            listeColision[n].append(colision[1]-1)
                            Canevas.coords(Carre[colision[1]-1], xmin1, ymin1 + H - 6)
                        if ymin3 > ymin2:
                            listeColision[n].append(colision[2]-1)
                            Canevas.coords(Carre[colision[2]-1], xmin1, ymin1 + H - 6)

                    if colision[1]-1 == n :
                        if ymin1 > ymin3 :
                            listeColision[n].append(colision[0]-1)
                            Canevas.coords(Carre[colision[0]-1], xmin2, ymin2 + H - 6)
                        if ymin3 > ymin1:
                            listeColision[n].append(colision[2]-1)
                            Canevas.coords(Carre[colision[2]-1], xmin2, ymin2 + H - 6)

                    if colision[2]-1 == n :
                        if ymin1 > ymin2 :
                            listeColision[n].append(colision[0]-1)
                            Canevas.coords(Carre[colision[0]-1], xmin3, ymin3 + H - 6)
                        if ymin2 > ymin1 :
                            listeColision[n].append(colision[1]-1)
                            Canevas.coords(Carre[colision[1]-1], xmin3, ymin3 + H - 6)


                # Colision de 2 blocs
                if len(colision) == 2 :
                    [xmin1, ymin1] = Canevas.coords(Carre[colision[0] - 1])
                    [xmin, ymin] = Canevas.coords(Carre[colision[1] - 1])

                    if colision[0]-1 == n and ymin1 < ymin :
                        listeColision[n].append(colision[1]-1)
                        Canevas.coords(Carre[colision[1]-1], xmin1, ymin1 + H - 6)

                    if colision[1]-1 == n and ymin1 > ymin:
                        listeColision[n].append(colision[0]-1)
                        Canevas.coords(Carre[colision[0]-1], xmin, ymin + H - 6)


                # On fusionne chaque liste
            for i in range(0, nbCarreActuel) :
                for n in range(0, nbCarreActuel) :
                    suivant = listeColision[n][-1]
                    if listeColision[n][0] != suivant :
                        del listeColision[n][-1]
                        listeColision[n] = listeColision[n] + listeColision[suivant]


                # Mise en memoire
            ordre = list(listeColision)
        print("le thread s'est termine proprement")
        Mafenetre.destroy()

    def stop(self):
        self.running = False


def ClicD(event):
    """ Gestion de l'événement Clic droit """


    # position du pointeur de la souris
    X = event.x
    Y = event.y

    for n in range(1,nbCarre) :
        [xmin,ymin] = Canevas.coords(Carre[n])
        xmax = xmin + L
        ymax = ymin + H
        if xmin <= X <= xmax and ymin <= Y <= ymax :
            for i in range(0, len(ordre[n])):
                Canevas.coords(ordre[n][i] + 1, -500, -500)

def ClicG(event):
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    for n in range(0,nbCarre) :
        [xmin,ymin] = Canevas.coords(Carre[n])

        xmax = xmin + L
        ymax = ymin + H
        if xmin<=X<=xmax and ymin<=Y<=ymax:
            DETECTION_CLIC_SUR_OBJET[n] = True
        else: DETECTION_CLIC_SUR_OBJET[n] = False

def Drag(event):
    """ Gestion de l'événement bouton gauche enfoncé """
    X = event.x
    Y = event.y

    for n in range(0, nbCarre):
        if DETECTION_CLIC_SUR_OBJET[n] == True:
            # limite de l'objet dans la zone graphique
            if X<0: X=0
            if X>Largeur: X=Largeur
            if Y<0: Y=0
            if Y>Hauteur: Y=Hauteur

            # mise à jour de la position de l'objet (drag)
            for i in range (0, len(ordre[n])) :
                Canevas.coords(ordre[n][i]+1, X - L / 2, Y - H / 2 + i*H - 6*i)




"""-------- CREATION DES FONCTION POUR LE 'EXECUTION DU PROGRAMME --------"""
def Save(executer):
    global f
    global tab
    global time
    global random

    f = open("monFichierPatricK.py", "w+")
    o = ordre[0]
    tab = 0
    time = False
    random = False
    for i in o:
        for b in Blocs:
            if b.getGenId() == i:
                Write(b)
    f.close()
    if executer == True :
        path = os.path.realpath("monFichierPatricK.py")
        os.system("python "+ path)

def Write(b):
    global tab
    global time
    global random
    global f

    if b.id == 1:
        f.write("\n" + tab * "\t" + "print("+b.getEntry()+")")
    if b.id == 2:
        f.write("\n" + tab * "\t" + "if "+b.getEntry()+":")
        tab = tab + 1
    if b.id == 3:
        f.write("\n" + tab * "\t" + "else :")
        tab = tab + 1
    if b.id == 4:
        f.write("\n" + tab * "\t" + "while "+b.getEntry()+":")
        tab = tab + 1
    if b.id == 6:
        f.write("\n" + tab * "\t" + "for z in range (0,"+b.getEntry()+") :")
        tab = tab + 1
    if b.id == 9:
        if time == True:
            f.write("\n" + tab * "\t" + "time.sleep(" + b.getEntry() + ")")
        if time == False :
            f.write("\n" + tab * "\t" + "import time" + "\n" + tab * "\t" + "time.sleep("+b.getEntry()+")")
            time = True
    if b.id == 10:
        if b.getEntry2() == b.getEntry3() == '':
            Range = "-10**99, 10**99"
        else:
            Range = str("int(" + b.getEntry2() + ")") + ", " + str("int(" + b.getEntry3() + ")")
        if random == True:
            f.write("\n" + tab * "\t" + b.getEntry1() + " = " + 'random.random(' + Range + ')')
        if random == False:
            f.write("\n" + tab * "\t" + "import random" + "\n" + tab * "\t" + b.getEntry1() + " = " + 'random.randint(' + Range + ')')
            random = True
    if b.id == 7:
        f.write("\n" + tab * "\t" + b.getEntry())
    if b.id == 11:
        f.write("\n" + tab * "\t" + b.getEntry() + ' = input("' + b.getEntry() + ' : ")' )

    elif b.id == 5:
        tab = tab - 1




"""-------- CREATION DES FONCTION POUR LES BOUTONS --------"""
def takeUserInput():
    for n in range(0, nbCarre):
        if DETECTION_CLIC_SUR_OBJET[n] == True and Blocs[n].id != 3 and Blocs[n].id != 5 and Blocs[n].id != 8 and Blocs[n].id != 10:
            if Blocs[n].entry == '':
                userInput = simpledialog.askstring("Ajouter une valeur", Blocs[n].display)
                if userInput == None : userInput = ''
                Blocs[n].entry = userInput
            elif Blocs[n].entry != '' :
                userInput = simpledialog.askstring("Changer la valeur", "Valeur actuelle : " + Blocs[n].entry + " " + Blocs[n].display)
                if userInput == None: userInput = Blocs[n].entry
                Blocs[n].entry = userInput
        if DETECTION_CLIC_SUR_OBJET[n] == True and Blocs[n].id == 10 :
            if Blocs[n].entry1 == '':
                userInput1 = simpledialog.askstring("Ajouter une valeur", "Variable a renseigner:")
            elif Blocs[n].entry1 != '':
                userInput1 = simpledialog.askstring("Changer la valeur", "Valeur actuelle : " + Blocs[n].entry1 + "," + "\n" + " Nouvelle variable a renseigner :")

            if Blocs[n].entry2 == '':
                userInput2 = simpledialog.askstring("Ajouter une valeur", "Borne inférieure :")
            elif Blocs[n].entry2 != '':
                userInput2 = simpledialog.askstring("Changer la valeur", "Valeur actuelle : " + Blocs[n].entry2 + "," + "\n" + "Nouvelle borne inférieure :")

            if Blocs[n].entry3 == '':
                userInput3 = simpledialog.askstring("Ajouter une valeur", "Borne supérieure :")
            elif Blocs[n].entry3 != '':
                userInput3 = simpledialog.askstring("Changer la valeur", "Valeur actuelle : " + Blocs[n].entry3 + "," + "\n" + " Nouvelle borne supérieure :")

            if userInput1 == None: userInput1 = ''
            if userInput2 == None: userInput2 = ''
            if userInput3 == None: userInput3 = ''
            Blocs[n].entry1 = userInput1
            Blocs[n].entry2 = userInput2
            Blocs[n].entry3 = userInput3

def creationBloc(type):
    global nbCarre
    global genId
    genId += 1
    Carre.append(type.new())
    Blocs.append(type)
    DETECTION_CLIC_SUR_OBJET.append(False)
    nbCarre = len(Carre)




"""-------- CODE PRINCIPAL --------"""
# Creation des variables
f = open("monFichierPatricK.py", "w+")
tab = 0
genId = 0
listeColision = list()
nbCarre = 1
Carre = list()
Blocs = list()
DETECTION_CLIC_SUR_OBJET = list()


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Projet PatricK")


# Création d'un widget Canvas
Largeur = 800
Hauteur = 800
Canevas = Canvas(Mafenetre,width=Largeur,height=Hauteur,bg ='white')


# Taille des blocs
L = 200
H = 70


# ouverture des images
imgDeb = ImageTk.PhotoImage(file ='images/bloc-debut.png')
imgVide = ImageTk.PhotoImage(file ='images/bloc-vide.png')
imgPrint = ImageTk.PhotoImage(file ='images/bloc-print.png')
imgIf = ImageTk.PhotoImage(file ='images/bloc-if.png')
imgElse = ImageTk.PhotoImage(file ='images/bloc-else.png')
imgEndOfLoop = ImageTk.PhotoImage(file ='images/bloc-endOfLoop.png')
imgFor = ImageTk.PhotoImage(file ='images/bloc-for.png')
imgWhile = ImageTk.PhotoImage(file ='images/bloc-while.png')
imgVar = ImageTk.PhotoImage(file ='images/bloc-variable.png')
imgDelay = ImageTk.PhotoImage(file ='images/bloc-delay.png')
imgRandom = ImageTk.PhotoImage(file ='images/bloc-random.png')
imgInput = ImageTk.PhotoImage(file ='images/bloc-input.png')


# Creation du menu
menubar = Menu(Mafenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label='Exécuter', command=lambda: Save(True))
menu1.add_command(label='Sauvegarder', command=lambda: Save(False))
menubar.add_cascade(label="Actions", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Afficher", command=lambda: creationBloc(Print()))
menu2.add_separator()
menu2.add_command(label="Si", command=lambda: creationBloc(If()))
menu2.add_command(label="Sinon", command=lambda: creationBloc(Else()))
menu2.add_command(label='Fin de boucle', command=lambda: creationBloc(endOfLoop()))
menu2.add_command(label='Répéter', command=lambda: creationBloc(For()))
menu2.add_command(label='Tant que', command=lambda: creationBloc(While()))
menu2.add_separator()
menu2.add_command(label='Saisir', command=lambda: creationBloc(Input()))
menu2.add_command(label='Variable', command=lambda: creationBloc(Variable()))
menu2.add_command(label='Nombre aléatoire', command=lambda: creationBloc(Random()))
menu2.add_separator()
menu2.add_command(label='Attendre', command=lambda: creationBloc(Delay()))
menubar.add_cascade(label="Blocs", menu=menu2)

menubar.add_command(label = "Ajouter une valeur", command = takeUserInput)

menubar.add_command(label = "quitter", command =lambda: thColision.stop())

Mafenetre.config(menu=menubar)


# Creation du bloc de demarrage
creationBloc(Debut())


# Creation des evenements
Canevas.bind('<Button-1>',ClicG) # évévement clic gauche (press)
Canevas.bind('<Button-3>',ClicD) # évévement clic gauche (press)
Canevas.bind('<B1-Motion>',Drag) # événement bouton gauche enfoncé (hold down)


# Demarrage du thread de colision
thColision = Colision()
thColision.start()


Canevas.focus_set()
Canevas.pack(padx=10,pady=10)


Mafenetre.mainloop()


