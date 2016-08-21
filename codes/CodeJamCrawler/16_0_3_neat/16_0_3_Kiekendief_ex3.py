import math

f = open("C-small-attempt0.in","r")
g = open ("output.log","w")

runs = int(f.readline())

def candivide(number):
    #print int(math.sqrt(number))
    for i in range(2, int(math.sqrt(number))+1):
        if (number%i) == 0 :
            return i
    return 0

def getdivisors(number) :
    list = []
    #print number
    for i in range(2,11):
        #print "   %d"%i
        conv = int(number,i)
        divisor = candivide(conv)
        #print "   --> %d"%divisor
        if divisor == 0 :
            break
        else :
            list.append(divisor)
    return list

for i in range(runs) :
    list = f.readline().split(" ")
    n = int(list[0])
    j = int(list[1])
    #print n
    #print j
    
    start = 2**(n-1)+1
    end = 2**(n)
    
    cnt = 0
    
    line = "Case #%d:"%(i+1)
    print line
    g.write(line+'\n')
    
    #print start
    #print end
    
    for i in range(start,end):
        #print i
        if (i%2) :
            number="{0:b}".format(i)
            list_divisors = getdivisors(number)
            if len(list_divisors) == 9:
                cnt += 1
                line = number
                for i in list_divisors :
                    line += " %d"%i
                print line
                g.write(line+'\n')      
                if cnt > j-1:
                    break
    #print cnt

f.close()
g.close()