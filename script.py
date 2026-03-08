


# initialisation de la game
game = [ 
    ["bt1","bc1","bf1","bq","br","bf2","bc2","bt2"], # p pion 1,2,3,4,5,6,7,8    1  postion : [n°ligne,n° collone]
    ["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"], # t tour 1 et 2           2 
    ["","","","","","","",""],                 # c cavalier 1 et 2               3
    ["","","","","","","",""],                 # f fou 1 et 2                    4
    ["","","","","","","",""],                 # r roi                           5
    ["wt1","","","","","","","wt2"],                 # q reine                         6
    ["wp1","wp2","wp3","wp4","wp5","wp6","wp7","wp8"], # b noir                  7
    ["wt1","wc1","wf1","wq","wr","wf2","wc2","wt2"]  # w blanc                   8
]

piece = {}
tour="w" # defini le début du tour au blanc
nottour="b"

for line in game:  #definir les position des piece
    for p in line:
        if "p" in p:
            piece[p]={
                "position":2,
                "moved?":False
            }
        if "t" in p:
            piece[p]={
                "position":2,
                "moved?":False
            }
        if "c" in p:
            piece[p]={
                "position":2
            }
        if "f" in p:
            piece[p]={
                "position":2
            }
        if "r" in p:
            piece[p]={
                "position":2,
                "moved?":False
            }
        if "q" in p:
            piece[p]={
                "position":2
            }
        else:
            pass


def postovalue(pos):
    return game[pos[0]][pos[1]]

def wichside(pini,pfin):                     #8 cas differend   hg h hd
    if pini[0]==pfin[0] and pini[1]<pfin[1]: # meme ligne        g P  d
        return "d"                           #                  bg b bd
    if pini[1]==pfin[1] and pini[0]<pfin[0]:
        return "b"
    if pini[0]==pfin[0] and pini[1]>pfin[1]:
        return "g"
    if pini[1]==pfin[1] and pini[0]>pfin[0]:
        return "h"
    if pini[0]>pfin[0] and pini[1]>pfin[1]:
        return "hd"
    if pini[0]>pfin[0] and pini[1]<pfin[1]:
        return "hg"
    if pini[0]<pfin[0] and pini[1]<pfin[1]:
        return "bg"
    if pini[0]<pfin[0] and pini[1]>pfin[1]:
        return "bd"

def verif(pos):# renvoie True si le mouv est impossible
    print(pos)
    if game[pos[0]][pos[1]]=="": return False
    elif nottour in game[pos[0]][pos[1]]: return False
    else: return True



def mouvtour(pini,pfin,n):
    side = wichside(pini,pfin) # detection du cote
    print(side)
    if side == "d":
        for i in range(pini[1]+1,pfin[1]+1):
            if not(verif([pini[0],i])):
                print(str(pini[0])+" , " + str(i) + " legal")
                continue
            print(str(pini[0])+" , " + str(i) + " Illegal")            
            return False

    if side == "g":
        for i in range(pfin[1],pini[1]):
            if not(verif([pini[0],i])):
                print(str(pini[0])+" , " + str(i) + " legal")
                continue
            print(str(pini[0])+" , " + str(i) + " Illegal")            
            return False

    if side == "h":
        for i in range(pfin[0],pini[0]):
            if not(verif([i,pini[1]])):
                print(str(i)+" , " + str(pini[1]) + " legal")
                continue
            print(str(i)+" , " + str(pini[1]) + " Illegal")            
            return False

    if side == "b":
        for i in range(pini[0]+1,pfin[0]+1):
            if not(verif([i,pini[0]])):
                print(str(i)+" , " + str(pini[0]) + " legal")
                continue
            print(str(i)+" , " + str(pini[0]) + " Illegal")            
            return False

    game[pini[0]][pini[1]]="" # on enleve la piece
    game[pfin[0]][pfin[1]]=tour+"t"+str(n) # on remet la piece
    
    return True

def mouvcavalier(pini,pfin,n):
    if verif(pfin):
        print(str(i)+" , " + str(pini[0]) + " Illegal")
        return False
    print(str(i)+" , " + str(pini[0]) + " legal")
    game[pini[0]][pini[1]]="" # on enleve la piece
    game[pfin[0]][pfin[1]]=tour+"c"+str(n) # on remet la piece
    return True

def deplacer(pini,pfin): # return false si le mouvement est impossible pini et pfin systeme de liste 1*1 a 8*8
    if pini==pfin: #verif si meme postion avent et apres
        return False
    piece=postovalue(pini)
    if "1" in piece: # detection du numéro de piece
        n=1
    elif "2" in piece:
        n=2
    elif "3" in piece:
        n=3
    elif "4" in piece:
        n=4
    elif "5" in piece:
        n=5
    elif "6" in piece:
        n=6
    elif "7" in piece:
        n=7
    elif "8" in piece:
        n=8
    else:
        n=False # False si pas de numero roi/reine
    
    if tour not in piece:  # verification si c'est le bon joueur
        return False
    
    if "t" in piece:
        return mouvtour(pini,pfin,n)
    if "c" in piece:
        return mouvcavalier(pini,pfin,n)
    if "f" in piece:
        return mouvfou(pini,pfin,n)
    if "p" in piece:
        return mouvpion(pini,pfin,n)
    if "r" in piece:
        return mouvroi(pini,pfin)
    if "q" in piece:
        return mouvqueen(pini,pfin)




if __name__ == "__main__":

    for line in game : print(line)
    deplacer([5,0],[6,0])
    print("\n")
    for line in game : print(line)
    #print(postovalue([7,7]))
    #for line in game : print(line)
    #print(piece)