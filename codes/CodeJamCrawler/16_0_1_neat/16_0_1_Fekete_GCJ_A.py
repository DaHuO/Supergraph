import sys
sys.stdin = open("input.txt","r")
f = open("output.txt","w")

times = int(input())
test_number = 1
while test_number<=times :
    n = int(input())

    if n==0 :
        f.write("Case #%s: INSOMNIA\n"%str(test_number))
    else :

        digits = set()
        x = n
        while len(digits)<10 :
            s = str(x)
            for c in s :
                digits.add(c)

            x+=n


        
        f.write("Case #%s: %s\n"%(str(test_number),str(x-n)))
        
    test_number+=1
        
f.close()
