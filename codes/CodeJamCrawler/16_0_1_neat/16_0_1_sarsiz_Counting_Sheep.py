t = int(input()) # enter the number of test cases
i=0
while(t):
    N = int(input())
    dict1 = {}
    k = 1
    t-=1
    i+=1
    if N == 0:
        print ('Case #' + str(i)+ ':' + ' INSOMNIA')
        continue
    else:
            
        temp1 = N
        while len(dict1)!=10:
            while temp1!=0:
                temp = temp1 % 10
                dict1[temp] = 1
                #print (dict1)            
                temp1 = temp1//10
            temp1 = k*N
            k+=1

    
    print('Case #'+ str(i)+ ': ' + str((k-2)*N))
           
     #test cases dec till 0       
