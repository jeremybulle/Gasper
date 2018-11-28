# -*-coding:utf-8 -*

#Importation des modules
from Tkinter import *
from tkMessageBox import *
import random
import os
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def position(i,j,grille):
    """ Position de Gasper """ 
    global value
    value=grille[i][j]
    Gasper["abs"]=j
    Gasper["ord"]=i
    # Si la valeur temporaire correpond à la valeur du Paradis le fantôme gagne
    if value==2:
        grille[i][j]="&"
        Chateautk(frame,grille)
        showinfo("GG !!","You win")
        f.quit()
    elif Gasper["pinte"]<0 or Gasper["pinte"]==0:
        result=askquestion("RIP", "Game Over")
        if result=="no":
            f.quit()
        elif result=="yes":
            restart_program()
    else :
        grille[i][j]="&"
        Chateautk(frame,grille)

def BuildCastle():
    """ Construction du chateau """
    grille=[[" "," ","*","*","*","*","*"," "," "," ",2," "," "],[" "," ","*"," "," "," ","*"," "," "," ","*"," "," "],
    [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
    [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
    [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],[" "," ","*"," "," "," ","*"," "," "," "," "," "," "],
    [" "," ","*","*",1,"*","*"," "," "," "," "," "," "]]
    return grille

def Pop_pinte(D):
    """Créer le nb de Pintes qui apparaissent dans le Château inférieur à 5 pintes dans tous le château """
    Pintet=0 #Nb total de pintes dans le chateau
    Nb=[] #Liste permettant de conserver les combinaisons possibles 
    while(Pintet<5):
        if Pintet==1:
            x=random.randint(1,3)
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
            x=random.randint(1,3)
            Pintet=Pintet+x
            Nb.append(x)
    #Créer un dictionnaire correspondant aux salles avec des pintes et leur nombre, on peut avoir jusqu'à 5 salles 
    for i in range(len(Nb)):
        Pintes[i]={"abs":None,"ord":None,"nb":Nb[i]}
    
        

#positionnement des ennemis:

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
        x = random.randint(0,11) # génère un indice aléatoire
        while Is_monstre(Index_pop,x) == True : #vérifie si l'indice est attribué à un autre monstre , si c est le cas relance random.randit
            x = random.randint(0,11)
        Index_pop.append(x) # note l'attribution d'indice dans Index_pop
        M["indice"] = x #permet de traquer l emplacement du monstre en cas de probleme avec Index_pop
        M["ord"] = Index_room[x][0] # modifie l'abs du monstre grace a l Index_room
        M["abs"] = Index_room[x][1] # modifie l ord du monstre grace a l Index_room
    for k in D.keys(): #Attribution des valeurs de salle aux pintes 
        x = random.randint(0,11) 
        while Is_monstre(Index_pop,x) == True : 
            x = random.randint(0,11)
        Index_pop.append(x)
        D[k]["indice"]=x
        D[k]["ord"]=Index_room[x][0] 
        D[k]["abs"]=Index_room[x][1]
        
def Is_one_case_range(Monstre,Gasper):
    """focntion qui verifie s'il y a un monstre à une case de Gasper"""
    if ((Monstre["ord"] == (Gasper["ord"] +1) or Monstre["ord"] == (Gasper["ord"] - 1)) and Monstre["abs"] == Gasper["abs"]): #monstre une case au dessus ou en dessous
        return True
    elif ((Monstre["abs"] == (Gasper["abs"] +1) or Monstre["abs"] == (Gasper["abs"] - 1)) and Monstre["ord"] == Gasper["ord"]): #monstre uns case à gauche ou à droite
        return True
    else :
        return False

#Maitre du chateau

def Retour_recep (i,j,Gasper) :
    """modifie les coordonnées de Gasper ce qui le place à la réception"""
    global x
    global y
    global value
    position(8,4,Plateau)
    x=8
    y=4


#Savant fou :

def Fou_take_pinte(Gasper):
    """Le Fou vole 1 pinte à Gasper, modifie la nombre de pinte que possède Gasper"""
    Gasper["pinte"] = Gasper["pinte"] - 1 #modifie la valeur dans le dict Gasper
    showinfo("Nani ??","Gasper perd une pinte d'energie, il lui reste %d pinte(s) d'energie"%(Gasper['pinte']))

def Fou_depl(i,j,Gasper,Index_room):
    """pouvoir du Fou qui modifie de manière aléatoire la position de Gasper"""
    global x
    global y
    global value
    r = random.randint(0,11)
    x = Index_room[r][0]
    y = Index_room[r][1]
    position(x,y,Plateau)

#Chamallow bibbendum:


def Bib_take_pinte(Gasper):
    """Le Bibbendum vole 2 pintes à Gasper, modifie la nombre de pinte que possède Gasper"""
    Gasper["pinte"] = Gasper["pinte"] - 2
    showinfo("Nani ??","Gasper perd une pinte d'energie, il lui reste %d pintes d'energie"%(Gasper["pinte"]))


#Trigger a poser apres chaque deplacement:
def Trigger(x,y,prev,Gasper):
    global mv
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
                showinfo("Warning","Gasper entend un bruit de clé")
            elif Monstre == Fou :
                showinfo("Warning","Gasper entend un rire sardonique")
            elif (Monstre == Bibbendum1 or Monstre == Bibbendum2 or Monstre == Bibbendum3):
                showinfo("Warning","Gasper sent une odeur alléchante de chamallow à la fraise")
        else :
            mv=2
    for k in Pintes.keys():
        if (Pintes[k]["abs"]==Gasper["abs"] and Pintes[k]["ord"]==Gasper["ord"]):
            if Pintes[k]["nb"]==0:
                showinfo("Bar","Tu as assez bu pochtron !!")
            else : 
                showinfo("Bar","Oh de l'ectoplasme !! Gasper gagne %d pintes"%(Pintes[k]["nb"]))
                Gasper["pinte"]=Gasper["pinte"]+Pintes[k]["nb"]
                Pintes[k]["nb"]=0


def Limite(x,y,grille):
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
  
def droite(i,j,prev,grille):
    global x
    global y
    global value
    global mv
    grille[i][j]=prev
    if Limite(i,j+1,grille)!=True:
        position(i,j+1,grille)
        Trigger(i,j,prev,Gasper)
        if mv==1:
            Retour_recep(i,j,Gasper)
            grille[i][j+1]=value
        elif mv==0 :
            Fou_depl(i,j,Gasper,Index_room)
            Trigger(i,j,prev,Gasper)
            grille[i][j+1]=value
        else :
            x=i
            y=j+1
    else :
        position(i,j,grille)
        showinfo("Warning","Mouvement impossible")
        x=i
        y=j
        
def gauche(i,j,prev,grille):
    global x
    global y
    global value
    global mv
    grille[i][j]=prev
    if Limite(i,j-1,grille)!=True:
        position(i,j-1,grille)
        Trigger(i,j,prev,Gasper)
        if mv==1:
            Retour_recep(i,j,Gasper)
            grille[i][j-1]=value
        elif mv==0 :
            Fou_depl(i,j,Gasper,Index_room)
            Trigger(i,j,prev,Gasper)
            grille[i][j+1]=value
        else :
            x=i
            y=j-1
    else :
        position(i,j,grille)
        showinfo("Warning","Mouvement impossible")
        x=i
        y=j
    

def haut(i,j,prev,grille):
    global x
    global y
    global value
    global mv
    grille[i][j]=prev
    if Limite(i-1,j,grille)!=True:
        position(i-1,j,grille)
        Trigger(i,j,prev,Gasper)
        if mv==1:
            Retour_recep(i,j,Gasper)
            grille[i-1][j]=value
        elif mv==0 :
            Fou_depl(i,j,Gasper,Index_room)
            Trigger(i,j,prev,Gasper)
            grille[i-1][j]=value
        else :
            x=i-1
            y=j
    else :
        position(i,j,grille)
        showinfo("Warning","Mouvement impossible")
        x=i
        y=j
    
def bas(i,j,prev,grille):
    global x
    global y
    global value
    global mv
    grille[i][j]=prev
    if Limite(i+1,j,grille)!=True:
        position(i+1,j,grille)
        Trigger(i,j,prev,Gasper)
        if mv==1:
            Retour_recep(i,j,Gasper)
            grille[i+1][j]=value
        elif mv==0 :
            Fou_depl(i,j,Gasper,Index_room)
            Trigger(i,j,prev,Gasper)
            grille[i+1][j]=value
        else :
            x=i+1
            y=j
    else :
        position(i,j,grille)
        showinfo("Warning","Mouvement impossible")
        x=i
        y=j

def Chateautk(w,grille):
    size=len(grille)
    size2=len(grille[0])
    n=0
    for i in range(size):
        for j in range(size2):
            n=n+1
            if grille[i][j]==1 or grille[i][j]==0 or grille[i][j]==2 :
                Canvas(w,width=50,height=50,bg="Lightsteelblue3").grid(row=i,column=j)
            elif grille[i][j]=="*":
                Canvas(w,width=50,height=50,bg="dark slate grey").grid(row=i,column=j)
            elif grille[i][j]==" ":
                Canvas(w,width=50,height=50,bg="gray6").grid(row=i,column=j)
            elif grille[i][j]=="&":
                can=Canvas(w,width=50,height=50)
                can.grid(row=i,column=j)
                img=PhotoImage(file="cat-ghost-pattern.gif",master=can)
                can.create_image(50/2,50/2,image=img)
                label=Label(image=img)
                label.image=img

Plateau=BuildCastle()

#Intitialisation:

#Plateau de jeu
Index_pop = [] # contient des indices x générés alétoirement => Index_room[x] = coordonnees de la salle dans lequelle il y a le monstre qui a obtenue l'indice X
Index_room = [[2,0],[4,0],[6,0],[2,4],[4,4],[6,4],[2,8],[4,8],[6,8],[2,12],[4,12],[6,12]] #liste des salle du chateau Index_room[5,1] = reception , Index_room[13]=paradis
Gasper = {"abs" : 0, "ord" : 0, "pinte" : 3}
Master = {"abs" : None, "ord" : None, "indice": None}
Fou = {"abs": None, "ord": None, "indice": None}
Bibbendum1 = {"abs": None, "ord": None,"indice": None}
Bibbendum2 = {"abs": None, "ord": None, "indice": None}
Bibbendum3 = {"abs": None, "ord": None, "indice": None}
Pintes={}
Liste_monstre = [Master,Fou,Bibbendum1,Bibbendum2,Bibbendum3]

#Creation de la fenetre
f=Tk()
f.title("Gasper")
frame=Frame(f)
frame.pack()
Chateautk(frame,Plateau)
cadre=LabelFrame(f,text="Déplacement")
cadre.pack(side=BOTTOM)
#Chateau

value=0
x=8
y=4
position(x,y,Plateau)
Pop_pinte(Pintes)
Pop_monstre(Pintes,Liste_monstre,Index_pop)

#Bouton deplacement

boutonl=Button(cadre,text="Left",command=lambda: gauche(x,y,value,Plateau))
boutonr=Button(cadre,text="Right",command=lambda: droite(x,y,value,Plateau))
boutonu=Button(cadre,text="Up",command=lambda: haut(x,y,value,Plateau))
boutond=Button(cadre,text="Down",command=lambda: bas(x,y,value,Plateau))
boutonl.grid(row=10,column=1)
boutonr.grid(row=10,column=2)
boutonu.grid(row=10,column=3)
boutond.grid(row=10,column=4)
#Bouton quitter 
boutonq=Button(cadre,text="Quit",command=f.quit)
boutonq.grid(row=10,column=5)

#Main
f.mainloop()
