test_cases = int(raw_input())
for test in range(test_cases):
    n = int(raw_input())
    if(n !=0):
        a = {x: 0 for x in range(10)}
        mul =1
        while len(a)>0:
            temp = mul*n
            while temp>0:
                temp1 = temp %10;
                if(temp1 in a):
                    del(a[temp1])
                temp /=10
            mul+=1
        print "case #"+str(test+1)+":"+" "+str((mul-1)*n)
    else:
        print "case #"+str(test+1)+":"+" INSOMNIA"