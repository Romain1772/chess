import copy


# initialisation de la game
game = [ 
    ["bt1","bc1","bf1","bq","br","bf2","bc2","bt2"], # p pion 1,2,3,4,5,6,7,8    1  postion : [n°ligne,n° collone]
    ["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"], # t tour 1 et 2           2 
    ["","","","","","","",""],                 # c cavalier 1 et 2               3
    ["","","","","","","",""],                 # f fou 1 et 2                    4
    ["","","","","","","",""],                 # r roi                           5
    ["","","","","","","",""],                 # q reine                         6
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

def maxn(t,name):
    max=1
    for i in dicoPiece.keys():
        if t in i and name in i:
            try:
                if int(i[2])>max:
                    max=int(i[2])
            except:
                pass
    return max

def mouv(pini,pfin,n,name,real=True):
    dif=pfin[1]-pini[1]
    if name=="r" and abs(dif)>1:#cas du roque
        if dif<0:#vers la gauche
            mouv(valuetopos(tour+"t1"),(pini[0],pini[1]-1),1,"t")
        else:
            mouv(valuetopos(tour+"t2"),(pini[0],pini[1]+1),1,"t")
    updatedico(pini,pfin)
    if real and name=="p" and (pfin[0]==0 or pfin[0]==7):#cas de la promotion
        del dicoPiece[game[pfin[0]][pfin[1]]]
        game[pini[0]][pini[1]]=""
        name=input("Quel piece est promu?(q/c/f/t)")
        n=maxn(tour,name)+1
        game[pfin[0]][pfin[1]]=tour+name+str(n)
        dicoPiece[tour+name+str(n)]["position"] = pfin
        dicoPiece[tour+name+str(n)]["moved?"] = True
        return
    dif=pfin[0]-pini[0]
    if real and name == "p" and abs(dif)==2:#avance de deux case par pion
        if dif<0:#blanc
            game[pini[0]-1][pini[1]]="."
        else:
            game[pini[0]+1][pini[1]]="."
    
    if postovalue(pfin)==".":#prise en passant
        del dicoPiece[game[pini[0]][pfin[1]]]
        game[pini[0]][pfin[1]]=""

    if game[pfin[0]][pfin[1]] != "":
        del dicoPiece[game[pfin[0]][pfin[1]]]
    game[pini[0]][pini[1]]="" # on enleve la piece
    if n==False: n=""
    game[pfin[0]][pfin[1]]=tour+name+str(n) # on remet la piece
    

def coupPossible(pini):
    piece = postovalue(pini)
    cpPossible=[]
    
    tmpTour = "b" if "b" in piece else "w"
    tmpNotTour = "w" if tmpTour == "b" else "b"

    def horsBoard(pos):
        if 0<=pos[0]<=7 and 0<=pos[1]<=7: return True
        else: return False

    if "c" in piece:
        for i in [(2, 1), (1, 2), (-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2)]:
            pos=adder(pini,i[0],i[1])
            if horsBoard(pos):
                pTest=postovalue(pos)
                if "" == pTest or tmpNotTour in pTest or "."==pTest:
                    cpPossible.append(pos)
            else:
                pass
    if "q" in piece or "f" in piece:
        for i in [(1,1), (1,-1), (-1,1), (-1,-1)]:
            coef=0
            while True:
                coef+=1
                vect=multi(i,coef)
                pos=adder(pini,vect[0],vect[1])
                if horsBoard(pos):
                    pTest=postovalue(pos)
                    if "" == pTest or "."==pTest:
                        cpPossible.append(pos)
                    elif tmpNotTour in pTest:
                        cpPossible.append(pos)
                        break
                    else:
                        break
                else:
                    break
    if "q" in piece or "t" in piece:
        for i in [(1,0), (-1,0), (0,1), (0,-1)]:
            coef=0
            while True:
                coef+=1
                vect=multi(i,coef)
                pos=adder(pini,vect[0],vect[1])
                if horsBoard(pos):
                    pTest=postovalue(pos)
                    if "" == pTest or "."==pTest:
                        cpPossible.append(pos)
                    elif tmpNotTour in pTest:
                        cpPossible.append(pos)
                        break
                    else:
                        break
                else:
                    break
    if "r" in piece:
        for i in [adder(pini,0,1),adder(pini,0,-1),adder(pini,-1,0),adder(pini,1,0),adder(pini,1,1),adder(pini,-1,-1),adder(pini,1,-1),adder(pini,-1,1)]:
            if horsBoard(pos):#au cas ou hors du board
                if tmpNotTour in postovalue(i) or "" == postovalue(i) or "." ==postovalue(i):
                    cpPossible.append(i)
            else:
                pass
        #roque:
        if dicoPiece[tmpTour+"r"]["moved?"]==False:
            if dicoPiece[tmpTour+"t1"]["moved?"]==False and (game[pini[0]][pini[1]-1]=="" and game[pini[0]][pini[1]-2]=="" and game[pini[0]][pini[1]-3]==""):
                cpPossible.append([pini[0],2])
            if dicoPiece[tmpTour+"t2"]["moved?"]==False and (game[pini[0]][pini[1]+1]=="" and game[pini[0]][pini[1]+2]==""):
                cpPossible.append([pini[0],6])
                
    
    if "p" in piece:
        posEv=(adder(pini,1,1),adder(pini,1,-1),adder(pini,-1,1),adder(pini,-1,-1),)
        if tmpTour=="b":
            for i in posEv[0:2]:
                if horsBoard(pos):
                    if "w" in postovalue(i) or "."==pTest:
                        cpPossible.append(i)
                else:
                    pass
        if tmpTour=="w":
            for i in posEv[2:4]:
                if horsBoard(pos):
                    if "b" in postovalue(i) or "."==pTest:
                        cpPossible.append(i)
                else:
                    pass
        if dicoPiece[piece]["moved?"]==False:
            if tmpTour=="w":
                cpPossible.append(adder(pini,-2,0))
            if tmpTour=="b":
                cpPossible.append(adder(pini,2,0))

        if "" == postovalue(adder(pini,1,0)) and "b" in piece :
            cpPossible.append(adder(pini,1,0))
        if "" == postovalue(adder(pini,-1,0)) and "w" in piece:
            cpPossible.append(adder(pini,-1,0))
    return cpPossible

def removePoint():
    global game
    for i in range(0,8):
        if game[2][i]==".": game[1][i]==""
    for i in range(0,8):
        if game[5][i]==".": game[6][i]==""

def ischeck(t,posRoi=False):
    '''t -> b/w la personne qui doit etre vérifié, es que t est en echec? retourne true (echec) / false (pas echec)'''
    if t=="b": nt="w"
    else: nt="b"
    if posRoi==False: posRoi=valuetopos(t+"r")
    for i in dicoPiece.keys():
        if nt in i:
            if posRoi in coupPossible(valuetopos(i)):
                return True
    return False

def ismate(t):
    '''t -> b/w la personne qui doit etre vérifié, es que t est en echec et mat? retourne true (echec) / false (pas echec)'''
    global game
    global dicoPiece
    posRoi=valuetopos(t+"r")
    if ischeck(t):
        for i in list(dicoPiece.keys()):
            if t in i:
                for k in coupPossible(valuetopos(i)):
                    try:
                        n=i[2]
                    except:
                        n=False
                    tempGame=copy.deepcopy(game)
                    tempdicoPiece=copy.deepcopy(dicoPiece)
                    mouv(valuetopos(i),k,n,i[1],False)
                    test = ischeck(t)
                    game = copy.deepcopy(tempGame)
                    dicoPiece=copy.deepcopy(tempdicoPiece)
                    if test==False: return False
        return True
    return False

def ispat(t):
    ''' '''
    global game
    global dicoPiece
    posRoi=valuetopos(t+"r")
    if not(ischeck(t)):
        for i in list(dicoPiece.keys()):
            if t in i:
                for k in coupPossible(valuetopos(i)):
                    try:
                        n=i[2]
                    except:
                        n=False
                    tempGame=copy.deepcopy(game)
                    tempdicoPiece=copy.deepcopy(dicoPiece)
                    mouv(valuetopos(i),k,n,i[1],False)
                    test = ischeck(t)
                    game = copy.deepcopy(tempGame)
                    dicoPiece=copy.deepcopy(tempdicoPiece)
                    if test==False: return False
        return True
    return False

def deplacer(pini,pfin): # return false si le mouvement est impossible pini et pfin systeme de liste 1*1 a 8*8
    global game
    global dicoPiece
    if pini==pfin: #verif si meme postion avant et apres
        return False
    piece=postovalue(pini)
    # detection du numéro de piece
    try:
        n=piece[2]
    except:
        n=False
    
    if tour not in piece:  # verification si c'est le bon joueur
        return False
    if pfin not in coupPossible(pini):
        return False
    
    tempGame=copy.deepcopy(game)
    tempdicoPiece=copy.deepcopy(dicoPiece)
    mouv(pini,pfin,n,piece[1])
    test = ischeck(tour)
    game = copy.deepcopy(tempGame)
    dicoPiece=copy.deepcopy(tempdicoPiece)
    if test==True: return False

    mouv(pini,pfin,n,piece[1])
    return True

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
        pat=ispat(tour)
        if pat!=False:
            if pat=="b":
                print(f"Les noirs sont en pat !")
            else:
                print(f"Les blanc sont en pat !")
            break
        if ismate(tour):
            print(f"Les {nottour} gagne !")
            break
        removePoint()
    printgame()


if __name__ == "__main__":
    main()