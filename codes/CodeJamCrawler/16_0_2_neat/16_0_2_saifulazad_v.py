__author__ = 'Azad'

def XD(l):
    c =0
    r = l[::-1]

    if r[0] =='-':
        c+=1
    for x in range(1,len(r)):
        if r[x] !=r[x-1]:
            c+=1

    return c

read = open('Bl.in','r')
writ = open('o.txt','w')
test = int(read.readline())

l = [((read.readline())).strip() for x in range(test)]



for (i, n) in enumerate(l,1):


    s = 'Case #{0}: {1}\n'.format(i,XD(n))
    writ.writelines(s)
