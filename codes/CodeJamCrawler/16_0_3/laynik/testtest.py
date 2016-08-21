fileRead = open('C:\\input.txt', encoding='utf-8')
fileWrite = open('C:\\output.txt', 'w', encoding='utf-8')
def baseN(num, b):
    ans = 0
    cur = 1
    while num > 0:
        ans += cur * (num % 10)
        cur *= b
        num = num // 10
    return ans
def isPrime(n):
    if n < 2: 
         return -1;
    if n % 2 == 0:             
         return 2
    k = 3
    while k * k * k * k * k <= n:
         if n % k == 0:
             return k
         k += 2
    return -1
cnt = int(fileRead.readline())
for num in range(cnt):
    ans = 0
    fileWrite.write('Case #' + str(num + 1)+ ':\n')
    s = (fileRead.readline().strip().split())
    i = (1 << (int(s[0]) - 1)) + 1
    while ans < int(s[1]):
        div = [0] * 11
        binary = int('{0:b}'.format(i))
        j = 2
        while j < 11:
            k = isPrime(baseN(binary, j))
            if k != -1:
                div[j] = k
            else:
                break
            j += 1
        if j == 11:
            print(ans, binary)
            fileWrite.write(str(binary) + ' ')
            j = 2
            while j < 11:
                fileWrite.write(str(div[j]) + ' ')
                j += 1
            fileWrite.write('\n')
            ans += 1
        i += 2
fileWrite.close()
