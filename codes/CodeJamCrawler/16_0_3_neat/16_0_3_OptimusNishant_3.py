def sol():
    b = []
    for i in xrange(32768,65536,2):
        k = str(bin(i))[3:-1]
        l = len(k)
        s = "1"+k+"1"
        temp = ""
        for ch in s:
            temp=temp+ch*2
        b.append(temp)
    return b

'''
def getdivisor(s,n):
    v = 0
    i=0
    for ch in s:
        v+=int(ch)*(n**i)
        i+=1
    d = 2
    while (v%d!=0):
        d+=1
    return d
'''

def main():
    k = input()
    n, j = map(int, raw_input().split())
    print "Case #1:"
    l = [3,4,5,6,7,8,9,10,11]
    c=0
    for item in sol():
        if c==500:
            break
        print item, " ".join(str(i) for i in l)
        c+=1

main()