## Définition des fonctions

# Convertir une liste en un entier (ex: [1,5,6]-->156)
def entier(L):
    a=''
    for k in L:
        a+=str(k)
    return int(a)

# Convertir une chaine de caractère avec un \n à la fin en une liste de nombre (ex: '156\n'-->[1,5,6])
def convert(N):
    L=list(str(N))
    M=L.copy()
    for k in range(len(L)):
        if L[k]!='\n':
            M[k]=int(M[k])
        else:
            M.remove('\n')
    return M

# Convertir une liste avec plusieurs occurence du meme nombre en un liste épurée (ex: [1,2,1,1,2]-->[1,2])
def redondant(L):
    k=0
    while k<len(L):
        a=L[k]
        s=0
        for i in range(len(L)):
            if a==L[i]:
                s+=1
        for j in range(s-1):
            L.remove(a)
        k+=1
    return L

# Fonction principale
def dream(N):                   # N=chaine de caractère avec un \n à la fin
    N=entier(convert(N))        # Permet de convertir en un chiffre (en enlevant le \n)
    L=redondant(convert(N))
    if L==[0]:
        return 'INSOMNIA'
    k=2
    while len(L)!=10:
        S=N*k
        M=convert(S)
        for i in range(len(M)):
            s=0
            for j in range(len(L)):
                if M[i]==L[j]:
                    s+=1
            if s==0:
                L.append(M[i])
        k+=1
    return S


## Traitement des fichiers d'entrée et de sortie

fichier=open('F:\Prog\Python\Textes Jam\Entrée\Jam2.in','r')
A=int(fichier.readline())

sortie=open('F:\Prog\Python\Textes Jam\Sortie\Jam2.txt','w')

P=[]
for k in range(A):
    P.append(fichier.readline())

for k in range(len(P)):
    sortie.write('Case #'+str(k+1)+': '+str(dream(P[k]))+'\n')

fichier.close()
sortie.close()