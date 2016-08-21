import sys
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
n=[0]*t

for i in xrange(0, t):
    n[i] = long(raw_input())
    #print n[i]
for i in xrange(0,t):
    if(n[i]==0):
        num = str(i+1).strip()
        print "Case #"+num+": INSOMNIA"
    else: #process a number
        m =0
        flag = 'n'
        dig = {d:0 for d in xrange(0,10)}
        #print dig
        #print "next number",n[i]
        while(1):
            #process number
            m += 1
            number = n[i]*m
            number_main=number
            #print "number",number
            while number:
                flag = 'y'
                digit = number % 10
                #print digit
                for x in dig: #update freq of d in dict dig
                    if digit == x:
                        dig[x]+=1
                        #print dig
                for x in dig:
                    if dig[x]==0:
                        flag ='n'
                if flag == 'y':
                    num = str(i+1).strip()
                    print "Case #"+num+":",number_main
                    break
                # remove last digit from number (as integer)
                number //= 10
            if flag == 'y':
                break
