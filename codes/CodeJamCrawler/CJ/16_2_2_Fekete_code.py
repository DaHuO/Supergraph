import sys
#sys.stdin = open("input.txt","r")
fout= open("output.txt","w")

tests = int(input())
test = 1
while test<=tests :
        
    delta = 100000000000000000
    x,y = '',''
    s,t = (list(x) for x in input().split())

    def rec1(pos) :
        global s,t
        if pos==len(s) :
            rec2(0)
            return
        if s[pos]!='?' :
            rec1(pos+1)
        else :
            for c in '0123456789' :
                s[pos] = c
                rec1(pos+1)
                s[pos] = '?'

    def rec2(pos) :
        global delta,x,y,s,t
        if pos==len(t) :
            d = abs(int(''.join(s))-int(''.join(t)))
            
            if d<delta :
                delta = d
                x = ''.join(s)
                y = ''.join(t)
            return
        if t[pos]!='?' :
            rec2(pos+1)
        else :
            for c in '0123456789' :
                t[pos] = c
                rec2(pos+1)
                t[pos] = '?'
    
    rec1(0)
    fout.write("Case #%s: %s %s\n"%(str(test),x,y))
    test+=1
fout.close()
