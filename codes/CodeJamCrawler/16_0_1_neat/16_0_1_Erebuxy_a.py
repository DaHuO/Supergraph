import math

num = int(raw_input())  # read a line with a single integer
for i in range(1,num+1):
    n = abs(int(raw_input()))
    if n == 0:
        print "Case #"+str(i)+": INSOMNIA"
    else:
        cou = [0 for j in range(10)]
        sol = [1 for j in range(10)]
        cur = n
        while True:
            temp = cur
            
            # add digits
            while temp > 0:
                dig = temp % 10
                cou[dig] = 1
                temp /= 10
            #check digit
            if cou == sol:
                print "Case #"+str(i)+":", cur
                break
            cur += n
                
                