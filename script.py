


# initialisation de la game
game = [ 
    ["bt1","bc1","bf1","bq","br","bf2","bc2","bt2"], # p pion 1,2,3,4,5,6,7,8    1  postion : [n°ligne,n° collone]
    ["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"], # t tour 1 et 2           2 
    ["","","","","","","",""],                 # c cavalier 1 et 2               3
    ["","","","","","","",""],                 # f fou 1 et 2                    4
    ["","","","","","","",""],                 # r roi                           5
    ["wf1","","","","","","",""],                 # q reine                         6
    ["wp1","wp2","wp3","wp4","wp5","wp6","wp7","wp8"], # b noir                  7
    ["wt1","wc1","wf1","wq","wr","wf2","wc2","wt2"]  # w blanc                   8
]

piece = {}
tour="w" # defini le début du tour au blanc
nottour="b"

ligne=-1
for line in game:  #definir les position des piece
    ligne+=1
    collone=-1
    for p in line:
        collone+=1
        if "p" in p:
            piece[p]={
                "position":[ligne,collone],
                "moved?":False
            }
        if "t" in p:
            piece[p]={
                "position":[ligne,collone],
                "moved?":False
            }
        if "c" in p:
            piece[p]={
                "position":[ligne,collone]
            }
        if "f" in p:
            piece[p]={
                "position":[ligne,collone]
            }
        if "r" in p:
            piece[p]={
                "position":[ligne,collone],
                "moved?":False
            }
        if "q" in p:
            piece[p]={
                "position":[ligne,collone]
            }
        else:
            pass


def postovalue(pos):
    return game[pos[0]][pos[1]]

def valuetopos(value):
    return piece[value]["position"]

def updatedico(pini,pfin):
    p=postovalue(pini)
    piece[p]["position"] = pfin
    piece[p]["moved?"] = True

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
        return "hg"
    if pini[0]>pfin[0] and pini[1]<pfin[1]:
        return "hd"
    if pini[0]<pfin[0] and pini[1]<pfin[1]:
        return "bd"
    if pini[0]<pfin[0] and pini[1]>pfin[1]:
        return "bg"

def verif(pos):# renvoie True si le mouv est impossible
    print(pos)
    if game[pos[0]][pos[1]]=="": return False
    elif nottour in game[pos[0]][pos[1]]: return False
    else: return True

def mouv(pini,pfin,n,piece):
    updatedico(pini,pfin)
    game[pini[0]][pini[1]]="" # on enleve la piece
    game[pfin[0]][pfin[1]]=tour+piece+str(n) # on remet la piece

def mouvtour(pini,pfin,n):
    side = wichside(pini,pfin) # detection du cote
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

    mouv(pini,pfin,n,"t")
    return True

def mouvcavalier(pini,pfin,n):
    if verif(pfin) or (pfin[0]-pini[0])**2+(pfin[1]-pini[1])**2!=5:
        print(str(pfin[0])+" , " + str(pfin[1]) + " Illegal")
        return False
    print(str(pfin[0])+" , " + str(pfin[1]) + " legal")

    mouv(pini,pfin,n,"c")
    return True

def mouvfou(pini,pfin,n):
    side = wichside(pini,pfin) # detection du cote
    print(side)
    
    if side == "bd":
        if abs(pini[0]-pini[1])!=abs(pfin[0]-pfin[1]):
            return False
        for i in range(pini[0]+1,pfin[0]+1):
            for k in range(pini[1]+1,pfin[1]+1):
                if abs(i-k)!=abs(pini[0]-pini[1]):
                    continue
                if not(verif([i,k])):
                    print(str(i)+" , " + str(k) + " legal")
                    continue
                print(str(i)+" , " + str(k) + " Illegal")

    if side == "hg":
        if abs(pini[0]-pini[1])!=abs(pfin[0]-pfin[1]):
            return False
        for i in range(pfin[0],pini[0]):
            for k in range(pfin[1],pini[1]):
                if abs(i-k)!=abs(pini[0]-pini[1]):
                    continue
                if not(verif([i,k])):
                    print(str(i)+" , " + str(k) + " legal")
                    continue
                print(str(i)+" , " + str(k) + " Illegal")
        
    if side == "hd":
        if abs(pini[0]+pini[1])!=abs(pfin[0]+pfin[1]):
            return False
        for i in range(pfin[0],pini[0]):
            for k in range(pini[1]+1,pfin[1]+1):
                if abs(i+k)!=abs(pini[0]+pini[1]):
                    continue
                if not(verif([i,k])):
                    print(str(i)+" , " + str(k) + " legal")
                    continue
                print(str(i)+" , " + str(k) + " Illegal")

    if side == "bg":
        if abs(pini[0]+pini[1])!=abs(pfin[0]+pfin[1]):
            return False
        for i in range(pini[0]+1,pfin[0]+1):
            for k in range(pfin[1],pini[1]):
                if abs(i+k)!=abs(pini[0]+pini[1]):
                    continue
                if not(verif([i,k])):
                    print(str(i)+" , " + str(k) + " legal")
                    continue
                print(str(i)+" , " + str(k) + " Illegal")

    mouv(pini,pfin,n,"f")
    return True

def mouvpion(pini,pfin,n):

    if ((pini[1]+1==pfin[1] and pini[0]+1==pfin[0]) or (pini[1]-1==pfin[1] and pini[0]+1==pfin[0])) and (nottour in postovalue(pfin)):
        print("mange la piece en diagonale")
        mouv(pini,pfin,n,"p")
        return True
    if pini[0]+1==pfin[0] and pini[1]==pfin[1]:
        print("avance d'une case")
        mouv(pini,pfin,n,"p")
        return True
    if pini[0]+2==pfin[0] and pini[1]==pfin[1] and piece[postovalue(pini)]["moved?"]==False:
        print("avance de deux case")
        mouv(pini,pfin,n,"p")
        return True
    else:
        return False

def mouvroi(pini,pfin):
    if abs(pini[0]-pfin[0])<=1 and abs(pini[1]-pfin[1])<=1 and not(abs(pini[0]-pfin[0])==0 and abs(pini[1]-pfin[1])==0):
        print("avance le roi")
        mouv(pini,pfin,"","r")
        return True
    if pini[0]==pfin[0] and pini[1]-pfin[1]==2 and piece[tour+"r"]["moved?"]==False and piece[tour+"t1"]["moved?"]==False and postovalue([pini[0],pini[1]-1])=="" and postovalue([pini[0],pini[1]-2])=="": #vers la gauche
        print("roque a gauche")
        mouv(valuetopos(tour+"t1"),[valuetopos(tour+"t1")[0],valuetopos(tour+"t1")[1]+2],1,"r")
        mouv(pini,pfin,"","r")
        return True
    if pini[0]==pfin[0] and pini[1]-pfin[1]==-2 and piece[tour+"r"]["moved?"]==False and piece[tour+"t2"]["moved?"]==False and postovalue([pini[0],pini[1]+1])=="" and postovalue([pini[0],pini[1]+2])=="": #vers la droite
        print("roque a droite")
        mouv(valuetopos(tour+"t2"),[valuetopos(tour+"t2")[0],valuetopos(tour+"t1")[1]-2],2,"r")
        mouv(pini,pfin,"","r")
        return True
    return False

def mouvqueen(pini,pfin):
    side = wichside(pini,pfin) # detection du cote
    
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

    if side == "bd":
        if abs(pini[0]-pini[1])!=abs(pfin[0]-pfin[1]):
            return False
        for i in range(pini[0]+1,pfin[0]+1):
            for k in range(pini[1]+1,pfin[1]+1):
                if abs(i-k)!=abs(pini[0]-pini[1]):
                    continue
                if not(verif([i,k])):
                    print(str(i)+" , " + str(k) + " legal")
                    continue
                print(str(i)+" , " + str(k) + " Illegal")

    if side == "hg":
        if abs(pini[0]-pini[1])!=abs(pfin[0]-pfin[1]):
            return False
        for i in range(pfin[0],pini[0]):
            for k in range(pfin[1],pini[1]):
                if abs(i-k)!=abs(pini[0]-pini[1]):
                    continue
                if not(verif([i,k])):
                    print(str(i)+" , " + str(k) + " legal")
                    continue
                print(str(i)+" , " + str(k) + " Illegal")
        
    if side == "hd":
        if abs(pini[0]+pini[1])!=abs(pfin[0]+pfin[1]):
            return False
        for i in range(pfin[0],pini[0]):
            for k in range(pini[1]+1,pfin[1]+1):
                if abs(i+k)!=abs(pini[0]+pini[1]):
                    continue
                if not(verif([i,k])):
                    print(str(i)+" , " + str(k) + " legal")
                    continue
                print(str(i)+" , " + str(k) + " Illegal")

    if side == "bg":
        if abs(pini[0]+pini[1])!=abs(pfin[0]+pfin[1]):
            return False
        for i in range(pini[0]+1,pfin[0]+1):
            for k in range(pfin[1],pini[1]):
                if abs(i+k)!=abs(pini[0]+pini[1]):
                    continue
                if not(verif([i,k])):
                    print(str(i)+" , " + str(k) + " legal")
                    continue
                print(str(i)+" , " + str(k) + " Illegal")

    mouv(pini,pfin,"","q")
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

def printgame():
    print("--a-b-c-d-e-f-g-h--")
    nligne=8
    for line in game:
        ligne=f"{nligne}|"
        nligne-=1
        for piece in line:
            if "w" in piece:
                    if "t" in piece:
                        ligne=ligne+"♜ "
                    if "c" in piece:
                        ligne=ligne+"♞ "
                    if "f" in piece:
                        ligne=ligne+"♝ "
                    if "p" in piece:
                        ligne=ligne+"♟ "
                    if "r" in piece:
                        ligne=ligne+"♚ "
                    if "q" in piece:
                        ligne=ligne+"♛ "
            elif "b" in piece:
                    if "t" in piece:
                        ligne=ligne+"♖ "
                    if "c" in piece:
                        ligne=ligne+"♘ "
                    if "f" in piece:
                        ligne=ligne+"♗ "
                    if "p" in piece:
                        ligne=ligne+"♙ "
                    if "r" in piece:
                        ligne=ligne+"♔ "
                    if "q" in piece:
                        ligne=ligne+"♕ "
            else:
                ligne=ligne+"  "
        print(ligne+" "*(17-len(ligne)) +"|")
    print("-"*18)

def ask():
    x = input("Quel piece ?")
    y = input("Ou?")
    return (x,y)

def main():
    winner = False
    while winner==False:
        printgame()
        moov = ask()
        if deplacer(valuetopos(moov[0]),int(moov[1]))==False:
            print("Coup invalide !")
            continue
        tour, nottour = nottour, tour
    
    printgame()
    print(f"Les {nottour} gagne !")


if __name__ == "__main__":
    main()
    #printgame()
    #deplacer([5,0],[3,2])
    #print("\n")
    #printgame()
    #deplacer([3,2],[5,0])
    #print("\n")
    #printgame()
    #print(postovalue([7,7]))
    #for line in game : print(line)
    #print(piece)