fileRead = open('C:\\input.txt', encoding='utf-8')
fileWrite = open('C:\\output.txt', 'w', encoding='utf-8')

n = int(fileRead.readline())
for i in range(n):
    used = [0] * 10
    fileWrite.write('Case #' + str(i + 1)+ ': ')
    x = int(fileRead.readline())
    ok = -1
    for j in range(100):
        myStr = str(x * (j + 1))
        for l in range(len(myStr)):
            used[int(myStr[l])] = 1         
        fail = False
        for k in range(10):
            if used[k] == 0:
                fail = True
        if not fail:
            ok = (j + 1) * x
            break
    if ok == -1:
        fileWrite.write('INSOMNIA\n')
    else:
        fileWrite.write(str(ok) + '\n')
fileWrite.close()
