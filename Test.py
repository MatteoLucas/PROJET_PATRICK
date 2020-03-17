from tkinter import *
import threading




def Colision():
    while 1:
            listeColision = []
            for n in range(0, nbCarre) :
                listeColision.append(0)

            colision = Canevas.find_overlapping(Canevas.coords(Carre[0])[0],Canevas.coords(Carre[0])[1],Canevas.coords(Carre[0])[2],Canevas.coords(Carre[0])[3])
            if len(colision)==2 :
                colle = colision[1]-1
                [xmin,ymin,xmax,ymax] = Canevas.coords(Carre[0])
                Canevas.coords(Carre[colle],xmin,ymax-6,xmax,ymax+2*TailleCarre-6)
                listeColision[1] = colle
            for n in range(1,nbCarre):
                colision = Canevas.find_overlapping(Canevas.coords(Carre[listeColision[n]])[0],Canevas.coords(Carre[listeColision[n]])[1],Canevas.coords(Carre[listeColision[n]])[2],Canevas.coords(Carre[listeColision[n]])[3])
                if len(colision)==3 :
                    if colision[0] != listeColision[n]+1 and colision[0] != listeColision[n-1]+1  : colle = colision[0]-1
                    elif colision[1] != listeColision[n]+1 and colision[1] != listeColision[n-1]+1  : colle = colision[1]-1
                    elif colision[2] != listeColision[n]+1 and colision[2] != listeColision[n-1]+1  : colle = colision[2]-1
                    [xmin,ymin,xmax,ymax] = Canevas.coords(Carre[listeColision[n]])
                    Canevas.coords(Carre[colle],xmin,ymax-6,xmax,ymax+2*TailleCarre-6)
                    listeColision[n+1] = colle



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

    ordre = list()
    X = event.x
    Y = event.y
    n = 0
    i = 0
    premierTrouve = False
    ordre.append(premierCarre)

    for n in range(0, len(listeColision)):
        if listeColision[n] == premierCarre and premierTrouve == False :
            premierTrouve = True
        if listeColision[n] != 0 and listeColision[n] != premierCarre and premierTrouve == True :
            ordre.append(listeColision[n])

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
            for n in range (0, len(ordre)) :
                Canevas.coords(Carre[ordre[n]],Xmin,Ymin + n*2*TailleCarre-n*6,Xmax,Ymax + n*2*TailleCarre-n*6)




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