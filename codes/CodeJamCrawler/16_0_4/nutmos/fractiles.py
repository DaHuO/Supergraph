test = int(raw_input())

def liststr(lista):
    return " ".join((str(lista)[1:-1]).split(", "))
import math
for II in range(1,test+1):
    s = raw_input().split(" ")
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    if a == c:
        listans = range(1,a+1)
        for i in range(2,b+1):
            for j in range(i-1,len(listans)):
                listans[j] += (j-i+1)*int(math.pow(a,i-1))
            #print listans
        if b >= a:
            print "Case #" + str(II) + ": " + str(listans[len(listans)-1])
        else:
            print "Case #" + str(II) + ": " + liststr(listans[b-1:len(listans)])
