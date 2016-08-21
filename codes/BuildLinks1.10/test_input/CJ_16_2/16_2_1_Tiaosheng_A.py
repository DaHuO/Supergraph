f = open('A-small-attempt0.in', 'r')
f2 = open('A-small-attempt0.out', 'w')
"""
f = open('A-large.in', 'r')
f2 = open('A-large.out', 'w')

n=int(f.readline())
t=[int(i) for i in file.readline().split()]
"""
n=int(f.readline())
l=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]

def fun(mot,tab):
    if not mot:
        return(tab)
    for i in range(10):
        if (sum([int(l[i].count(c) <= mot.count(c)) for c in l[i]]))==len(l[i]):
            #print(mot,i)
            t=[e for e in tab]
            t[i]+=1
            m=[e for e in mot]
            for e in l[i]:
                #print(e,m)
                m.remove(e)
            x=fun(m,t)
            if x:
                return(x)

for i in range(n):

    mot=str(f.readline()[:-1])
    #print(mot)
    tab=fun(mot,[0]*10)
    x=""
    for j in range(10):
        x+=str(j)*tab[j]
    f2.write("Case #"+str(i+1)+": "+str(x)+"\n")
