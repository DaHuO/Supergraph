def deletion(case, s, nbr):
    new_case = list(case)
    new_dico = {}
    #print("."+str(nbr))
    #print("."+s)
    while nbr > 0:
        #print("-"+str(new_case))
        for l in s:
            index = new_case.index(l)
            new_case.pop(index)
        nbr -= 1
    dico = {}
    for i in range(ord('A'),ord('Z')+1):
        dico[chr(i)]=0
    for l in new_case:
        dico[l] += 1
    return new_case, dico

def solve(case):
    res = {}
    for i in range(10):
        res[i] = 0
    dico = {}
    for i in range(ord('A'),ord('Z')+1):
        dico[chr(i)]=0
    for l in case:
        dico[l] += 1

    while len(case) > 0:
        if dico['Z']>0:
            res[0]=dico['Z']
            case, dico = deletion(case,"ZERO", res[0])
        elif dico['X']>0:
            res[6]=dico['X']
            case, dico = deletion(case,"SIX", res[6])
        elif dico['W']>0:
            res[2]=dico['W']
            case, dico = deletion(case,"TWO", res[2])
        elif dico['U']>0:
            res[4]=dico['U']
            case, dico = deletion(case,"FOUR", res[4])
        elif dico['O']>0:
            res[1]=dico['O']
            case, dico = deletion(case,"ONE", res[1])
        elif dico['R']>0:
            res[3]=dico['R']
            case, dico = deletion(case,"THREE", res[3])
        elif dico['S']>0:
            res[7]=dico['S']
            case, dico = deletion(case,"SEVEN", res[7])
        elif dico['V']>0:
            res[5]=dico['V']
            case, dico = deletion(case,"FIVE", res[5])
        elif dico['N']>0:
            res[9]=int(dico['N']/2)
            case, dico = deletion(case,"NINE", res[9])
        elif dico['H']>0:
            res[8]=dico['H']
            case, dico = deletion(case,"EIGHT", res[8])


    s_res = ""
    #print(res)
    for r in res:
        if res[r]>0:
            s_res += str(r)*res[r]
    return s_res 
t= int(input())
for i in range(1,t+1):
    case = input()
    #print(case+"\n")
    print("Case #"+str(i)+": "+solve(case))
#C, d = deletion("AABBCCDDEEFF", "BCD", 2)
#Print(c)
