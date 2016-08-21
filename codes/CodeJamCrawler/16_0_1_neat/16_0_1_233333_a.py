import sys

input = sys.stdin.readlines()

for i in xrange(1,len(input)):
    dict1 = {}
    n = input[i].strip('\n')
    if n == '0':
        print 'Case #'+str(i)+': '+'INSOMNIA'
        continue
        
    j = 1
    while 1:
        n2 = int(n)*j
        #print n2
        s = str(n2)
        flag = 0
        
        for char in s:
            #print character
            if char not in dict1:
                dict1[char] = 1
            if len(dict1) >= 10:
                #print dict1
                flag = 1
                break
        if flag == 1:
            print 'Case #'+str(i)+': '+str(n2)
            break
        
        j += 1

