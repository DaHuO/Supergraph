t = int(raw_input())
for i in range(t):
    k = 1
    str1 = "0123456789"
    n = int(raw_input())
    if (n == 0):
        ans = "INSOMNIA"
    else:
        while(len(str1) > 0):
            val = n * k
            #print val
            #print str1
            for j in str(val):
                if(j in str1):
                    str1 = str1[:str1.index(j)] + str1[str1.index(j)+1:]
            k+=1
        ans = str(val);
    print "Case #" + str(i+1) + ": " + ans
    
