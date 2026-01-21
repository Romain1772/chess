


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
tour="w"

for line in game:
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
    return game[int(pos/10)-1][pos-10*(int(pos/10))-1]

def mouvtour():
    if 

def deplacer(pini,pfin): # return false si le mouvement est impossible pini et pfin systeme de 1*1 a 8*8
    piece=postovalue(pini)
    if "1" in piece:
        n=1
    if "2" in piece:
        n=2
    if tour not in piece:  # verification si c'est le bon joueur
        return False
    if "t" in piece:
        mouvtour(pini,pfin,n)
        pass




if __name__ == "__main__":
    #for line in game : print(line)
    #print(piece)