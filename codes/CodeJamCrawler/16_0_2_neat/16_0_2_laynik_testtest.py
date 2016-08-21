fileRead = open('C:\\input.txt', encoding='utf-8')
fileWrite = open('C:\\output.txt', 'w', encoding='utf-8')

n = int(fileRead.readline())
for num in range(n):
    ans = 0
    fileWrite.write('Case #' + str(num + 1)+ ': ')
    s = (fileRead.readline().strip())
    i = 0
    while i < len(s):
        j = i
        while (j < len(s) and s[i] == s[j]):
            j += 1
        if j < len(s):
            ans += 1
        i = j
    if s[i - 1] == '-':
        ans += 1
    fileWrite.write(str(ans) + '\n')
fileWrite.close()
