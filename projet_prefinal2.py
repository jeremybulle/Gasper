# -*-coding:utf-8 -*


"""ce programme est un jeu, où l'utilisateur déplace un fantôme appelé Gasper.
Le but du jeu est de rejoindre le paradis en traversant le chateau tout en évitant
les monstres. Gasper doit toujours avoir au moins une pinte dans son invnetaire,
si ce n'est pas la cas, c'est Game Over."""

#importation des modules
import sys
import os
import random


#Fonctions liées à la construction du chateau

def menu():
    """affichage de l'interface avec l'utilisateur"""
    print ( "1- Gasper entre dans le chateau")
    print ( "2- Droite")
    print ( "3- Gauche")
    print ( "4- Haut")
    print ( "5- Bas")
    print ( "0- Sortir")
    answer=int(input())
    return answer

def BuildCastle():
    """ Construction des éléments du chateau """
    grille=[[" "," ","*","*","*","*","*"," "," "," ",2," "," "],[" "," ","*"," "," "," ","*"," "," "," ","*"," "," "],
    [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
    [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
    [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],[" "," ","*"," "," "," ","*"," "," "," "," "," "," "],
    [" "," ","*","*",1,"*","*"," "," "," "," "," "," "]]
    return grille

def afficher(grille):
    """Affichage du chateau sur le terminal"""
    size=len(grille)
    for i in range(size):
        for j in grille[i]:
            print j,
        print " "

# Pop pinte :

def Pop_pinte(D):
    """Créer le nb de Pintes qui apparaissent dans le Château inférieur à 5 pintes dans tous le château """
    Pintet=0 #Nb total de pintes dans le chateau
    Nb=[] #Liste permettant de conserver les combinaisons possibles
    while(Pintet<5):
        if Pintet==1:
            x=random.randint(1,4)
            Pintet=Pintet+x
            Nb.append(x)
        elif Pintet==2:
            x=random.randint(1,3)
            Pintet=Pintet+x
            Nb.append(x)
        if Pintet==3:
            x=random.randint(1,2)
            Pintet=Pintet+x
            Nb.append(x)
        elif Pintet==4:
            x=1
            Pintet=Pintet+x
            Nb.append(x)
        else :
            x=random.randint(1,5)
            Pintet=Pintet+x
            Nb.append(x)
    #Créer un dictionnaire correspondant aux salles avec des pintes et leur nombre, on peut avoir jusqu'à 5 salles
    for i in range(len(Nb)):
        Pintes[i]={"abs":None,"ord":None,"nb":Nb[i]}


#Fonctions liées à la position de Gasper

def position(i,j,grille):
    """ Position de Gasper et conditions de fin de jeu """
    value=grille[i][j]
    Gasper["abs"]=j
    Gasper["ord"]=i
    # Si la valeur temporaire correpond à la valeur du Paradis le fantôme gagne
    if value==2:
        print "You win !!"
        print "Appuyez une touche pour fermer le programme"
        print "1. fermer le programme"
        print "2. relancer une partie"
        flag = input()
        if flag == 1 :
            exit()
        if flag == 2 :
            None
    # Si Gasper n'a plus de pintes, il perd"
    elif Gasper["pinte"]<0 or Gasper["pinte"]==0:
        print "Game Over"
        print "1. fermer le programme"
        print "2. relancer une partie"
        flag = input()
        if flag == 1 :
            exit()
        if flag == 2 :
            None
    # Sinon Gasper peut continuer son chemin
    else :
        grille[i][j]="&"
        afficher(grille)
        return value

def Limite(x,y,grille):
    """délimite l'espace du terrain de jeu"""
    size=len(grille)
    size1=len(grille[0])
    if x>size-1 :
        return True
    elif y>size1-1:
        return True
    elif x==-1:
        return True
    elif y==-1:
        return True
    elif grille[x][y]==" ":
        return True

def droite(x,y,prev,grille):
    """ déplace Gasper d'une case vers la droite"""
    grille[x][y]=prev
    if Limite(x,y+1,grille)!=True:
        value=position(x,y+1,grille)
        mv=Trigger(x,y,prev,Gasper)
        if mv==1:
            x1,y1,value1=Retour_recep(x,y,Gasper)
            grille[x][y+1]=value
            return x1,y1,value1
        elif mv==0 :
            x1,y1,value1=Fou_depl(x,y,Gasper,Index_room)
            grille[x][y+1]=value
            mv=Trigger(x,y,prev,Gasper)
            return x1,y1,value1
        else :
            return x,y+1,value
    else :
        value=position(x,y,grille)
        print("Mouvement impossible")
        return x,y,value

def gauche(x,y,prev,grille):
    """ déplace Gasper d'une case vers la gauche"""
    grille[x][y]=prev
    if Limite(x,y-1,grille)!=True:
        value=position(x,y-1,grille)
        mv=Trigger(x,y,prev,Gasper)
        if mv==1:
            x1,y1,value1=Retour_recep(x,y,Gasper)
            grille[x][y-1]=value
            return x1,y1,value1
        elif mv==0 :
            x1,y1,value1=Fou_depl(x,y,Gasper,Index_room)
            grille[x][y+1]=value
            mv=Trigger(x,y,prev,Gasper)
            return x1,y1,value1
        else :
            return x,y-1,value
    else :
        value=position(x,y,grille)
        print ("Mouvement impossible")
        return x,y,value


def haut(x,y,prev,grille):
    """ déplace Gasper d'une case vers le haut"""
    grille[x][y]=prev
    if Limite(x-1,y,grille)!=True:
        value=position(x-1,y,grille)
        mv=Trigger(x,y,prev,Gasper)
        if mv==1:
            x1,y1,value1=Retour_recep(x,y,Gasper)
            grille[x-1][y]=value
            return x1,y1,value1
        elif mv==0 :
            x1,y1,value1=Fou_depl(x,y,Gasper,Index_room)
            mv=Trigger(x,y,prev,Gasper)
            grille[x-1][y]=value
            return x1,y1,value1
        else :
            return x-1,y,value
    else :
        value=position(x,y,grille)
        print ("Mouvement impossible")
        return x,y,value

def bas(x,y,prev,grille):
    """ déplace Gasper d'une case vers le bas"""
    grille[x][y]=prev
    if Limite(x+1,y,grille)!=True:
        value=position(x+1,y,grille)
        mv=Trigger(x,y,prev,Gasper)
        if mv==1:
            x1,y1,value1=Retour_recep(x,y,Gasper)
            grille[x+1][y]=value

            return x1,y1,value1
        elif mv==0 :
            x1,y1,value1=Fou_depl(x,y,Gasper,Index_room)
            mv=Trigger(x,y,prev,Gasper)
            grille[x+1][y]=value
            return x1,y1,value1
        else :
            return x+1,y,value
    else :
        value=position(x,y,grille)
        print ("Mouvement impossible")
        return x,y,value

#Trigger à poser apres chaque deplacement:
def Trigger(x,y,prev,Gasper):
    for Monstre in Liste_monstre:
        if (Monstre["abs"]==Gasper["abs"] and Monstre["ord"]==Gasper["ord"]):
            if Monstre == Master:
                mv=1
                return mv
            elif Monstre == Fou :
                mv=0
                Fou_take_pinte(Gasper)
                return mv
                Trigger(Gasper)
            elif (Monstre == Bibbendum1 or Monstre == Bibbendum2 or Monstre == Bibbendum3):
                Bib_take_pinte(Gasper)
        elif Is_one_case_range(Monstre,Gasper) == True :
            if Monstre == Master :
                print("Gasper entend un bruit de clé")
            elif Monstre == Fou :
                print("Gasper entend un rire sardonique")
            elif (Monstre == Bibbendum1 or Monstre == Bibbendum2 or Monstre == Bibbendum3):
                print("Gasper sent une odeur alléchante de chamallow à la fraise")
        else :
            mv=2
    for k in Pintes.keys():
        if (Pintes[k]["abs"]==Gasper["abs"] and Pintes[k]["ord"]==Gasper["ord"]):
            if Pintes[k]["nb"]==0:
                print "Tu as assez bu pochtron !!"
            else :
                print "Oh de la biere !! Gasper gagne %d pintes"%(Pintes[k]["nb"])
                Gasper["pinte"]=Gasper["pinte"]+Pintes[k]["nb"]
                Pintes[k]["nb"]=0

# Fonctions relatives à la positions des ennemis:
def Is_monstre(Index_pop,x):
    """vérifie s il y a déjà un monstre dans la piece, x étant la valeur envoyée par la fonction random"""
    flag = 0
    for i in Index_pop : #scan la liste Indice_pop pour voir si l indice aleatoire fournit par la fonction random.randit() n'a pas déjà été attribué à un autre monstre
        if x == i :
            flag = flag + 1 #ajoute 1 a la valeur de flag si le indice existe déjà dans Index_pop
    if flag > 0 :
        return True #indice déjà attribué à un monstre
    else :
        return False #indice pas utilisé pour un autre monstre, il est utilisable pour un nouveau monstre

def Pop_monstre(D,Liste_monstre,Index_pop):
    """fonction qui attribue les coordonnées à tous les monstres"""
    Index_pop = [] #reset l indice de pop si on veut faire repop les monstres de maniere aleatoire(sans que l ancien pop influe)
    for M in Liste_monstre:
        x = random.randint(0,12) # génère un indice aléatoire
        while Is_monstre(Index_pop,x) == True : #vérifie si l'indice est attribué à un autre monstre , si c est le cas relance random.randit
            x = random.randint(0,12)
        Index_pop.append(x) # note l'attribution d'indice dans Index_pop
        M["indice"] = x #permet de traquer l emplacement du monstre en cas de probleme avec Index_pop
        M["abs"] = Index_room[x][0] # modifie l'abs du monstre grace a l Index_room
        M["ord"] = Index_room[x][1] # modifie l ord du monstre grace a l Index_room
    for k in D.keys(): #Attribution des valeurs de salle aux pintes
        x = random.randint(0,12)
        while Is_monstre(Index_pop,x) == True :
            x = random.randint(0,12)
        Index_pop.append(x)
        D[k]["indice"]=x
        D[k]["abs"]=Index_room[x][0]
        D[k]["ord"]=Index_room[x][1]

def Is_one_case_range(Monstre,Gasper):
    """focntion qui verifie s'il y a un monstre à une case de Gasper"""
    if ((Monstre["ord"] == (Gasper["ord"] +1) or Monstre["ord"] == (Gasper["ord"] - 1)) and Monstre["abs"] == Gasper["abs"]): #monstre une case au dessus ou en dessous
        return True
    elif ((Monstre["abs"] == (Gasper["abs"] +1) or Monstre["abs"] == (Gasper["abs"] - 1)) and Monstre["ord"] == Gasper["ord"]): #monstre uns case à gauche ou à droite
        return True
    else :
        return False

#Maitre du chateau

def Retour_recep (x,y,Gasper) :
    """modifie les coordonnées de Gasper ce qui le place à la réception"""
    value=position(8,4,Plateau)
    x=8
    y=4
    return x,y,value


#Savant fou :

def Fou_take_pinte(Gasper):
    """Le Fou vole 1 pinte à Gasper, modifie la nombre de pinte que possède Gasper"""
    Gasper["pinte"] = Gasper["pinte"] - 1 #modifie la valeur dans le dict Gasper
    print("Gasper perd une pinte d'energie, il lui reste", Gasper["pinte"],"pinte(s) d'energie")

def Fou_depl(x,y,Gasper,Index_room):
    """pouvoir du Fou qui modifie de manière aléatoire la position de Gasper"""
    i = random.randint(0,12)
    y = Index_room[i][0]
    x = Index_room[i][1]
    value=position(x,y,Plateau)
    return x,y,value

#Chamallow bibbendum:


def Bib_take_pinte(Gasper):
    """Le Bibbendum vole 2 pintes à Gasper, modifie la nombre de pinte que possède Gasper"""
    Gasper["pinte"] = Gasper["pinte"] - 2
    print("Gasper une pinte d'energie, il lui reste", Gasper["pinte"],"pinte(s) d'energie")

#Intitialisation:

#Plateau de jeu
Index_pop = [] # contient des indices x générés alétoirement => Index_room[x] = coordonnees de la salle dans lequelle il y a le monstre qui a obtenue l'indice X
Index_room = [[0,2],[0,4],[0,6],[4,2],[4,4],[4,6],[8,2],[8,4],[8,6],[12,2],[12,4],[12,6],[4,0],[10,8]] #liste des salle du chateau Index_room[4,0] = reception , Index_room[10,8]=paradis
Gasper = {"abs" : 0, "ord" : 0, "pinte" : 3}
Master = {"abs" : None, "ord" : None, "indice": None}
Fou = {"abs": None, "ord": None, "indice": None}
Bibbendum1 = {"abs": None, "ord": None,"indice": None}
Bibbendum2 = {"abs": None, "ord": None, "indice": None}
Bibbendum3 = {"abs": None, "ord": None, "indice": None}
Pintes={}
Liste_monstre = [Master,Fou,Bibbendum1,Bibbendum2,Bibbendum3]
Plateau=[]


#Main

if __name__ == '__main__':

    Plateau=BuildCastle()
    afficher(Plateau)


    while True :
        answer=menu()
        os.system("clear")
        if answer==1:
            os.system("clear")
            x=8
            y=4
            value=position(x,y,Plateau)
            Pop_pinte(Pintes)
            Pop_monstre(Pintes,Liste_monstre,Index_pop)
        elif answer==2:
            os.system("clear")
            x,y,value=droite(x,y,value,Plateau)
        elif answer==3:
            os.system("clear")
            x,y,value=gauche(x,y,value,Plateau)
        elif answer==4:
            os.system("clear")
            x,y,value=haut(x,y,value,Plateau)
        elif answer==5:
            os.system("clear")
            x,y,value=bas(x,y,value,Plateau)
        elif answer==0:
            break
