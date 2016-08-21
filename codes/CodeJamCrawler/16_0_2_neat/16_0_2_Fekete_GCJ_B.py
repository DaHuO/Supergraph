import sys
sys.stdin = open("input.txt","r")
f = open("output.txt","w")

times = int(input())
test_number = 1
while test_number<=times :
    s = input()
    n = len(s)
    
    i = n-1
    total = 0

    happy_side_symbol = '+'

    while i>=0 :
        if s[i] != happy_side_symbol :
            total+=1
            happy_side_symbol = s[i]
        i-=1

    f.write("Case #"+str(test_number)+": "+str(total)+'\n')
        
    test_number+=1
        
f.close()
