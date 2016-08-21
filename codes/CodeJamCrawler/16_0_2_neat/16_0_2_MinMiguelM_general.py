filenameInput = "B-large.in"
filenameOutput = "B-large.out"

sides = dict({'-':'+','+':'-'})

def flip(S,j):
    str = ''
    SS = S[:j]
    SS.reverse()
    for i in range(len(SS)):
        str = SS[i]
        SS[i] = sides[str]
    return SS+S[j:]

def happySide(S):
    for i in S:
        if i == '-':
            return False
    return True

def maneuver(S):
    count = 0
    if len(S)==1:
        return 0 if S[0] == '+' else 1
    else:
        while happySide(S) == False:
            j = len(S)
            for i in range(len(S)-1):
                if S[i] != S[i+1]:
                    j = i+1
                    break;
            S = flip(S,j)
            count+=1
    return count

def loadFile():
    f = open(filenameInput,"r")
    tc = int(f.readline())
    string=""
    i=1
    while(i<=tc):
        S = list(f.readline())
        c = maneuver(S if S[len(S)-1] != '\n' else S[:len(S)-1])
        string += "Case #"+str(i)+": "+str(c)+"\n" if i<tc else "Case #"+str(i)+": "+str(c)
        i+=1
    saveFile(string)
    f.close()

def saveFile(string):
    f = open(filenameOutput,"w")
    #f.write("Case #",x,": ",y, )
    f.write(string)
    f.close()

loadFile()
