import sys
orig_stdout = sys.stdout
f = file('ou.txt', 'w')
sys.stdout = f
def flip(l,x,y):
    l[x:y+1].reverse()
    for i in range(x,y+1,1):
        if l[i] == '-':
            l[i] = '+'
        else:
            l[i] = '-'

    return l
def check(n):
    l = []


    for j in range(len(n)):
        if n[j] == '-':
            l.append(j)
        else : break

    return l
def count(n):
    l = []


    for j in range(len(n)):
        if n[j] == '-':
            l.append(j)

    return l

for i in range(input()):
    n = list(raw_input())


    res = []
    j = 0
    while True:


        p = count(n)
        l = check(n)

        if l == [] and p == []:
            break
        else :
            if len(l) >= len(p) and l[0] == 0:


                n = flip(n[l[0]:l[-1]+1],l[0],l[-1]) + n[l[-1]+1:]

                j += 1
                continue
            else :

                n = flip(n[0:p[-1]+1],0,p[-1]) + n[p[-1]+1:]

                j += 1
                continue



    print "Case #%s: %s"%(i+1, j)

sys.stdout = orig_stdout
f.close()
