import copy


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

dicoPiece = {}
tour="w" # defini le début du tour au blanc
nottour="b"

ligne=-1
for line in game:  #definir les position des piece
    ligne+=1
    collone=-1
    for p in line:
        collone+=1
        if "p" in p:
            dicoPiece[p]={
                "position":[ligne,collone],
                "moved?":False
            }
        if "t" in p:
            dicoPiece[p]={
                "position":[ligne,collone],
                "moved?":False
            }
        if "c" in p:
            dicoPiece[p]={
                "position":[ligne,collone]
            }
        if "f" in p:
            dicoPiece[p]={
                "position":[ligne,collone]
            }
        if "r" in p:
            dicoPiece[p]={
                "position":[ligne,collone],
                "moved?":False
            }
        if "q" in p:
            dicoPiece[p]={
                "position":[ligne,collone]
            }
        else:
            pass


def postovalue(pos):
    return game[pos[0]][pos[1]]

def valuetopos(value):
    return dicoPiece[value]["position"]

def chesstogame(ch):
    '''Transcris une postion d'echec en postion sur le board'''
    v1=0
    for i in ["a","b","c","d","e","f","g","h"]:
        if ch[0] == i:
            break
        v1+=1
    v2=0
    for i in ["8","7","6","5","4","3","2","1"]:
        if ch[1] == i:
            break
        v2+=1
    return [v2,v1]

def gametochess(pos):
    '''a faire au besoin'''
    pass

def updatedico(pini,pfin):
    p=postovalue(pini)
    dicoPiece[p]["position"] = pfin
    dicoPiece[p]["moved?"] = True

def adder(pos,xadd,yadd):
    return (pos[0]+xadd,pos[1]+yadd)

def multi(pos,coef):
    return (pos[0]*coef,pos[1]*coef)

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

def verif(pos):# renvoie True si le mouv est impossible si la case est non vide avec sa propre equipe ne verifie pas la faisabilité
    print(pos)
    if game[pos[0]][pos[1]]=="": return False
    elif nottour in game[pos[0]][pos[1]]: return False
    else: return True

def mouv(pini,pfin,n,name,real=True):
    if real==False:
        return
    
    updatedico(pini,pfin)
    if game[pfin[0]][pfin[1]] != "":
        del dicoPiece[game[pfin[0]][pfin[1]]]
    game[pini[0]][pini[1]]="" # on enleve la piece
    game[pfin[0]][pfin[1]]=tour+name+str(n) # on remet la piece

def mouvtour(pini,pfin,n,real=True):
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

    mouv(pini,pfin,n,"t",real)
    return True

def mouvcavalier(pini,pfin,n,real=True):
    if verif(pfin) or (pfin[0]-pini[0])**2+(pfin[1]-pini[1])**2!=5:
        print(str(pfin[0])+" , " + str(pfin[1]) + " Illegal")
        return False
    print(str(pfin[0])+" , " + str(pfin[1]) + " legal")

    mouv(pini,pfin,n,"c",real)
    return True

def mouvfou(pini,pfin,n,real=True):
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

    mouv(pini,pfin,n,"f",real)
    return True

def mouvpion(pini,pfin,n,real=True):
    def promo(real=True):
        if real==True: return
        if pfin[0]==0 or pfin[0]==7:
            ndicoPiece=input("Vers quel piece promouvoir?(f/q/t/c)")
            maxx=0
            for i in dicoPiece:
                if ndicoPiece in i and tour in i:
                    try:
                        if maxx<i[3]:
                            maxx=i[3]
                    except:
                        pass

            del dicoPiece[game[pfin[0]][pfin[1]]]

            game[pfin[0]][pfin[1]]=tour+ndicoPiece+str(maxx+1)

            
            p=postovalue(pfin)
            dicoPiece[p]["position"] = pfin
            dicoPiece[p]["moved?"] = True
                            

            
    if tour == "b":
        if ((pini[1]+1==pfin[1] and pini[0]+1==pfin[0]) or (pini[1]-1==pfin[1] and pini[0]+1==pfin[0])) and (nottour in postovalue(pfin)):
            print("mange la dicoPiece en diagonale")
            mouv(pini,pfin,n,"p",real)
            promo(real)
            return True
        if pini[0]+1==pfin[0] and pini[1]==pfin[1] and postovalue(pfin)=="":
            print("avance d'une case")
            mouv(pini,pfin,n,"p",real)
            promo(real)
            return True
        if pini[0]+2==pfin[0] and pini[1]==pfin[1] and postovalue([pfin[0]-1,pfin[1]])=="" and dicoPiece[postovalue(pini)]["moved?"]==False and postovalue(pfin)=="":
            print("avance de deux case")
            mouv(pini,pfin,n,"p",real)
            promo(real)
            return True
        else:
            return False
    else:
        if ((pini[1]-1==pfin[1] and pini[0]+1==pfin[0]) or (pini[1]+1==pfin[1] and pini[0]+1==pfin[0])) and (nottour in postovalue(pfin)):
            print("mange la dicoPiece en diagonale")
            mouv(pini,pfin,n,"p",real)
            promo(real)
            return True
        if pini[0]-1==pfin[0] and pini[1]==pfin[1] and postovalue(pfin)=="":
            print("avance d'une case")
            mouv(pini,pfin,n,"p",real)
            promo(real)
            return True
        if pini[0]-2==pfin[0] and pini[1]==pfin[1] and postovalue([pfin[0]+1,pfin[1]])=="" and dicoPiece[postovalue(pini)]["moved?"]==False and postovalue(pfin)=="":
            print("avance de deux case")
            mouv(pini,pfin,n,"p",real)
            promo(real)
            return True
        else:
            return False

def mouvroi(pini,pfin,real=True):
    if abs(pini[0]-pfin[0])<=1 and abs(pini[1]-pfin[1])<=1 and not(abs(pini[0]-pfin[0])==0 and abs(pini[1]-pfin[1])==0):
        print("avance le roi")
        mouv(pini,pfin,"","r",real)
        return True
    if pini[0]==pfin[0] and pini[1]-pfin[1]==2 and dicoPiece[tour+"r"]["moved?"]==False and dicoPiece[tour+"t1"]["moved?"]==False and postovalue([pini[0],pini[1]-1])=="" and postovalue([pini[0],pini[1]-2])=="": #vers la gauche
        print("roque a gauche")
        mouv(valuetopos(tour+"t1"),[valuetopos(tour+"t1")[0],valuetopos(tour+"t1")[1]+2],1,"r")
        mouv(pini,pfin,"","r",real)
        return True
    if pini[0]==pfin[0] and pini[1]-pfin[1]==-2 and dicoPiece[tour+"r"]["moved?"]==False and dicoPiece[tour+"t2"]["moved?"]==False and postovalue([pini[0],pini[1]+1])=="" and postovalue([pini[0],pini[1]+2])=="": #vers la droite
        print("roque a droite")
        mouv(valuetopos(tour+"t2"),[valuetopos(tour+"t2")[0],valuetopos(tour+"t1")[1]-2],2,"r")
        mouv(pini,pfin,"","r",real)
        return True
    return False

def mouvqueen(pini,pfin,real=True):
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

    mouv(pini,pfin,"","q",real)
    return True

def coupPossible(pini):
    piece = postovalue(pini)
    cpPossible=[]
    if "b" in piece:
        tour="b"
        nottour="w"
    else:
        tour="w"
        nottour="b"
    if "c" in piece:
        for i in [(2, 1), (1, 2), (-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2)]:
            pos=adder(pini,i[0],i[1])
            try:
                pTest=postovalue(pos)
                if "" == pTest or nottour in pTest:
                    cpPossible.append(pos)
            except:
                pass
    if "q" in piece or "f" in piece:
        for i in [(1,1), (1,-1), (-1,1), (-1,-1)]:
            coef=0
            while True:
                coef+=1
                vect=multi(i,coef)
                pos=adder(pini,vect[0],vect[1])
                try:
                    pTest=postovalue(pos)
                    if "" == pTest:
                        cpPossible.append(pos)
                    elif nottour in pTest:
                        cpPossible.append(pos)
                        break
                    else:
                        break
                except:
                    break
    if "q" in piece or "t" in piece:
        for i in [(1,0), (-1,0), (0,1), (0,-1)]:
            coef=0
            while True:
                coef+=1
                vect=multi(i,coef)
                pos=adder(pini,vect[0],vect[1])
                try:
                    pTest=postovalue(pos)
                    if "" == pTest:
                        cpPossible.append(pos)
                    elif nottour in pTest:
                        cpPossible.append(pos)
                        break
                    else:
                        break
                except:
                    break
    if "r" in piece:
        for i in [adder(pini,0,1),adder(pini,0,-1),adder(pini,-1,0),adder(pini,1,0),adder(pini,1,1),adder(pini,-1,-1),adder(pini,1,-1),adder(pini,-1,1)]:
            try:#au cas ou hors du board
                if nottour in postovalue(i) or "" == postovalue(i):
                    cpPossible.append(i)
            except:
                pass
        #roque:
        if dicoPiece[tour+"r"]["moved?"]==False:
            if dicoPiece[tour+"t1"]["moved?"]==False and (game[pini[0]][pini[1]-1]=="" and game[pini[0]][pini[1]-2]=="" and game[pini[0]][pini[1]-3]==""):
                cpPossible.append([pini[0],2])
            if dicoPiece[tour+"t2"]["moved?"]==False and (game[pini[0]][pini[1]+1]=="" and game[pini[0]][pini[1]+2]==""):
                cpPossible.append([pini[0],6])
                
    
    if "p" in piece:
        posEv=(adder(pini,1,1),adder(pini,1,-1),adder(pini,-1,1),adder(pini,-1,-1),)
        if tour=="b":
            for i in posEv[0:2]:
                try:
                    if "w" in postovalue(i):
                        cpPossible.append(i)
                except:
                    pass
        if tour=="w":
            for i in posEv[2:4]:
                try:
                    if "b" in postovalue(i):
                        cpPossible.append(i)
                except:
                    pass

        if "" == postovalue(adder(pini,1,0)) and "b" in piece :
            cpPossible.append(adder(pini,1,0))
        if "" == postovalue(adder(pini,-1,0)) and "w" in piece:
            cpPossible.append(adder(pini,-1,0))
    return cpPossible


def ischeck(t):
    '''t -> b/w la personne qui doit etre vérifié, es que t est en echec? retourne true (echec) / false (pas echec)'''
    global game
    global dicoPiece
    nt="b" 
    if t=="b": nt = "w"
    tempGame=copy.deepcopy(game)
    tempdicoPiece=copy.deepcopy(dicoPiece)

    for i in dicoPiece.keys():
        if nt in i:
            if deplacer(dicoPiece[i]["position"],dicoPiece[t+"r"]["position"],real=False):
                return True
            game = copy.deepcopy(tempGame)
            dicoPiece=copy.deepcopy(tempdicoPiece)

    return False


def deplacer(pini,pfin,real=True): # return false si le mouvement est impossible pini et pfin systeme de liste 1*1 a 8*8
    if pini==pfin: #verif si meme postion avant et apres
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
    
    if tour not in piece and real:  # verification si c'est le bon joueur
        return False
    
    if "t" in piece:
        return mouvtour(pini,pfin,n,real)
    if "c" in piece:
        return mouvcavalier(pini,pfin,n,real)
    if "f" in piece:
        return mouvfou(pini,pfin,n,real)
    if "p" in piece:
        return mouvpion(pini,pfin,n,real)
    if "r" in piece:
        return mouvroi(pini,pfin,real)
    if "q" in piece:
        return mouvqueen(pini,pfin,real)

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
    x = input("De ?")
    y = input("A ?")
    return (x,y)

def main():
    global tour
    global nottour
    winner = False
    while winner==False:
        printgame()
        moov = ask()
        if deplacer(chesstogame(moov[0]),chesstogame(moov[1]))==False:
            print("Coup invalide !")
            continue
        tour, nottour = nottour, tour
    
    printgame()
    print(f"Les {nottour} gagne !")


if __name__ == "__main__":
    main()