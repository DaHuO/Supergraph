n = raw_input()
#print n
n = int(n)
i=0
#z = [1,2,3,4,5,6,7,8,9,10]
while(i<n):
    
    z = {}
    for co in range(0,10):
        z[co] = False

    
    x = raw_input()
    x = int(x)
    #print x
    if x == 0:
         t = i+1
         op = "Case #"+str(t)+": INSOMNIA"
         print op
         i = i+1
    else:
        l = []
        l.append(x)
        j=1
        flag = False
        while(flag== False and j<100):
            
            y = x*j
            l.append(y)
            
            k = list(str(y))
            #print k
            #print y
            for val in k:
                val = int(val)
                z[val] = True
                #print val,z[val]
            flag = True
            #print "length",len(z)
            for key in z:
                #print "key",z[key],"number",key
                if z[key]== False:
                    
                    flag = False
                    
            if flag == True:
                j= 10
                t = i+1
                op = "Case #"+str(t)+":"
                print op,y
                


                i = i+1
                
            else:
                j = j+1
                    

