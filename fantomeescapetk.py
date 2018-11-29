# -*-coding:utf-8 -*
"""ce programme est un jeu, où l'utilisateur déplace un fantôme appelé Gasper.
Le but du jeu est de rejoindre le paradis en traversant le chateau tout en évitant
les monstres. Gasper doit toujours avoir au moins une pinte dans son inventaire,
si ce n'est pas la cas, c'est Game Over."""
#Importation des modules
from Tkinter import *
from tkMessageBox import *
import random
import os

def restart_programme():
    """Relance le programme en cours"""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def BuildCastle():
    """ Construction du chateau """
    grille=[[" "," ","*","*","*","*","*"," "," "," ","P"," "," "],[" "," ","*"," "," "," ","*"," "," "," ","*"," "," "],
    [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
    [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],["*"," ","*"," "," "," ","*"," "," "," ","*"," ","*"],
    [0,"*","*","*",0,"*","*","*",0,"*","*","*",0],[" "," ","*"," "," "," ","*"," "," "," "," "," "," "],
    [" "," ","*","*","R","*","*"," "," "," "," "," "," "]]
    return grille

def Chateautk(w,grille):
    size=len(grille)
    size2=len(grille[0])
    n=0
    for i in range(size):
        for j in range(size2):
            n=n+1
            if grille[i][j]=="P" or grille[i][j]==0 or grille[i][j]=="R" :
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
                
#Gaser et ses mouvements

def position(i,j,grille):
    """ Position de Gasper """ 
    global value
    value=grille[i][j]
    Gasper["abs"]=j
    Gasper["ord"]=i
    # Si la valeur temporaire correpond à la valeur du Paradis le fantôme gagne
    if value=="P":
        grille[i][j]="&"
        Chateautk(frame,grille)
        showinfo("Victoire","Gasper rejoint le paradis des fantomes")
        f.quit()
    elif Gasper["pinte"]<0 or Gasper["pinte"]==0:
        result=askquestion("RIP", "Oh non Gasper a diparu ! Veux-tu recommencer ?")
        if result=="no":
            f.quit()
        elif result=="yes":
            restart_programme()
    else :
        grille[i][j]="&"
        Chateautk(frame,grille)
        
#Gestion des limites de la matrice et des mouvements impossibles de Gasper

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
        Trigger(Gasper,Liste_monstre,Pintes)
        if mv==1:
            Retour_recep(i,j+1,value)
        elif mv==0 :
            Fou_depl(i,j+1,value,Index_room)
            Trigger(Gasper,Liste_monstre,Pintes)
        else :
            x=i
            y=j+1
    else :
        position(i,j,grille)
        showwarning("Warning","Mouvement impossible")
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
        Trigger(Gasper,Liste_monstre,Pintes)
        if mv==1:
            Retour_recep(i,j-1,value)
        elif mv==0 :
            Fou_depl(i,j-1,value,Index_room)
            Trigger(Gasper,Liste_monstre,Pintes)
        else :
            x=i
            y=j-1
    else :
        position(i,j,grille)
        showwarning("Warning","Mouvement impossible")
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
        Trigger(Gasper,Liste_monstre,Pintes)
        if mv==1:
            Retour_recep(i-1,j,value)
        elif mv==0 :
            Fou_depl(i-1,j,value,Index_room)
            Trigger(Gasper,Liste_monstre,Pintes)
        else :
            x=i-1
            y=j
    else :
        position(i,j,grille)
        showwarning("Warning","Mouvement impossible")
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
        Trigger(Gasper,Liste_monstre,Pintes)
        if mv==1:
            Retour_recep(i+1,j,value)
        elif mv==0 :
            Fou_depl(i+1,j,value,Index_room)
            Trigger(Gasper,Liste_monstre,Pintes)
        else :
            x=i+1
            y=j
    else :
        position(i,j,grille)
        showwarning("Warning","Mouvement impossible")
        x=i
        y=j

#Positionnement des ennemis:

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
    
def Pop_pinte(D):
    """Créer le nb de Pintes qui apparaissent dans le Château inférieur à 5 pintes dans tous le château """
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
    #Créer un dictionnaire correspondant aux salles avec des pintes et leur nombre, on peut avoir jusqu'à 5 salles 
    for i in range(len(Nb)):
        D[i]={"abs":None,"ord":None,"nb":Nb[i]}

def Pop_monstre(D,listm,Ip,Ir):
    """fonction qui attribue les coordonnées à tous les monstres"""
    Index_pop = [] #reset l indice de pop si on veut faire repop les monstres de maniere aleatoire(sans que l ancien pop influe)
    for M in listm:
        x = random.randint(0,11) # génère un indice aléatoire
        while Is_monstre(Ip,x) == True : #vérifie si l'indice est attribué à un autre monstre , si c est le cas relance random.randit
            x = random.randint(0,11)
        Ip.append(x) # note l'attribution d'indice dans Index_pop
        M["ord"] = Ir[x][0] # modifie l'abs du monstre grace a l Index_room
        M["abs"] = Ir[x][1] # modifie l ord du monstre grace a l Index_room
    for k in D.keys(): #Attribution des valeurs de salle aux pintes 
        x = random.randint(0,11) 
        while Is_monstre(Ip,x) == True : 
            x = random.randint(0,11)
        Ip.append(x)
        D[k]["ord"]=Ir[x][0] 
        D[k]["abs"]=Ir[x][1]
        
def Is_one_case_range(Monstre,joueur):
    """focntion qui verifie s'il y a un monstre à une case de joueur"""
    if ((Monstre["ord"] == (joueur["ord"] +1) or Monstre["ord"] == (joueur["ord"] - 1)) and Monstre["abs"] == joueur["abs"]): #monstre une case au dessus ou en dessous
        return True
    elif ((Monstre["abs"] == (joueur["abs"] +1) or Monstre["abs"] == (joueur["abs"] - 1)) and Monstre["ord"] == joueur["ord"]): #monstre uns case à gauche ou à droite
        return True
    else :
        return False

#Maitre du chateau

def Retour_recep (i,j,prev) :
    """modifie les coordonnées de joueur ce qui le place à la réception"""
    global x
    global y
    global value
    showinfo("Cher visiteur","Laissez-moi vous raccompagner à l'entrée de ma demeure")
    Plateau[i][j]=prev
    position(8,4,Plateau)
    x=8
    y=4

#Savant fou :

def Fou_take_pinte(joueur):
    """Le Fou vole 1 pinte à joueur, modifie la nombre de pinte que possède joueur"""
    joueur["pinte"] = joueur["pinte"] - 1 #modifie la valeur dans le dict Gasper
    showinfo("Comment oses-tu rentrer dans mon laboratoire ?","Gasper perd une pinte d'energie, il lui reste %d pinte(s) d'energie"%(Gasper['pinte']))

def Fou_depl(i,j,prev,listR):
    """pouvoir du Fou qui modifie de manière aléatoire la position de Gasper"""
    global x
    global y
    global value
    r = random.randint(0,11)
    x = listR[r][0]
    y = listR[r][1]
    Plateau[i][j]=prev
    position(x,y,Plateau)

#Chamallow bibbendum:

def Bib_take_pinte(joueur):
    """Le Bibbendum vole 2 pintes à Gasper, modifie la nombre de pinte que possède Gasper"""
    joueur["pinte"] = joueur["pinte"] - 2
    showinfo("De la mousse envahit la piece","Gasper perd une pinte d'energie, il lui reste %d pintes d'energie"%(joueur["pinte"]))


#Trigger à lancer apres chaque deplacement, cela permet la gestion des évênements d'intéraction entre les monstres et Gasper:
def Trigger(joueur,listm,dicP):
    global mv
    for Monstre in listm:
        if (Monstre["abs"]==joueur["abs"] and Monstre["ord"]==joueur["ord"]):
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
        elif Is_one_case_range(Monstre,joueur) == True :
            if Monstre == Master :
                showinfo("Warning","Gasper entend un bruit de clé")
            elif Monstre == Fou :
                showinfo("Warning","Gasper entend un rire sardonique")
            elif (Monstre == Bibbendum1 or Monstre == Bibbendum2 or Monstre == Bibbendum3):
                showinfo("Warning","Gasper sent une odeur alléchante de chamallow à la fraise")
        else :
            mv=2
    for k in dicP.keys():
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
    Index_pop = [] # contient des indices x générés alétoirement => Index_room[x] = coordonnees de la salle dans lequelle il y a le monstre qui a obtenue l'indice X
    Index_room = [[2,0],[4,0],[6,0],[2,4],[4,4],[6,4],[2,8],[4,8],[6,8],[2,12],[4,12],[6,12]] #liste des salle du chateau 
    Gasper = {"abs" : 0, "ord" : 0, "pinte" : 3}
    Master = {"abs" : None, "ord" : None}
    Fou = {"abs": None, "ord": None}
    Bibbendum1 = {"abs": None, "ord": None}
    Bibbendum2 = {"abs": None, "ord": None}
    Bibbendum3 = {"abs": None, "ord": None}
    Pintes={}
    Liste_monstre = [Master,Fou,Bibbendum1,Bibbendum2,Bibbendum3]

#Creation de la fenetre
    f=Tk()
    f.title("Gasper")
    frame=Frame(f)
    frame.pack()
    cadre=LabelFrame(f,text="Déplacement")
    cadre.pack(side=BOTTOM)
#Chateau
    Plateau=BuildCastle()
    Chateautk(frame,Plateau)
    value=0
    x=8
    y=4
    position(x,y,Plateau)
    Pop_pinte(Pintes)
    Pop_monstre(Pintes,Liste_monstre,Index_pop,Index_room)

#Bouton deplacement
    boutonl=Button(cadre,text="Gauche",command=lambda: gauche(x,y,value,Plateau))
    boutonr=Button(cadre,text="Droite",command=lambda: droite(x,y,value,Plateau))
    boutonu=Button(cadre,text="Haut",command=lambda: haut(x,y,value,Plateau))
    boutond=Button(cadre,text="Bas",command=lambda: bas(x,y,value,Plateau))
    boutonl.grid(row=1,column=1)
    boutonr.grid(row=1,column=2)
    boutonu.grid(row=1,column=3)
    boutond.grid(row=1,column=4)
#Bouton quitter
#Bouton restart
    boutonq=Button(cadre,text="Quit",command=f.quit)
    boutonq.grid(row=2,column=4)
    boutonres=Button(cadre,text="Restart",command=restart_programme)
    boutonres.grid(row=2,column=1)

    f.mainloop()
