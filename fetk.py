# -*-coding:utf-8 -*
#Python 2.7
#Jeu Escape Game
#Jeremy BULLE et Domitille COQ--ETCHEGARAY
#Master 1 Bio-Informatique 2018-2019

"""Ce programme est un jeu, où l'utilisateur deplace un fantôme appele Gasper.
Le but du jeu est de rejoindre le paradis en traversant le chateau tout en evitant
les monstres. Gasper doit toujours avoir au moins une pinte dans son inventaire,
si ce n'est pas la cas, c'est Game Over."""

#Importation des modules
from Tkinter import *
from tkMessageBox import *
import random
import os
import sys

def restart_program():
    """Relance le programme en cours"""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def BuildCastle(n):
    """ Construction des elements du chateau """
    if n==1: #Level 1
        grille=[[" "," ","*","*","*","*","*"," "," "," ","E"," "," "],[" "," ","*"," "," "," ","*"," "," "," ","*"," "," "],
        [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
        [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
        [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],[" "," ","*"," "," "," ","*"," "," "," "," "," "," "],
        [" "," ","*","*","R","*","*"," "," "," "," "," "," "]]
        return grille
    elif n==2: #Level 2
        grille=[[" "," "," "," "," "," "," "," "," "," ","R"," "," "],[0,"*","*","*","*","*",0,"*","*"," ","*"," "," "],
        ["*"," "," "," ","*"," "," "," ",0,"*","*"," "," "],["*","*",0,"*","*","*",0," "," "," ","*"," "," "],
        [0," ","*"," "," "," ","*"," "," "," ",0," "," "],["*"," ","*"," "," "," ","*"," "," "," ","*"," "," "],
        ["*"," ","P"," "," "," ",0,"*","*","*","*"," "," "],["*"," ","*"," "," "," ","*"," "," "," ","*"," "," "],
        [0,"*",0,"*",0,"*","*","*","*","*",0," "," "]]
        return grille

def Salle(n):
    """ Determine les cases "Salle" de la matrice """
    if n==1: #Level 1
        salle=[[2,0],[4,0],[6,0],[2,4],[4,4],[6,4],[2,8],[4,8],[6,8],[2,12],[4,12],[6,12]]
        return salle
    elif n==2: #Level 2
        salle=[[8,0],[4,0],[1,0],[3,2],[8,2],[8,4],[1,6],[3,6],[6,6],[2,8],[4,10],[8,10]]
        return salle

def Chateautk(v,w,grille):
    """ Affichage interface graphique """
    #Affichage du nb de vie de Gasper tout le long de la partie
    varL="Nb de pintes de Gasper :%d"%(Gasper["pinte"])
    Label(v,text=varL).grid(row=3,column=1)
    size=len(grille)
    size2=len(grille[0])
    for i in range(size):
        for j in range(size2):
            #Creation des differentes cases
            if grille[i][j]==0 :
                Canvas(w,width=50,height=50,bg="Lightsteelblue3").grid(row=i,column=j)
            elif grille[i][j]=="E":
                Canvas(w,width=50,height=50,bg="firebrick4").grid(row=i,column=j)
            elif grille[i][j]=="P" :
                Canvas(w,width=50,height=50,bg="SpringGreen4").grid(row=i,column=j)
            elif grille[i][j]=="R":
                Canvas(w,width=50,height=50,bg="DarkOrchid4").grid(row=i,column=j)
            elif grille[i][j]=="*":
                Canvas(w,width=50,height=50,bg="dark slate grey").grid(row=i,column=j)
            elif grille[i][j]==" ":
                Canvas(w,width=50,height=50,bg="gray6").grid(row=i,column=j)
            elif grille[i][j]=="&":
                can=Canvas(w,width=50,height=50)
                can.grid(row=i,column=j)
                #Affichage d'une image a place d'une simple case
                img=PhotoImage(file="cat-ghost-pattern.gif",master=can)
                can.create_image(50/2,50/2,image=img)
                label=Label(image=img)
                label.image=img

#Gasper et ses mouvements

def position(i,j,grille):
    """ Position de Gasper """
    global value
    global level
    global Index_room
    global Index_pop
    global Liste_monstre
    global x
    global y
    global Plateau
    value=grille[i][j] #Recupere la valeur de la matrice ou va se deplacer Gasper
    #Modification des coordonnees de la position de Gasper
    Gasper["abs"]=j
    Gasper["ord"]=i
    # Si la valeur temporaire correpond a la valeur du Paradis le fantôme gagne
    if value=="P":
        grille[i][j]="&"
        Chateautk(vie,frame,grille)
        result=askquestion("Victoire","Veux tu recommencer ?")
        if result=="no":
            showinfo("Gasper","Gasper rejoint le paradis des fantômes")
            f.quit() #Ferme la fenetre Tk()
        elif result=="yes":
            restart_program() #Relance le programme
    #Si la valeur correspond a la valeur de l'etage on lance le niveau 2
    elif value=="E":
        grille[i][j]="&"
        Chateautk(vie,frame,grille)
        showinfo("Ascenseur","Veuillez monter dans l'ascenseur")
        #Initialisation du deuxieme niveau
        level=2
        Plateau=BuildCastle(level)
        Index_room=Salle(level)
        Liste_monstre=choix_monstre(level)
        x=0
        y=10
        position(x,y,Plateau)
        Index_pop = []
        Pop_pinte(Pintes)
        Pop_monstre(Pintes,Liste_monstre,Index_pop,Index_room)
        return value
    elif Gasper["pinte"]<0 or Gasper["pinte"]==0:
        result=askquestion("RIP", "Oh non Gasper a diparu ! Veux-tu recommencer ?")
        if result=="no":
            f.quit() #Ferme la fenetre Tk()
        elif result=="yes":
            restart_program() #Relance le programme
    else :
        grille[i][j]="&"
        Chateautk(vie,frame,grille)

#Gestion des limites de la matrice et des mouvements impossibles de Gasper

def Limite(x,y,grille):
    """ Delimite l'espace du terrain de jeu"""
    size=len(grille)
    size1=len(grille[0])
    # Limite de la matrice
    if x>size-1 :
        return True
    elif y>size1-1:
        return True
    #Empeche l'utilisation de valeur negative pour le depacement de Gasper
    elif x==-1:
        return True
    elif y==-1:
        return True
    # Si jamais la valeur temporaire est " " Gasper rencontre un mur et ne peut pas passer
    elif grille[x][y]==" ":
        return True

def droite(i,j,prev,grille,lm,joueur,dp,Ip,n,Ir):
    """Deplacement d'une case a droite"""
    global x
    global y
    global value
    global mv
    grille[i][j]=prev
    if Limite(i,j+1,grille)!=True:
        position(i,j+1,grille)
        Trigger(joueur,Ip,lm,dp,Ir)
        if mv==1:
            Retour_recep(n,i,j+1,value)
        elif mv==0 :
            Fou_depl(i,j+1,value,Ir)
            Trigger(joueur,Ip,lm,dp,Ir)
        else :
            x=i
            y=j+1
    else :
        position(i,j,grille)
        showwarning("Warning","Mouvement impossible")
        x=i
        y=j

def gauche(i,j,prev,grille,lm,joueur,dp,Ip,n,Ir):
    """ Deplacement d'une case a gauche"""
    global x
    global y
    global value
    global mv
    grille[i][j]=prev
    if Limite(i,j-1,grille)!=True:
        position(i,j-1,grille)
        Trigger(joueur,Ip,lm,dp,Ir)
        if mv==1:
            Retour_recep(n,i,j-1,value)
        elif mv==0 :
            Fou_depl(i,j-1,value,Index_room)
            Trigger(joueur,Ip,lm,dp,Ir)
        else :
            x=i
            y=j-1
    else :
        position(i,j,grille)
        showwarning("Warning","Mouvement impossible")
        x=i
        y=j


def haut(i,j,prev,grille,lm,joueur,dp,Ip,n,Ir):
    """Deplacement d'une case au dessus"""
    global x
    global y
    global value
    global mv
    grille[i][j]=prev
    if Limite(i-1,j,grille)!=True:
        position(i-1,j,grille)
        Trigger(joueur,Ip,lm,dp,Ir)
        if mv==1:
            Retour_recep(n,i-1,j,value)
        elif mv==0 :
            Fou_depl(i-1,j,value,Ir)
            Trigger(joueur,Ip,lm,dp,Ir)
        else :
            x=i-1
            y=j
    else :
        position(i,j,grille)
        showwarning("Warning","Mouvement impossible")
        x=i
        y=j

def bas(i,j,prev,grille,lm,joueur,dp,Ip,n,Ir):
    """Deplacement d'une case en dessous"""
    global x
    global y
    global value
    global mv
    grille[i][j]=prev
    if Limite(i+1,j,grille)!=True:
        position(i+1,j,grille)
        Trigger(joueur,Ip,lm,dp,Ir)
        if mv==1:
            Retour_recep(n,i+1,j,value)
        elif mv==0 :
            Fou_depl(i+1,j,value,Ir)
            Trigger(joueur,Ip,lm,dp,Ir)
        else :
            x=i+1
            y=j
    else :
        position(i,j,grille)
        showwarning("Warning","Mouvement impossible")
        x=i
        y=j

#Positionnement des ennemis:

def Is_monstre(Ip,x):
    """verifie s il y a deja un monstre dans une case "Salle", x etant la valeur envoyee par la fonction random"""
    flag = 0
    for i in Ip : #scan la liste Indice_pop pour voir si l indice aleatoire fournit par la fonction random.randit() n'a pas deja ete attribue a un autre monstre
        if x == i :
            flag = flag + 1 #ajoute 1 a la valeur de flag si le indice existe deja dans Index_pop
    if flag > 0 :
        return True #indice deja attribue a un monstre
    else :
        return False #indice pas utilise pour un autre monstre, il est utilisable pour un nouveau monstre

def Pop_pinte(D):
    """Creer le nb de Pintes qui apparaissent dans le Château inferieur a 5 pintes dans tous le château """
    Pintet=0 #Nb total de pintes dans le chateau
    Nb=[] #Liste permettant de conserver les combinaisons possibles
    while(Pintet<5):
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
    #Creer un dictionnaire correspondant aux salles avec des pintes et leur nombre, on peut avoir jusqu'a 5 salles
    for i in range(len(Nb)):
        D[i]={"abs":None,"ord":None,"nb":Nb[i]}

def choix_monstre(n):
    """Determine les monstres present dans le chateau en fonction du niveau"""
    if n==1: #Level 1
        choix={"Master" : {"abs": None, "ord": None},"Fou" :{"abs": None, "ord": None}, "Bibbendum1": {"abs": None, "ord": None},"Bibbendum2": {"abs": None, "ord": None}, "Bibbendum3": {"abs": None, "ord": None}}
        return choix
    if n==2: #Level 2
        choix={"Master" : {"abs": None, "ord": None},"Fou": {"abs": None, "ord": None},"Bibbendum1": {"abs": None, "ord": None}, "Gobelin" : {"abs": None, "ord": None}}
        return choix

def Pop_monstre(D,lm,Ip,Ir):
    """fonction qui attribue les coordonnees a tous les monstres"""
    for M in lm.keys() :
        x = random.randint(0,11) # genère un indice aleatoire
        while Is_monstre(Ip,x) == True : #verifie si l'indice est attribue a un autre monstre , si c est le cas relance random.randit
            x = random.randint(0,11)
        Ip.append(x) # note l'attribution d'indice dans Index_pop
        lm[M]["ord"] = Ir[x][0] # modifie l'abs du monstre grace a l Index_room
        lm[M]["abs"] = Ir[x][1] # modifie l ord du monstre grace a l Index_room
    for k in D.keys(): #Attribution des valeurs de salle aux pintes
        x = random.randint(0,11)
        while Is_monstre(Ip,x) == True :
            x = random.randint(0,11)
        Ip.append(x)
        D[k]["ord"]=Ir[x][0]
        D[k]["abs"]=Ir[x][1]

def Is_one_case_range(Monstre,joueur,lm):
    """focntion qui verifie s'il y a un monstre a une case de Gasper"""
    if ((lm[Monstre]["ord"] == (joueur["ord"] +1) or lm[Monstre]["ord"] == (joueur["ord"] - 1)) and lm[Monstre]["abs"] == joueur["abs"]): #monstre une case au dessus ou en dessous
        return True
    elif ((lm[Monstre]["abs"] == (joueur["abs"] +1) or lm[Monstre]["abs"] == (joueur["abs"] - 1)) and lm[Monstre]["ord"] == joueur["ord"]): #monstre uns case a gauche ou a droite
        return True
    else :
        return False

#Maitre du chateau
#Evenement
def Retour_recep (n,i,j,prev) :
    """modifie les coordonnees de joueur ce qui le place a la reception"""
    global x
    global y
    global value
    showinfo("Cher visiteur","Laissez-moi vous raccompagner a l'entree de ma demeure")
    Plateau[i][j]=prev
    if n==1:
        x=8
        y=4
    if n==2:
        x=0
        y=10
    position(x,y,Plateau)

#Savant fou :
#Evenement
def Fou_take_pinte(joueur):
    """Le Fou vole 1 pinte a joueur, modifie la nombre de pinte que possède joueur"""
    joueur["pinte"] = joueur["pinte"] - 1 #modifie la valeur dans le dict Gasper
    showinfo("Comment oses-tu rentrer dans mon laboratoire ?","Gasper perd une pinte d'energie, il lui reste %d pinte(s) d'energie"%(Gasper['pinte']))

def Fou_depl(i,j,prev,listR):
    """pouvoir du Fou qui modifie de manière aleatoire la position de Gasper"""
    global x
    global y
    global value
    r = random.randint(0,11)
    x = listR[r][0]
    y = listR[r][1]
    Plateau[i][j]=prev
    position(x,y,Plateau)

#Chamallow bibbendum:
#Evenement
def Bib_take_pinte(joueur):
    """Le Bibbendum vole 2 pintes a Gasper, modifie la nombre de pinte que possède Gasper"""
    joueur["pinte"] = joueur["pinte"] - 2
    showinfo("De la mousse envahit la piece","Gasper perd une pinte d'energie, il lui reste %d pintes d'energie"%(joueur["pinte"]))

#Gobelin
def Gobelin_skill(joueur, Ip, lm,Ir):
    """Le gobelin vole 1 pinte a Gasper et se teleporte dans une autre case "Salle" vide """
    joueur["pinte"] = joueur["pinte"] - 1
    showinfo("Arglglglglglgl", "Le gobelin fuit et derobe une pinte d'ectoplasme a Gasper, il reste %d pinte(s) d'ectoplasme a Gasper"%(joueur["pinte"]))
    x = random.randint(0,11) # genère un indice aleatoire
    while Is_monstre(Ip,x) == True : #verifie si l'indice est attribue a un autre monstre , si c est le cas relance random.randit
        x = random.randint(0,11)
    Ip[3]= x # modifie le nouvel intice attribue au gobelin
    lm["Gobelin"]["ord"] = Ir[x][0] # modifie l'abs du Gobelin grace a l Index_room
    lm["Gobelin"]["abs"] = Ir[x][1] # modifie l ord du Gobelin grace a l Index_room

#Trigger a lancer apres chaque deplacement, cela permet la gestion des evênements d'interaction entre les monstres et Gasper:
def Trigger(joueur,Ip,listm,dicP,Ir):
    global mv
    for Monstre in listm.keys(): #Monstre
        if (listm[Monstre]["abs"]==joueur["abs"] and listm[Monstre]["ord"]==joueur["ord"]):
            if Monstre == "Master":
                mv=1
                return mv
            elif Monstre == "Fou" :
                mv=0
                Fou_take_pinte(joueur)
                return mv
            elif Monstre == "Gobelin" :
                Gobelin_skill(joueur,Ip,listm,Ir)
            elif (Monstre == "Bibbendum1" or Monstre == "Bibbendum2" or Monstre == "Bibbendum3"):
                Bib_take_pinte(joueur)
        elif Is_one_case_range(Monstre,joueur,listm) == True :
            if Monstre == "Master" :
                showinfo("Warning","Gasper entend un bruit de cle")
            elif Monstre == "Gobelin":
                showinfo("Warning","Gasper entend un petit ricanement")
            elif Monstre == "Fou" :
                showinfo("Warning","Gasper entend un rire sardonique")
            elif (Monstre ==" Bibbendum1" or Monstre == "Bibbendum2" or Monstre == "Bibbendum3"):
                showinfo("Warning","Gasper sent une odeur allechante de chamallow a la fraise")
        else :
            mv=2
    for k in dicP.keys(): #Pintes
        if (dicP[k]["abs"]==joueur["abs"] and dicP[k]["ord"]==joueur["ord"]):
            if Pintes[k]["nb"]==0:
                showinfo("Bar","Tu as assez bu pochtron !!")
            else :
                showinfo("Bar","Oh de l'ectoplasme !! Gasper gagne %d pintes"%(dicP[k]["nb"]))
                joueur["pinte"]=joueur["pinte"]+dicP[k]["nb"]
                dicP[k]["nb"]=0
#Main

if __name__ == '__main__':

#Intitialisation:

#Plateau de jeu
    level=1
    Index_pop = [] # contient des indices x generes aletoirement => Index_room[x] = coordonnees de la salle dans lequelle il y a le monstre qui a obtenue l'indice X
    Index_room = Salle(level) #liste des salle du chateau
    Gasper = {"abs" : 0, "ord" : 0, "pinte" : 3} #Creation de Gasper
    Pintes={} #Creation des pintes
    Liste_monstre = choix_monstre(level) #Creation des monstres

#Creation de la fenetre et des cadres affichant les boutons et la vie de Gasper
    f=Tk()
    f.title("Fantôme Escape")
    frame=Frame(f)
    frame.pack()
    vie=LabelFrame(f,text="Vie")
    vie.pack()
    cadre=LabelFrame(f,text="Deplacement")
    cadre.pack()
    cadre2=Label(f)
    cadre2.pack()
#Apparition des monstres Gasper et Pintes dans la matrice
    Plateau=BuildCastle(level)
    Chateautk(vie,frame,Plateau)
    value=0
    x=8
    y=4
    position(x,y,Plateau)
    Pop_pinte(Pintes)
    Pop_monstre(Pintes,Liste_monstre,Index_pop,Index_room)

#Bouton deplacement
    boutonl=Button(cadre,text="Gauche",command=lambda: gauche(x,y,value,Plateau,Liste_monstre,Gasper,Pintes,Index_pop,level,Index_room)).grid(row=1,column=1)
    boutonr=Button(cadre,text="Droite",command=lambda: droite(x,y,value,Plateau,Liste_monstre,Gasper,Pintes,Index_pop,level,Index_room)).grid(row=1,column=2)
    boutonu=Button(cadre,text="Haut",command=lambda: haut(x,y,value,Plateau,Liste_monstre,Gasper,Pintes,Index_pop,level,Index_room)).grid(row=1,column=3)
    boutond=Button(cadre,text="Bas",command=lambda: bas(x,y,value,Plateau,Liste_monstre,Gasper,Pintes,Index_pop,level,Index_room)).grid(row=1,column=4)
#Bouton quitter\Bouton restart
    boutonq=Button(cadre2,text="Quit",command=f.quit).grid(row=2,column=4)
    boutonres=Button(cadre2,text="Restart",command=restart_program).grid(row=2,column=1)

    f.mainloop()
