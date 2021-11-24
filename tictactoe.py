#______(1)DECLARATIONS DES VARIABLES
tableau = []
taille_x = 3
taille_y = 3
for i in range(taille_x*taille_y) :
    tableau.append(0)
if taille_x >= taille_y:#determiner si le tableau est horizontale/carrée ou verticale
    grand = taille_x
    petit = taille_y
else :
    grand = taille_y
    petit = taille_x
combo_max = 3 #3 pour un tictactoe; 4 pour un puissance 4

tour = True
win_X = False
win_O = False
fini = False

#______(2)AFFICHAGE DU TABLEAU
def affichage():#création d'une fonction
    for i in range (0,taille_y):
        for j in range (0,taille_x):
            case = tableau[i*3+j]
            if case == 1 :
                print('X','',end='')
            elif case == 2 :
                print('O','',end='')
            else :
                print('*','',end='')
        print ('')#retour à la ligne
#______(3)TOUR DE JEU
def jeu(x):
    choix = -1
    while choix<0 or choix>8 or tableau[choix]!=0:
        choix = int(input("Choissisez une case : "))-1
        if choix<0 or choix>8 :
            print("Cette case n'existe pas !")
        elif tableau[choix]!=0 :
            print("Cette case est déjà prise !")

    tableau[choix]=x
    
#______(4)Verification victoire
#____________(4.1)Verification ligne verticale
def verification():
    for i in range (0,taille_x):
        
        if combo < combo_max:
            combo=0
            for j in range (0,taille_y):
                case = tableau[j*taille_x+i]
                if combo == 0 :
                    if case != 0 :
                        combo = combo+1
                else :
                    if case == tableau[case-taille_x] :
                        combo = combo+1
                    else :
                        combo = 0
        elif case == 1:
            win_X = True
        elif case == 2:
            win_O = True
                    
#____________(4.2)Verification ligne horizontale
    for i in range (0,taille_y):
        
        if combo < combo_max:
            combo=0
            for j in range (0,taille_x):
                case = tableau[i*taille_x+j]
                if combo == 0 :
                    if case != 0 :
                        combo = combo+1
                else :
                    if case == tableau[case-1] :
                        combo = combo+1
                    else :
                        combo = 0
        elif case == 1:
            win_X = True
        elif case == 2:
            win_O = True

#____________(4.3)Verification diagonale
    
    
    for i in range (0,grand-(petit-1)):
        for j in range (0,taille_x):
            if combo < combo_max:
                combo=0
                case = tableau[i+j*taille_x+j]
                if combo == 0 :
                    if case != 0 :
                        combo = combo+1
                else :
                    if case == tableau[case-1] :
                        combo = combo+1
                    else :
                        combo = 0
        for j in range (0,taille_x):
            if combo < combo_max:
                combo=0
                case = tableau[i+j*taille_x+j]
                if combo == 0 :
                    if case != 0 :
                        combo = combo+1
                else :
                    if case == tableau[case-1] :
                        combo = combo+1
                    else :
                        combo = 0
            elif case == 1:
                win_X = True
            elif case == 2:
                win_O = True

#______(5)Verification grille complète
    fini = True
    for i in range (0,taille_x*taille_y):
        if tableau [i] == 0:
            fini = False
        

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
    verification()
if win_O == True:
    print("Le joueur O à gagné !")
elif win_X == True :
    print("Le joueur X à gagné !")
else :
    print("match nul !")
affichage()