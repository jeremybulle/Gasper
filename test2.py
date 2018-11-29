# -*-coding:utf-8 -*

"""ce programme est un jeu, où l'utilisateur déplace un fantôme appelé Gasper.
Le but du jeu est de rejoindre le paradis en traversant le chateau tout en évitant
les monstres. Gasper doit toujours avoir au moins une pinte dans son inventaire,
si ce n'est pas la cas, c'est Game Over."""

#importation des modules
import sys
import os
import random

def restart_program():
    """Relance le programme en cours"""
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Fonctions liées à la construction du chateau

def menu(grille):
    """affichage de l'interface avec l'utilisateur"""
    afficher(grille)
    print ("Gasper possède {0} pinte(s)".format(Gasper["pinte"]))
    print ( "6- Droite")
    print ( "4- Gauche")
    print ( "8- Haut")
    print ( "2- Bas")
    print ( "0- Sortir")
    try :
        answer=int(input())
        return answer
    except SyntaxError: # si l'utilisatuer appuie sur la touche entrée sans ajouter de valeur
        pass
    except NameError : # si l'utilisateur entre une str au lieu d'un int
        pass

def BuildCastle(n):
    """ Construction des éléments du chateau """
    if n==2:
        grille=[[" "," "," "," "," "," "," "," "," "," ","R"," "," "],[0,"*","*","*","*","*",0,"*","*"," ","*"," "," "],
        ["*"," "," "," ","*"," "," "," ",0,"*","*"," "," "],["*","*",0,"*","*","*",0," "," "," ","*"," "," "],
        [0," ","*"," "," "," ","*"," "," "," ",0," "," "],["*"," ","P"," "," "," ","*"," "," "," ","*"," "," "],
        ["*"," ","*"," "," "," ",0,"*","*","*","*"," "," "],["*"," ","*"," "," "," ","*"," "," "," ","*"," "," "],
        [0,"*","*","*",0,"*","*","*","*","*",0," "," "]]
        return grille
    elif n==1:
        grille=[[" "," ","*","*","*","*","*"," "," "," ","E"," "," "],[" "," ","*"," "," "," ","*"," "," "," ","*"," "," "],
        [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
        [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
        [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],[" "," ","*"," "," "," ","*"," "," "," "," "," "," "],
        [" "," ","*","*","R","*","*"," "," "," "," "," "," "]]
        return grille


def Salle(n):
    if n==2:
        salle=[[8,0],[4,0],[1,0],[2,8],[3,2],[1,3],[8,4],[6,6],[3,6],[1,6],[8,10],[4,10]]
        return salle
    elif n==1:
        salle=[[2,0],[4,0],[6,0],[2,4],[4,4],[6,4],[2,8],[4,8],[6,8],[2,12],[4,12],[6,12]]
        return salle
    
def choix_monstre(n):
    if n==1:
        choix=[Master,Fou,Bibbendum1,Bibbendum2,Bibbendum3]
        return choix
    if n==2:
        choix=[Master,Fou,Bibbendum1]
        return choix
        
def afficher(grille):
    """Affichage du chateau sur le terminal"""
    size=len(grille)
    for i in range(size):
        for j in grille[i]:
            print j,
        print " "

#Fonctions liées à la position de Gasper

def position(i,j,grille):
    """ Position de Gasper et conditions de fin de jeu """
    global Plateau
    global Index_room
    global n
    value=grille[i][j]
    Gasper["abs"]=j
    Gasper["ord"]=i
    # Si la valeur temporaire correpond à la valeur du Paradis le fantôme gagne
    if value=="P":
        print "You win !!"
        print "Appuyez une touche pour fermer le programme"
        print "1. fermer le programme"
        print "2. relancer une partie"
        flag = input()
        if flag == 1 :
            sys.exit()
        if flag == 2 :
            restart_program()
    elif value=="E":
        print "Veuillez monter dans l'ascenseur"
        level=2
        Plateau=BuildCastle(level)
        Index_room=Salle(level)
        Liste_monstre=choix_monstre(level)
        x=0
        y=10
        value=position(x,y,Plateau)
        Pop_pinte(Pintes)
        Pop_monstre(Pintes,Liste_monstre,Index_room)
        return value
    # Si Gasper n'a plus de pintes, il perd"
    elif Gasper["pinte"]<0 or Gasper["pinte"]==0:
        print "Gasper ne peut plus se déplacer sans énergie..."
        print "Game Over"
        print "1. fermer le programme"
        print "2. relancer une partie"
        flag = input()
        if flag == 1 :
            sys.exit()
        if flag == 2 :
            os.system("clear")
            restart_program()
    # Sinon Gasper peut continuer son chemin
    else :
        grille[i][j]="&"
        return value

def Limite(i,j,grille):
    """délimite l'espace du terrain de jeu"""
    size=len(grille)
    size1=len(grille[0])
    if i>size-1 :
        return True
    elif j>size1-1:
        return True
    elif i==-1:
        return True
    elif j==-1:
        return True
    elif grille[i][j]==" ":
        return True

def droite(i,j,prev,grille):
    """ déplace Gasper d'une case vers la droite"""
    grille[i][j]=prev
    if Limite(i,j+1,grille)!=True:
        value=position(i,j+1,grille)
        mv=Trigger(Liste_monstre,Gasper,Pintes)
        if mv==1:
            x1,y1,value1=Retour_recep(level)
            grille[i][j+1]=value
            return x1,y1,value1
        elif mv==0 :
            x1,y1,value1=Fou_depl(Index_room)
            grille[i][j+1]=value
            mv=Trigger(Liste_monstre,Gasper,Pintes)
            return x1,y1,value1
        else :
            return i,j+1,value
    else :
        value=position(i,j,grille)
        print("Mouvement impossible")
        return i,j,value

def gauche(i,j,prev,grille):
    """ déplace Gasper d'une case vers la gauche"""
    grille[i][j]=prev
    if Limite(i,j-1,grille)!=True:
        value=position(i,j-1,grille)
        mv=Trigger(Liste_monstre,Gasper,Pintes)
        if mv==1:
            x1,y1,value1=Retour_recep(level)
            grille[i][j-1]=value
            return x1,y1,value1
        elif mv==0 :
            x1,y1,value1=Fou_depl(Index_room)
            grille[i][j+1]=value
            mv=Trigger(Liste_monstre,Gasper,Pintes)
            return x1,y1,value1
        else :
            return i,j-1,value
    else :
        value=position(i,j,grille)
        print ("Mouvement impossible")
        return i,j,value

def haut(i,j,prev,grille):
    """ déplace Gasper d'une case vers le haut"""
    grille[i][j]=prev
    if Limite(i-1,j,grille)!=True:
        value=position(i-1,j,grille)
        mv=Trigger(Liste_monstre,Gasper,Pintes)
        if mv==1:
            x1,y1,value1=Retour_recep(level)
            grille[i-1][j]=value
            return x1,y1,value1
        elif mv==0 :
            x1,y1,value1=Fou_depl(Index_room)
            mv=Trigger(Liste_monstre,Gasper,Pintes)
            grille[i-1][j]=value
            return x1,y1,value1
        else :
            return i-1,j,value
    else :
        value=position(i,j,grille)
        print ("Mouvement impossible")
        return i,j,value

def bas(i,j,prev,grille):
    """ déplace Gasper d'une case vers le bas"""
    grille[i][j]=prev
    if Limite(i+1,j,grille)!=True:
        value=position(i+1,j,grille)
        mv=Trigger(Liste_monstre,Gasper,Pintes)
        if mv==1:
            x1,y1,value1=Retour_recep(level)
            grille[i+1][j]=value
            return x1,y1,value1
        elif mv==0 :
            x1,y1,value1=Fou_depl(Index_room)
            mv=Trigger(Liste_monstre,Gasper,Pintes)
            grille[i+1][j]=value
            return x1,y1,value1
        else :
            return i+1,j,value
    else :
        value=position(i,j,grille)
        print ("Mouvement impossible")
        return i,j,value

# Fonctions relatives à la positions des ennemis:
def Is_monstre(Ip,x):
    """vérifie s il y a déjà un monstre dans la piece, x étant la valeur envoyée par la fonction random"""
    flag = 0
    for i in Ip : #scan la liste Indice_pop pour voir si l indice aleatoire fournit par la fonction random.randit() n'a pas déjà été attribué à un autre monstre
        if x == i :
            flag = flag + 1 #ajoute 1 a la valeur de flag si le indice existe déjà dans Index_pop
    if flag > 0 :
        return True #indice déjà attribué à un monstre
    else :
        return False #indice pas utilisé pour un autre monstre, il est utilisable pour un nouveau monstre
    
def Pop_pinte(dict_pinte):
    """Créer le nb de Pintes qui apparaissent dans le Château inférieur à 5 pintes dans tous le château """
    Pintet=0 #Nb total de pintes dans le chateau
    Nb=[] #Liste permettant de conserver les combinaisons possibles
    while(Pintet<5): #Nous devons avoir que 5 pintes 
        if Pintet==3:
            x=random.randint(1,2)
            Pintet=Pintet+x
            Nb.append(x)
        elif Pintet==4:
            x=1
            Pintet=Pintet+x
            Nb.append(x)
        else :
            x=random.randint(1,3)
            Pintet=Pintet+x
            Nb.append(x)
    #Créer un dictionnaire correspondant aux salles avec des pintes et leur nombre, on peut avoir jusqu'à 5 salles
    for i in range(len(Nb)):
        dict_pinte[i]={"abs":None,"ord":None,"nb":Nb[i]}

def Pop_monstre(D,lm,Ip):
    """fonction qui attribue les coordonnées à tous les monstres"""
    Ip = [] #reset l indice de pop si on veut faire repop les monstres de maniere aleatoire(sans que l ancien pop influe)
    for M in lm:
        x = random.randint(0,11) # génère un indice aléatoire
        while Is_monstre(Ip,x) == True : #vérifie si l'indice est attribué à un autre monstre , si c est le cas relance random.randit
            x = random.randint(0,11)
        Ip.append(x) # note l'attribution d'indice dans Index_pop
        M["ord"] = Index_room[x][0] # modifie l'abs du monstre grace a l Index_room
        M["abs"] = Index_room[x][1] # modifie l ord du monstre grace a l Index_room
    for k in D.keys(): #Attribution des valeurs de salle aux pintes
        x = random.randint(0,11)
        while Is_monstre(Ip,x) == True :
            x = random.randint(0,11)
        Ip.append(x)
        D[k]["ord"]=Index_room[x][0]
        D[k]["abs"]=Index_room[x][1]

def Is_one_case_range(Monstre,joueur):
    """focntion qui verifie s'il y a un monstre à une case de Gasper"""
    if ((Monstre["ord"] == (joueur["ord"] +1) or Monstre["ord"] == (joueur["ord"] - 1)) and Monstre["abs"] == joueur["abs"]): #monstre une case au dessus ou en dessous
        return True
    elif ((Monstre["abs"] == (joueur["abs"] +1) or Monstre["abs"] == (joueur["abs"] - 1)) and Monstre["ord"] == joueur["ord"]): #monstre uns case à gauche ou à droite
        return True
    else :
        return False

#Maitre du chateau

def Retour_recep (n) :
    """modifie les coordonnées de Gasper ce qui le place à la réception"""
    if n==1:
        x=8
        y=4
    elif n==2:
        x=0
        y=10
    value=position(x,y,Plateau)
    return x,y,value

#Savant fou :

def Fou_take_pinte(joueur):
    """Le Fou vole 1 pinte à Gasper, modifie la nombre de pinte que possède joueur"""
    joueur["pinte"] = joueur["pinte"] - 1 #modifie la valeur dans le dict Gasper
    print "Gasper perd une pinte d'ectoplasme, il lui reste %d pinte(s) d'energie"%(joueur["pinte"])

def Fou_depl(Index_room):
    """pouvoir du Fou qui modifie de manière aléatoire la position de Gasper"""
    i = random.randint(0,11)
    x = Index_room[i][0]
    y = Index_room[i][1]
    value=position(x,y,Plateau)
    return x,y,value

#Chamallow bibbendum:

def Bib_take_pinte(joueur):
    """Le Bibbendum vole 2 pintes à Gasper, modifie la nombre de pinte que possède Gasper"""
    joueur["pinte"] = joueur["pinte"] - 2
    print "Gasper paralysé perd deux pintes d'ectoplasme, il lui reste %d pinte(s) d'ectoplasme"%(joueur["pinte"])

#Trigger à poser apres chaque deplacement:
def Trigger(lm,joueur,D):
    for Monstre in lm:
        if (Monstre["abs"]==joueur["abs"] and Monstre["ord"]==joueur["ord"]): #Si les positions sont identiques
            if Monstre == Master:
                mv=1
                return mv
            elif Monstre == Fou :
                mv=0
                Fou_take_pinte(joueur)
                return mv
                Trigger(joueur)
            elif (Monstre == Bibbendum1 or Monstre == Bibbendum2 or Monstre == Bibbendum3):
                Bib_take_pinte(joueur)
        elif Is_one_case_range(Monstre,joueur) == True : #Si la position de Gasper -1 de la position des monstres
            if Monstre == Master :
                print("Gasper entend un bruit de clé")
            elif Monstre == Fou :
                print("Gasper entend un rire sardonique")
            elif (Monstre == Bibbendum1 or Monstre == Bibbendum2 or Monstre == Bibbendum3):
                print("Gasper sent une odeur alléchante de chamallow à la fraise")
        else :
            mv=2
    for k in D.keys():
        if (D[k]["abs"]==joueur["abs"] and D[k]["ord"]==joueur["ord"]):
            if D[k]["nb"]==0:
                print "Tu as assez bu pochtron !!"
            else :
                print "Oh de l'ectoplasme vert !! Gasper gagne %d pintes"%(D[k]["nb"])
                joueur["pinte"]=joueur["pinte"]+D[k]["nb"]
                D[k]["nb"]=0

#Main


if __name__ == '__main__':
    
#Intitialisation:

#Plateau de jeu
    level=1
    Index_pop = [] # contient des indices x générés alétoirement => Index_room[x] = coordonnees de la salle dans lequelle il y a le monstre qui a obtenue l'indice X
    Index_room = Salle(level) #liste des salle du chateau Index_room[4,0] = reception , Index_room[10,8]=paradis
    Gasper = {"abs" : 0, "ord" : 0, "pinte" : 3}
    Master = {"abs" : None, "ord" : None}
    Fou = {"abs": None, "ord": None}
    Bibbendum1 = {"abs": None, "ord": None}
    Bibbendum2 = {"abs": None, "ord": None}
    Bibbendum3 = {"abs": None, "ord": None}
    Pintes={}
    Liste_monstre = choix_monstre(level)
    Plateau=[]
    Plateau=BuildCastle(level)
    x=8
    y=4
    value=position(x,y,Plateau)
    Pop_pinte(Pintes)
    Pop_monstre(Pintes,Liste_monstre,Index_pop)
    while True:
        print x,y
        answer=menu(Plateau)
        os.system("clear")
        if answer==6:
            os.system("clear")
            x,y,value=droite(x,y,value,Plateau)
        elif answer==4:
            os.system("clear")
            x,y,value=gauche(x,y,value,Plateau)
        elif answer==8:
            os.system("clear")
            x,y,value=haut(x,y,value,Plateau)
        elif answer==2:
            os.system("clear")
            x,y,value=bas(x,y,value,Plateau)
        elif answer==0:
            sys.exit()
