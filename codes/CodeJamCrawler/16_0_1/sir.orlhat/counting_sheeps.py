myfile = open('A-large.in' , 'r')
answer = open('A-large.out','w')

T = myfile.readline()
T = int(T)
T_count = 1

while ( T != 0):
    N = myfile.readline()
    N = int(N)

    mul = 1#checker
    finish = 0#done

    D = [0,0,0,0,0,0,0,0,0,0]

    while(finish == 0):
        val = N*mul
        new_dig = [int(i) for i in str(val)]#values
        res = len(new_dig)#ans
        counter = 0

        while(counter <res):
            if new_dig[counter] == 1:
                D[0] = 1
            elif new_dig[counter] ==2:
                D[1] = 1
            elif new_dig[counter] ==3:
                D[2] = 1
            elif new_dig[counter] ==4:
                D[3] = 1
            elif new_dig[counter] ==5:
                D[4] = 1
            elif new_dig[counter] ==6:
                D[5] = 1
            elif new_dig[counter] ==7:
                D[6] = 1
            elif new_dig[counter] ==8:
                D[7] = 1
            elif new_dig[counter] ==9:
                D[8] = 1
            elif new_dig[counter] ==0:
                D[9] = 1

            counter +=1
        #print(D)
        slp = sum(D)
        if(slp == 10):
            finish = 1
            
            print("Case #" + str(T_count) + ': ' + str(val), file = answer)
        if(val == 0):
            finish = 1
            
            print("Case #" + str(T_count) + ': ' + 'INSOMNIA', file = answer)
            
        mul += 1
    T_count+=1
    T-=1
answer.close()




















            
                
        
