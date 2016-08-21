import math

n = input()
a = map(int,raw_input().strip().split(' '))
p = a[0]
q = a[1]

num = '1'+'0'*(p-2)+'1'
#print num

d='10'

w = 0
e = 'Case #1:\n'

while(w<q):
    k = 0
    l = num
    def returnSimplifiedNumber(num,n):
        z = 0
        for i in range(len(num)):
            z+=(n**i)*int(num[len(num)-1-i])
        #print z
        if (z%2 == 0):
    	    return 2
        else:
    	    p = 3
            while (p < 1000):
                if(z%p == 0):
                    return p
                else:
            	    p+=2
            return 0
    for p in range(2,11):
        if(returnSimplifiedNumber(num,p) == 0):
            break
        else:   
            l+=' '+str(returnSimplifiedNumber(num,p))    
        k+=1
    if(k == 9):
        w+=1
        e+=l+'\n'
        #print l
    num = bin(int(num,2) + int(d,2))[2:]

print e





