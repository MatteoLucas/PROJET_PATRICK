from tkinter import *
import threading




def Colision():
    global ordre
    while 1:
        listeColision = []
        for n in range(0, nbCarre) :
            listeColision.append(list())
            listeColision[n].append(n)


        for n in range(0, nbCarre) :
            colision = Canevas.find_overlapping(Canevas.coords(Carre[n])[0], Canevas.coords(Carre[n])[1], Canevas.coords(Carre[n])[2], Canevas.coords(Carre[n])[3])
            if len(colision) == 3 :
                if colision[0]-1 == n :
                    [xmin1, ymin1, xmax1, ymax1] = Canevas.coords(Carre[colision[1] - 1])
                    [xmin2, ymin2, xmax2, ymax2] = Canevas.coords(Carre[colision[2] - 1])
                    [xmin, ymin, xmax, ymax] = Canevas.coords(Carre[colision[0] - 1])
                    if ymin1 > ymin2 :
                        listeColision[n].append(colision[1]-1)
                        Canevas.coords(Carre[colision[1]-1], xmin, ymax - 6, xmax, ymax + 2 * TailleCarre - 6)
                    if ymin2 > ymin1:
                        listeColision[n].append(colision[2]-1)
                        Canevas.coords(Carre[colision[2] - 1], xmin, ymax - 6, xmax, ymax + 2 * TailleCarre - 6)
                if colision[1]-1 == n :
                    [xmin1, ymin1, xmax1, ymax1] = Canevas.coords(Carre[colision[0] - 1])
                    [xmin2, ymin2, xmax2, ymax2] = Canevas.coords(Carre[colision[2] - 1])
                    [xmin, ymin, xmax, ymax] = Canevas.coords(Carre[colision[1] - 1])
                    if ymin1 > ymin2 :
                        listeColision[n].append(colision[0]-1)
                        Canevas.coords(Carre[colision[0] - 1], xmin, ymax - 6, xmax, ymax + 2 * TailleCarre - 6)
                    if ymin2 > ymin1:
                        listeColision[n].append(colision[2]-1)
                        Canevas.coords(Carre[colision[2] - 1], xmin, ymax - 6, xmax, ymax + 2 * TailleCarre - 6)
                if colision[2]-1 == n :
                    [xmin1, ymin1, xmax1, ymax1] = Canevas.coords(Carre[colision[0]-1])
                    [xmin2, ymin2, xmax2, ymax2] = Canevas.coords(Carre[colision[1]-1])
                    [xmin, ymin, xmax, ymax] = Canevas.coords(Carre[colision[2]-1])
                    if ymin1 > ymin2 :
                        listeColision[n].append(colision[0]-1)
                        Canevas.coords(Carre[colision[0] - 1], xmin, ymax - 6, xmax, ymax + 2 * TailleCarre - 6)
                    if ymin2 > ymin1 :
                        listeColision[n].append(colision[1]-1)
                        Canevas.coords(Carre[colision[1] - 1], xmin, ymax - 6, xmax, ymax + 2 * TailleCarre - 6)
            if len(colision) == 2 :
                if colision[0]-1 == n :
                    [xmin1, ymin1, xmax1, ymax1] = Canevas.coords(Carre[colision[1] - 1])
                    [xmin, ymin, xmax, ymax] = Canevas.coords(Carre[colision[0] - 1])
                    if ymin1 > ymin :
                        listeColision[n].append(colision[1]-1)
                        Canevas.coords(Carre[colision[1] - 1], xmin, ymax - 6, xmax, ymax + 2 * TailleCarre - 6)
                if colision[1]-1 == n :
                    [xmin1, ymin1, xmax1, ymax1] = Canevas.coords(Carre[colision[0] - 1])
                    [xmin, ymin, xmax, ymax] = Canevas.coords(Carre[colision[1] - 1])
                    if ymin1 > ymin :
                        listeColision[n].append(colision[0]-1)
                        Canevas.coords(Carre[colision[0] - 1], xmin, ymax - 6, xmax, ymax + 2 * TailleCarre - 6)

            # On fusionne chaque liste
        for i in range(0, nbCarre) :
            for n in range(0, nbCarre) :
                suivant = listeColision[n][-1]
                if listeColision[n][0] != suivant :
                    del listeColision[n][-1]
                    listeColision[n] = listeColision[n] + listeColision[suivant]

            # Mise en memoire
        ordre = list(listeColision)






def Clic(event):
    """ Gestion de l'événement Clic gauche """


    # position du pointeur de la souris
    X = event.x
    Y = event.y

    for n in range(0,nbCarre) :
        global premierCarre
        [xmin,ymin,xmax,ymax] = Canevas.coords(Carre[n])

        if xmin<=X<=xmax and ymin<=Y<=ymax:
            DETECTION_CLIC_SUR_OBJET[n] = True
            premierCarre = n
        else: DETECTION_CLIC_SUR_OBJET[n] = False




def Drag(event):
    """ Gestion de l'événement bouton gauche enfoncé """
    X = event.x
    Y = event.y
    n = 0
    i = 0
    for n in range (0,nbCarre) :
        if DETECTION_CLIC_SUR_OBJET[n] == True:
            # limite de l'objet dans la zone graphique
            if X<0: X=0
            if X>Largeur: X=Largeur
            if Y<0: Y=0
            if Y>Hauteur: Y=Hauteur

            Xmin = X-TailleCarre
            Ymin = Y-TailleCarre
            Xmax = X+TailleCarre
            Ymax = Y+TailleCarre

            # mise à jour de la position de l'objet (drag)
            for i in range (0, len(ordre[n])) :
                Canevas.coords(Carre[ordre[n][i]],Xmin,Ymin + i*2*TailleCarre-i*6,Xmax,Ymax + i*2*TailleCarre-i*6)




premierCarre = 0
listeColision = list()

nbCarre = 10
Carre = list()
DETECTION_CLIC_SUR_OBJET = list()
for n in range (0,nbCarre) :
    DETECTION_CLIC_SUR_OBJET.append(False)


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Projet PatricK")


# Création d'un widget Canvas
Largeur = 500
Hauteur = 500
TailleCarre = 20
Canevas = Canvas(Mafenetre,width=Largeur,height=Hauteur,bg ='white')


# Création des objets graphiques
Carre.append(Canevas.create_rectangle(0,0,TailleCarre*2,TailleCarre*2,fill='green'))
for n in range (1,nbCarre) :
    Carre.append(Canevas.create_rectangle(n*(TailleCarre*2+10),0,n*(TailleCarre*2+10)+TailleCarre*2,TailleCarre*2,fill='maroon'))


# La méthode bind() permet de lier un événement avec une fonction
Canevas.bind('<Button-1>',Clic) # évévement clic gauche (press)
Canevas.bind('<B1-Motion>',Drag) # événement bouton gauche enfoncé (hold down)


# Demarrage du thread de colision

thColision = threading.Thread(target=Colision)
thColision.start()


Canevas.focus_set()
Canevas.pack(padx=10,pady=10)

Mafenetre.mainloop()