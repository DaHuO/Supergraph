import math 


with open('output.txt', 'w') as g:
    pass


with open('D-small-attempt1.in') as f:
    lineBuf = f.readline()
    T = int(lineBuf)

    for cnt in range(T):
        lineBuf = f.readline()
        kcs = lineBuf.split(' ')
        k = int(kcs[0])
        c = int(kcs[1])
        s = int(kcs[2])

        if math.ceil(k/c) > s:
            with open('output.txt', 'a') as g:
                g.write('Case #'+str(cnt+1)+': IMPOSSIBLE\n')
            continue
        
        result = []
        kPointer = 0
        flag = 0

        while flag == 0:

            fullPointer = kPointer
            for cnt2 in range(c-1):

                offset = kPointer+cnt2+1
                if offset >= k-1:

                    offset = k-1
                    flag = 1

                fullPointer = fullPointer * k + offset
            
            result.append(fullPointer)
            kPointer = kPointer + c 
            if kPointer > k-1:
                break

        resultStr = ''
        for cnt3 in range(len(result)):
            resultStr = resultStr+' '+str(result[cnt3]+1)

        with open('output.txt', 'a') as g:
            g.write('Case #'+str(cnt+1)+':'+resultStr+'\n')


                
