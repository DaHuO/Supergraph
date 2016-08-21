import sys
import operator
test = input()
t = 1
while(test!=0):
    n = input()
    np = n
    par = raw_input()
    f = par.split()
    f = map(int,f)
    part = {}
    i = 65
    j=0
    sum = 0
    while(np!=0):
        part[chr(i)] = f[j]
        sum = sum + f[j]
        i = i+1
        j = j+1
        
        np = np -1
    j1 = str (t)
    sys.stdout.write('Case #'+j1+': ')
    t = t+1
    sorted_part = sorted(part.items(), key = operator.itemgetter(1), reverse =True)
    #print sorted_part
    while(sum!=0):
        fir_tup = sorted_part[0][1]
        sec_tup = sorted_part[1][1]
        
        div = float (sum/2)
        if (sum==3):
            part[sorted_part[0][0]] = fir_tup -1
            #print sorted_part[0][0]
            sys.stdout.write(sorted_part[0][0])
            sum = sum -1
        else:
            if(fir_tup -1 < div and sec_tup -1 < div):
                part[sorted_part[0][0]] = fir_tup -1
                part[sorted_part[1][0]] = sec_tup -1
                #print sorted_part[0][0]+sorted_part[1][0]
                sys.stdout.write(sorted_part[0][0]+sorted_part[1][0])
                sum = sum-2
            else:
                part[sorted_part[0][0]] = sorted_part[0][1] -2
                #print sorted_part[0][0]+sorted_part[0][0]
                sys.stdout.write(sorted_part[0][0]+sorted_part[0][0])
                sum = sum - 2
        
        sorted_part = sorted(part.items(), key = operator.itemgetter(1), reverse =True)
        if(sum!=0):
            sys.stdout.write(' ')
    print
    test = test -1
