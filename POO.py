from tkinter import *
import threading
from tkinter import Entry

from PIL import ImageTk




def Colision():
    global ordre
    while 1:

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



def ClicD(event):
    """ Gestion de l'événement Clic droit """


    # position du pointeur de la souris
    X = event.x
    Y = event.y

    for n in range(0,nbCarre) :
        [xmin,ymin] = Canevas.coords(Carre[n])
        xmax = xmin + L
        ymax = ymin + H
        if xmin <= X <= xmax and ymin <= Y <= ymax:
            for i in range(0, len(ordre[n])):
                Canevas.coords(ordre[n][i] + 1, -500, -500)

def ClicG(event):
    """ Gestion de l'événement Clic gauche """
    '''Probleme : Quand on clique sur c1 event.x et event.y on les valeurs pour c1 et non pour Canevas'''
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    print(X,Y)
    for n in range(0,nbCarre) :
        [xmin,ymin] = Canevas.coords(Carre[n])

        xmax = xmin + L
        ymax = ymin + H
        if xmin<=X<=xmax and ymin<=Y<=ymax:
            DETECTION_CLIC_SUR_OBJET[n] = True
        else: DETECTION_CLIC_SUR_OBJET[n] = False

    print(DETECTION_CLIC_SUR_OBJET)

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


def Executer():
    print('Execution')
    global f
    f = open("monFichierScratch.py", "w+")
    o = ordre[0]
    for i in o:
        for b in Blocs:
            if b.getGenId() == i:
                Write(b)

f = open("monFichierScratch.py", "w+")
tab = 0
def Write(b):
    global tab
    global f
    if b.id == 1:
        f.write("\n" + tab * "\t" + "print('"+b.getEntry()+"')")
    if b.id == 2:
        f.write("\n" + tab * "\t" + "if "+b.getEntry()+":")
        tab = tab + 1
    if b.id == 3:
        f.write("\n" + tab * "\t" + "else "+b.getEntry()+":")
        tab = tab + 1
    if b.id == 4:
        f.write("\n" + tab * "\t" + "while "+b.getEntry()+":")
        tab = tab + 1
    if b.id == 6:
        f.write("\n" + tab * "\t" + "for "+b.getEntry()+":")
        tab = tab + 1
    if b.id == 7:
        f.write("\n" + tab * "\t" + b.getEntry())
    elif b.id == 5:
        tab = tab - 1
        '''
        if 'if' in toWrite or 'else' in toWrite or 'for' in toWrite or 'while' in toWrite or 'elif' in toWrite:
            f.write("\n" + tab * "\t" + toWrite)
            tab = tab + 1
        elif 'endOfLoop' == toWrite:
            tab = tab - 1
        elif tab > 0:
            f.write("\n" + tab * "\t" + toWrite)
        else:
            f.write("\n" + toWrite)'''

    #f.close()
def Save():
    global f
    f.close()

def blocPrint():
    global nbCarre
    global genId
    genId += 1
    C = Print()
    Carre.append(C.new())
    Blocs.append(C)
    DETECTION_CLIC_SUR_OBJET.append(False)
    nbCarre = len(Carre)

def blocIf():
    global nbCarre
    global genId
    genId += 1
    C = If()
    Carre.append(C.new())
    Blocs.append(C)
    DETECTION_CLIC_SUR_OBJET.append(False)
    nbCarre = len(Carre)

def blocVar():
    global nbCarre
    global genId
    genId += 1
    C = Variable()
    Carre.append(C.new())
    Blocs.append(C)
    DETECTION_CLIC_SUR_OBJET.append(False)
    nbCarre = len(Carre)

def blocElse():
    global nbCarre
    global genId
    genId += 1
    C = Else()
    Carre.append(C.new())
    Blocs.append(C)
    DETECTION_CLIC_SUR_OBJET.append(False)
    nbCarre = len(Carre)


def blocEndOfLoop():
    global nbCarre
    global genId
    genId += 1
    C = endOfLoop()
    Carre.append(C.new())
    Blocs.append(C)
    DETECTION_CLIC_SUR_OBJET.append(False)
    nbCarre = len(Carre)
    Convertion[len(Convertion) + 1] = 'enfOfLoop'


genId = 0

#Création des classe:
class Print:
    id = 1
    bId = 0
    def __init__(self):
        self.c1 = Canvas(Canevas, width=L, height=H, bg='white')
        self.e1 = Entry(Canevas)
        self.bId = genId


    def new(self):
        print("nouveau bloc print")
        self.c1.create_image(0, 0, anchor=NW, image=image3)
        self.c1.create_window(30, 30, anchor=NW, window=self.e1)
        # La méthode bind() permet de lier un événement avec une fonction
        self.c1.bind('<Button-1>', ClicG)  # évévement clic gauche (press)
        self.c1.bind('<Button-3>', ClicD)  # évévement clic gauche (press)
        self.c1.bind('<B1-Motion>', Drag)  # événement bouton gauche enfoncé (hold down)
        return Canevas.create_window(2, 2, anchor=NW, window=self.c1)
        self.c1.focus_set()
        self.c1.pack(padx=10, pady=10)

    def getEntry(self):
        #print(self.e1.get())
        return self.e1.get()
    def getGenId(self):
        return self.bId

class endOfLoop:
    id = 5
    def __init__(self):
        print(genId)
        self.bId = genId
    def new(self):
        return Canevas.create_image(0, 0, anchor=NW, image=image6)
    def getGenId(self):
        return self.bId


class If:
    id = 2
    def __init__(self):
        print(genId)
        self.c1 = Canvas(Canevas, width=L, height=H, bg='white')
        self.e1 = Entry(Canevas)
        self.bId = genId

    def new(self):
        print("nouveau bloc if")
        self.c1.create_image(0, 0, anchor=NW, image=image4)
        self.c1.create_window(30, 30, anchor=NW, window=self.e1)
        # La méthode bind() permet de lier un événement avec une fonction
        self.c1.bind('<Button-1>', ClicG)  # évévement clic gauche (press)
        self.c1.bind('<Button-3>', ClicD)  # évévement clic gauche (press)
        self.c1.bind('<B1-Motion>', Drag)  # événement bouton gauche enfoncé (hold down)
        return Canevas.create_window(2, 2, anchor=NW, window=self.c1)
        self.c1.focus_set()
        self.c1.pack(padx=10, pady=10)

    def getEntry(self):
        return self.e1.get()
    def getGenId(self):
        return self.bId

class Else:
    id = 3
    def __init__(self):
        print(genId)
        self.c1 = Canvas(Canevas, width=L, height=H, bg='white')
        self.e1 = Entry(Canevas)
        self.bId = genId

    def new(self):
        print("nouveau bloc if")
        self.c1.create_image(0, 0, anchor=NW, image=image5)
        self.c1.create_window(30, 30, anchor=NW, window=self.e1)
        # La méthode bind() permet de lier un événement avec une fonction
        self.c1.bind('<Button-1>', ClicG)  # évévement clic gauche (press)
        self.c1.bind('<Button-3>', ClicD)  # évévement clic gauche (press)
        self.c1.bind('<B1-Motion>', Drag)  # événement bouton gauche enfoncé (hold down)
        return Canevas.create_window(2, 2, anchor=NW, window=self.c1)
        self.c1.focus_set()
        self.c1.pack(padx=10, pady=10)

    def getEntry(self):
        return self.e1.get()
    def getGenId(self):
        return self.bId

class While:
    id = 4
    def __init__(self):
        print(genId)
        self.c1 = Canvas(Canevas, width=L, height=H, bg='white')
        self.e1 = Entry(Canevas)
        self.bId = genId

    def new(self):
        print("nouveau bloc if")
        self.c1.create_image(0, 0, anchor=NW, image=image2)
        self.c1.create_window(30, 30, anchor=NW, window=self.e1)
        # La méthode bind() permet de lier un événement avec une fonction
        self.c1.bind('<Button-1>', ClicG)  # évévement clic gauche (press)
        self.c1.bind('<Button-3>', ClicD)  # évévement clic gauche (press)
        self.c1.bind('<B1-Motion>', Drag)  # événement bouton gauche enfoncé (hold down)
        return Canevas.create_window(2, 2, anchor=NW, window=self.c1)
        self.c1.focus_set()
        self.c1.pack(padx=10, pady=10)

    def getEntry(self):
        return self.e1.get()
    def getGenId(self):
        return self.bId

class For:
    id = 6
    def __init__(self):
        print(genId)
        self.c1 = Canvas(Canevas, width=L, height=H, bg='white')
        self.e1 = Entry(Canevas)
        self.bId = genId

    def new(self):
        print("nouveau bloc if")
        self.c1.create_image(0, 0, anchor=NW, image=image2)
        self.c1.create_window(30, 30, anchor=NW, window=self.e1)
        # La méthode bind() permet de lier un événement avec une fonction
        self.c1.bind('<Button-1>', ClicG)  # évévement clic gauche (press)
        self.c1.bind('<Button-3>', ClicD)  # évévement clic gauche (press)
        self.c1.bind('<B1-Motion>', Drag)  # événement bouton gauche enfoncé (hold down)
        return Canevas.create_window(2, 2, anchor=NW, window=self.c1)
        self.c1.focus_set()
        self.c1.pack(padx=10, pady=10)

    def getEntry(self):
        return self.e1.get()
    def getGenId(self):
        return self.bId


class Variable:
    id = 7

    def __init__(self):
        print(genId)
        self.c1 = Canvas(Canevas, width=L, height=H, bg='white')
        self.e1 = Entry(Canevas)
        self.bId = genId

    def new(self):
        print("nouveau bloc if")
        self.c1.create_image(0, 0, anchor=NW, image=image2)
        self.c1.create_window(30, 30, anchor=NW, window=self.e1)
        # La méthode bind() permet de lier un événement avec une fonction
        self.c1.bind('<Button-1>', ClicG)  # évévement clic gauche (press)
        self.c1.bind('<Button-3>', ClicD)  # évévement clic gauche (press)
        self.c1.bind('<B1-Motion>', Drag)  # événement bouton gauche enfoncé (hold down)
        return Canevas.create_window(2, 2, anchor=NW, window=self.c1)
        self.c1.focus_set()
        self.c1.pack(padx=10, pady=10)

    def getEntry(self):
        return self.e1.get()

    def getGenId(self):
        return self.bId

listeColision = list()
nbCarre = 1
Carre = list()
Blocs = list()
DETECTION_CLIC_SUR_OBJET = list()



# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Projet PatricK")


# Creation des boutons
Executer = Button(Mafenetre, text ='Exécuter', command = Executer)
Executer.pack(side = LEFT, padx = 10, pady = 10)

Afficher = Button(Mafenetre, text ='Print', command = blocPrint)
Afficher.pack(side = LEFT, padx = 10, pady = 10)

Vide = Button(Mafenetre, text ='Fin de boucle', command = blocEndOfLoop)
Vide.pack(side = LEFT, padx = 10, pady = 10)

ifBtn = Button(Mafenetre, text ='If', command = blocIf)
ifBtn.pack(side = LEFT, padx = 10, pady = 10)

saveBtn = Button(Mafenetre, text ='Save', command = Save)
saveBtn.pack(side = RIGHT, padx = 10, pady = 10)

varBtn = Button(Mafenetre, text ='Var', command = blocVar)
varBtn.pack(side = LEFT, padx = 10, pady = 10)

elseBtn = Button(Mafenetre, text ='Else', command = blocElse)
elseBtn.pack(side = LEFT, padx = 10, pady = 10)


# Création d'un widget Canvas
Largeur = 800
Hauteur = 800
Canevas = Canvas(Mafenetre,width=Largeur,height=Hauteur,bg ='white')


# Taille des blocs
L = 200
H = 70


# ouverture des images
image = ImageTk.PhotoImage(file ='images/bloc-debut.png')
image2 = ImageTk.PhotoImage(file ='images/bloc-vide.png')
image3 = ImageTk.PhotoImage(file ='images/bloc-print.png')
image4 = ImageTk.PhotoImage(file ='images/bloc-if.png')
image5 = ImageTk.PhotoImage(file ='images/bloc-else.png')
image6 = ImageTk.PhotoImage(file ='images/bloc-endOfLoop.png')


# Creation du bloc de demarrage
Carre.append(Canevas.create_image(600, 600, anchor=NW, image=image))
DETECTION_CLIC_SUR_OBJET.append(False)
Convertion = {1:'Debut'}





# La méthode bind() permet de lier un événement avec une fonction
Canevas.bind('<Button-1>',ClicG) # évévement clic gauche (press)
Canevas.bind('<Button-3>',ClicD) # évévement clic gauche (press)
Canevas.bind('<B1-Motion>',Drag) # événement bouton gauche enfoncé (hold down)


# Demarrage du thread de colision

thColision = threading.Thread(target=Colision)
thColision.start()


Canevas.focus_set()
Canevas.pack(padx=10,pady=10)



Mafenetre.mainloop()