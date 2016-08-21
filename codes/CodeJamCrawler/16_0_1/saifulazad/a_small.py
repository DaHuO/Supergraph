from collections import defaultdict


def C(n):

    if n == 0:
        return 'INSOMNIA'
    else:

        digit = defaultdict(int)
        x = 1
        while x>=1:

            al = str(x*n)

            for dig in al:
                digit[dig]+=1

            if len(digit) == 10:
                return al

            x = x+1




read = open('Al.in','r')
writ = open('o.txt','w')
test = int(read.readline())

l = [(int(read.readline())) for x in range(test)]

#print l
for (i, n) in enumerate(l,1):

    s = 'Case #{0}: {1}\n'.format(i,C(n))
    writ.writelines(s)