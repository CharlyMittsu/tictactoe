#______(1)DECLARATIONS DES VARIABLES
tableau = []
taille_x = 3 #taille horizontale du tableau
taille_y = 3 #taille verticale du tableau
for i in range(taille_x*taille_y) :
    tableau.append(0)

combo_max = 3 #nombre de signe à la suite nécessaire pour gagner

tour = True
win_X = False
win_O = False
fini = False

#______(2)AFFICHAGE DU TABLEAU
def affichage():#création d'une fonction
    for i in range (0,taille_y):
        for j in range (0,taille_x):
            case = tableau[i*taille_x+j]
            if case == 1 :
                print('X','',end='')
            elif case == 2 :
                print('O','',end='')
            else :
                print('*','',end='')
        print ('')#retour à la ligne
#______(3)TOUR DE JEU
def jeu(x):
    choix = -1#à chaque fois on met par défaut une case qui n'existe pas pour rentrer dans la boucle
    while choix<0 or choix>len(tableau)-1 or tableau[choix]!=0:
        choix = int(input("Choissisez une case : "))-1
        if choix<0 or choix>len(tableau)-1 :
            print("Cette case n'existe pas !")
        elif tableau[choix]!=0 :
            print("Cette case est déjà prise !")

    tableau[choix]=x
    
#______(4)Verification victoire
#____________(4.1)Verification ligne verticale
def verification():
    combo=0
    for i in range (0,taille_x):
        
        if combo < combo_max:
            combo=0
            for j in range (0,taille_y):
                if combo<combo_max :
                    case = tableau[j*taille_x+i]
                    if combo == 0 :
                        if case != 0 :
                            combo = combo+1
                    else :
                        if case == tableau[(j-1)*taille_x+i] :
                            combo = combo+1
                        else :
                            combo = 0

        
                    
#____________(4.2)Verification ligne horizontale
    for i in range (0,taille_y):
        
        if combo < combo_max:
            combo=0
            for j in range (0,taille_x):
                if combo<combo_max :
                    case = tableau[i*taille_x+j]
                    if combo == 0 :
                        if case != 0 :
                            combo = combo+1
                    else :
                        if case == tableau[i*taille_x+j-1] :
                            combo = combo+1
                        else :
                            combo = 0


#____________(4.3)Verification diagonale
    
#décalage du code de vérif dans le cas d'un tableau plus grand

    for h in range (0,taille_y-(combo_max-1)):#parcourir le tableau verticalement
        if combo < combo_max:
            for i in range (0,taille_x-(combo_max-1)):#parcourir le tableau horizontalement
                if combo < combo_max:
                    combo=0

#vérification diagonale tic tac toe

                    for j in range (0,combo_max):#parcourir le tableau diagonalement de haut en bas   
                        case = tableau[h*taille_x+i+j*taille_x+j]
                        if combo == 0 :
                            if case != 0 :
                                combo = combo+1
                        else :
                            if case == tableau[h*taille_x+i+(j-1)*taille_x+j-1] :
                                combo = combo+1
                            else :
                                combo = 0
                if combo < combo_max:
                    combo=0                        
                    for j in range (0,combo_max):#parcourir le tableau diagonalement de bas en haut
                        case = tableau[h*taille_x+i+(combo_max-j-1)*taille_x+j]
                        if combo == 0 :
                            if case != 0 :
                                combo = combo+1
                        else :
                            if case == tableau[h*taille_x+i+(combo_max-j)*taille_x+j-1] :
                                combo = combo+1
                            else :
                                combo = 0
    if combo == combo_max:
        return (case)
    else :
        return 0        
    

#______(5)Verification grille complète
def complet():
    fini = True
    for i in range (0,taille_x*taille_y):
        if tableau [i] == 0:
            fini = False
    return fini
    
    
        

#______(6)JEU
while win_O == False and win_X == False and fini == False :
    affichage()

    if tour == True :
        print("Au tour du joueur O")
        jeu(2)
        tour = False
    else :
        print("Au tour du joueur X")
        jeu(1)
        tour = True
    case = verification()
    if case == 1:
        win_X = True
    elif case == 2:
        win_O = True
    fini = complet()
    
if win_O == True:
    print("Le joueur O à gagné !")
elif win_X == True :
    print("Le joueur X à gagné !")
else :
    print("match nul !")
affichage()