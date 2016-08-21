with open('output.txt', 'w') as g:
    pass


with open('B-large.in') as f:
    lineBuf = f.readline()
    T = int(lineBuf)

    for cnt in range(T):
        height = [0 for i in range(2501)]
        n = int(f.readline())
        for cnt2 in range(2*n-1):
            lineBuf = f.readline()
            tmpHeightList = lineBuf.split(' ')
            for h in tmpHeightList:
                height[int(h)] = height[int(h)]+1
        
        result = ""
        for cnt3 in range(len(height)):
            if height[cnt3]%2 == 1:
                result = result +' '+ str(cnt3)
        with open('output.txt', 'a') as g:
            g.write('Case #'+str(cnt+1)+':'+result+'\n')

