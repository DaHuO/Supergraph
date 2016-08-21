with open('output.txt', 'w') as g:
    pass


with open('A-large.in') as f:
    lineBuf = f.readline()
    T = int(lineBuf)

    for cnt in range(T):
        digits = [0 for i in range(10)]
        num = int(f.readline())
        flag = 0

        for subCnt in range(101):
            newNum = (subCnt+1)*num
            
            while newNum > 0:
                lastDig = newNum%10
                if digits[lastDig] == 0:
                    digits[lastDig] = 1

                newNum = newNum//10

            if sum(digits) == 10:
                flag = 1

                with open('output.txt', 'a') as g:
                    g.write('Case #'+str(cnt+1)+': '+str((subCnt+1)*num)+'\n')
                break

        if flag == 1:
            continue
        else:
            with open('output.txt', 'a') as g:
                g.write('Case #'+str(cnt+1)+': INSOMNIA\n')

