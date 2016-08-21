fileRead = open('C:\\input.txt', encoding='utf-8')
fileWrite = open('C:\\output.txt', 'w', encoding='utf-8')
cnt = int(fileRead.readline())
for num in range(cnt):
    fileWrite.write('Case #' + str(num + 1)+ ': ')
    s = fileRead.readline().strip()
    ans = ''
    maxLet = 'A'
    for i in range(len(s)):
        if (s[i] >= maxLet):
            ans = s[i] + ans
            maxLet = s[i]
        else:
            ans = ans + s[i]
    fileWrite.write(ans + '\n')
fileWrite.close()
