[xmin, ymin, xmax, ymax] = Canevas.coords(Carre[listeColision[0]])
        for n in range(0, len(listeColision)):
            Canevas.coords(Carre[listeColision[n]], xmin, ymin + n * 2 * TailleCarre - n * 6, xmax,ymax + n * 2 * TailleCarre - n * 6)


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
