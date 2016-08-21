f = open('E:\\Code Jam 2016\\A-large.txt', mode = 'r')
fo = open('E:\\Code Jam 2016\\out.txt', mode = 'w')

testCases = int(f.readline())
for case in range(1,testCases+1):
    print case
    N = int(f.readline())
    newN = N
    foundList = [0,0,0,0,0,0,0,0,0,0]
    if(N!=0):
        while(True):
            N_str = str(newN)
            for i in range(10):
                pos = N_str.find(str(i))
                if (pos > -1):
                    foundList[i] = 1
                    #print foundList
            if(sum(foundList) == 10):
                break
            newN = newN + N
        #print newN
        output = 'case #'+str(case)+': '+str(newN)+'\n'
        fo.writelines(output)
    else:
        #print 'INSOMNIA'
        output = 'case #'+str(case)+': INSOMNIA\n'
        fo.writelines(output)
print 'finish'
