with open('output.txt', 'w') as g:
    pass


with open('B-large.in') as f:
    lineBuf = f.readline()
    T = int(lineBuf)

    for cnt in range(T):

        lineBuf = f.readline()
        lineBuf = lineBuf.strip('\n')
        result = 0

        for cnt2 in range(len(lineBuf)-1):

            if lineBuf[cnt2] != lineBuf[cnt2+1]:

                result = result+1

        if lineBuf[-1] == '-':
            result = result+1

        with open('output.txt', 'a') as g:
            g.write('Case #'+str(cnt+1)+': '+str(result)+'\n')


                
