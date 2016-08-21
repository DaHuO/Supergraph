ind = open("B-large.in", "r")
outd = open("B-large.out", "w")

T = int(ind.readline())

def flip(S, idx):
    S_ = ""
    for i in range(len(S)):
        if i >= idx:
            S_ += (S[i])
        elif S[i] == "-":
            S_ += "+"
        else:
            S_ += "-"
    return S_

for i in range(1, T+1):
    S = ind.readline().strip()
    
    flips = 0
    solved = False
    
    while solved == False:
        try:
            p = S.index("-")
            if p>0:
                flips += 1
                S = flip(S,p)
            else:
                flips += 1
                S = flip(S,S.rindex("-")+1)
        except ValueError:
            solved = True
        
    print("Case #"+str(i)+": "+str(flips)+"\n")
    outd.write("Case #"+str(i)+": "+str(flips)+"\n")

ind.close()
outd.close()

