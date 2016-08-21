import sys

def finito(s):
    ris = True
    for j in range(len(s)):
        if s[j][0] != 0:
            return False
    return True
def errore(s,t):
    for j in range(len(s)):
        if s[j][0] > t / 2:
            return True
    return False
def Esegui(s,t):
    evac = ""
    s.sort(reverse=True)
    if t % 2 != 0:
        s[0][0] = s[0][0] - 1
        evac =evac + s[0][1]+" "
        t -=1
    s.sort(reverse=True)
    while not(finito(s)):
        evac = evac + s[0][1] + s[1][1]+" "
        s[0][0] = s[0][0] - 1
        s[1][0] = s[1][0] - 1
        t -=2
        s.sort(reverse=True)
        if errore(s,t):
            return "Accidenti"
##        print evac, s 
    evac= evac[:-1]
    return evac

alph = "A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z"
alph = alph.split()
##print alph
sys.stdin=open('data.txt')
foutput = open('output.txt','w')
T=input()
risultato =""
for t in range(1,int(T)+1):
    N = int(input())
##    print N
    data = raw_input()
    if data[-1] == "\n":
        data = data[:-1].split()
    else:
        data = data.split()
    sen = []
    tot = 0
    for k in range(N):
        tot +=int(data[k])
        sen.append([int(data[k]), alph[k]])
##    if t == 6:
##        sen.sort(reverse=True)
##        print sen
##        break
    #print  "Case #" + str(t)+": "+Esegui(sen,tot) + "\n" 
    risultato = risultato +  "Case #" + str(t)+": "+Esegui(sen,tot) + "\n"
foutput.write(risultato[:-1])
foutput.close()
