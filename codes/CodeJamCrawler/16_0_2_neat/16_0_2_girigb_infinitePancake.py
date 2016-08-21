T = int(raw_input())
counter=1
while(T > 0):
    string = raw_input()
    ans = 0
    flag = False
    # print reversed(list(string))
    for j in reversed(string):
        if(flag == False):
            if( j == '-'):
                ans+=1
                flag=True
        else:
            if(j == "+"):
                ans+=1
                flag = False

    print "Case #"+str(counter)+": "+str(ans)
    counter+=1
    T-=1
