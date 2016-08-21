import re

def sleep(n):
    n=list(n)
    a=[]
    for x in l:
        c=n.count(x)
        for i in range(c):
            a.append(d[x][0])
            for j in d[x][1]:
                n.remove(j)
    return(''.join(map(str,sorted(a))))
        

l=list("ZXWSVUGTOI")
d={
    'Z':(0,"ZERO"), 'O':(1,"ONE"), 'W':(2,"TWO"), 'T':(3,"THREE"), 'U':(4,"FOUR"),
    'V':(5,"FIVE"), 'X':(6,"SIX"), 'S':(7,"SEVEN"), 'G':(8,"EIGHT"), 'I':(9,"NINE")
    }

inp=open("A-large.in")
inp.readline() #trusting all the lines in input are important
out=open("1la.txt","w")
case=1
for n in inp:
    out.write("Case #"+str(case)+": "+str(sleep(n[:-1]))+"\n")
    case+=1
inp.close()
out.close()
    
