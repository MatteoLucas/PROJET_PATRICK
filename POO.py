from tkinter import *
import threading
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

    for n in range (0,nbCarre) :
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
    print(Blocs)

def Afficher():
    global nbCarre
    C = Print()
    Carre.append(C.new())
    Blocs.append(C)
    DETECTION_CLIC_SUR_OBJET.append(False)
    nbCarre = len(Carre)


def Vide():
    global nbCarre
    Carre.append(Canevas.create_image(0, 0, anchor=NW, image=image2))
    DETECTION_CLIC_SUR_OBJET.append(False)
    nbCarre = len(Carre)
    Convertion[len(Convertion)+1] = 'Violet'




#Création des classe:
class Print:
    id = 1
    toPrint = ""
    def new(self):
        print("nouveau bloc print")
        c1 = Canvas(Canevas, width=L, height=H, bg='white')
        e1 = Entry(Canevas)
        c1.create_image(0, 0, anchor=NW, image=image3)
        c1.create_window(30, 30, anchor=NW,window=e1)
        # La méthode bind() permet de lier un événement avec une fonction
        c1.bind('<Button-1>', ClicG)  # évévement clic gauche (press)
        c1.bind('<Button-3>', ClicD)  # évévement clic gauche (press)
        c1.bind('<B1-Motion>', Drag)  # événement bouton gauche enfoncé (hold down)
        return Canevas.create_window(2, 2, anchor=NW, window=c1)
        c1.focus_set()
        c1.pack(padx=10, pady=10)


class If:
    id = 2

    def new(self):
        Carre.append(Canevas.create_image(0, 0, anchor=NW, image=image))

class Else:
    id = 3

    def new(self):
        Carre.append(Canevas.create_image(0, 0, anchor=NW, image=image2))

class While:
    id = 4

    def new(self):
        Carre.append(Canevas.create_image(0, 0, anchor=NW, image=image3))

class For:
    id = 5

class Variable:
    id = 6
    nom = "a définir"
    value = "a définir"




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

Afficher = Button(Mafenetre, text ='Afficher', command = Afficher)
Afficher.pack(side = LEFT, padx = 10, pady = 10)

Vide = Button(Mafenetre, text ='Vide', command = Vide)
Vide.pack(side = LEFT, padx = 10, pady = 10)


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