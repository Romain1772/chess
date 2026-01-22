


# initialisation de la game
game = [ 
    ["bt1","bc1","bf1","bq","br","bf2","bc2","bt2"], # p pion 1,2,3,4,5,6,7,8
    ["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"], # t tour 1 et 2
    ["","","","","","","",""],                 # c cavalier 1 et 2
    ["","","","","","","",""],                 # f fou 1 et 2
    ["","","","","","","",""],                 # r roi
    ["","","","","","","",""],                 # q reine
    ["wp1","wp2","wp3","wp4","wp5","wp6","wp7","wp8"], # b noir
    ["wt1","wc1","wf1","wq","wr","wf2","wc2","wt2"]  # w blanc
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
    return game[pos[0]-1][pos[1]-1]

def wichside(pini,pfin):                     #8 cas differend   hg h hd
    if pini[0]==pfin[0] and pini[1]<pfin[1]: # meme ligne        g P  d
        return "d"                           #                  bg b bd
    if pini[1]==pfin[1] and pini[0]<pfin[0]:
        return "h"
    if pini[0]==pfin[0] and pini[1]>pfin[1]:
        return "g"
    if pini[1]==pfin[1] and pini[0]>pfin[0]:
        return "b"
    if pini[0]<pfin[0] and pini[1]<pfin[1]:
        return "hd"
    if pini[0]<pfin[0] and pini[1]>pfin[1]:
        return "hg"
    if pini[0]>pfin[0] and pini[1]>pfin[1]:
        return "bg"
    if pini[0]>pfin[0] and pini[1]<pfin[1]:
        return "bd"

def verif(pos):
    if game[pos[0]-1][pos[1]+1]=="": return False
    elif nottour in game[pos[0]-1][pos[1]+1]: return False
    else: return True

def mouvtour(pini,pfin,n):
    side = wichside(pini,pfin)
    print(side)
    if side == "d" or side == "g":
        for i in range:
            #verif([,])
            pass


    game[pini[0]-1][pini[1]-1]=""
    game[pfin[0]-1][pfin[1]-1]=tour+"t"+str(n)
    pass

def deplacer(pini,pfin): # return false si le mouvement est impossible pini et pfin systeme de liste 1*1 a 8*8
    if pini==pfin:
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
        mouvtour(pini,pfin,n)
    if "c" in piece:
        mouvcavalier(pini,pfin,n)
    if "f" in piece:
        mouvfou(pini,pfin,n)
    if "p" in piece:
        mouvpion(pini,pfin,n)
    if "r" in piece:
        mouvroi(pini,pfin)
    if "q" in piece:
        mouvqueen(pini,pfin)
        pass




if __name__ == "__main__":
    for line in game : print(line)
    mouvtour([8,1],[5,5],1)
    for line in game : print(line)
    #print(postovalue([7,7]))
    #for line in game : print(line)
    #print(piece)