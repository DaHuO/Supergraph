# Code Jam: Counting Sheep
out=open('output.txt', 'w+')

def find_dig(dig):
    if dig in lis:
        if sum(lis)==45 and 0 in lis: return True
        else: return False  
    else:
        lis.append(dig)
        if sum(lis)==45 and 0 in lis: return True
        else: return False


def digits(x):
    for i in xrange(1,99999999):
        num = x*i
        num = str(num)
        #print num
        for j in num:
            dig = int(j)
            #print j
            if find_dig(dig) : break
        if find_dig(dig) : break
    j = "\nCase #{}: {}".format(c, num)
    out.write(j)

ans=[]
lis = []
f=open('A-large.in','r')
count=0
c=1
for k in f:
    lis = []
    if count==0:
        tc = int(k)
        count=count+1
        continue
    x = int(k)
    if x==0:
        j = "Case #{}: {}".format(c, "INSOMNIA")
        out.write(j)
        c+=1
        continue
    digits(x)
    c+=1


out.close()
