t = int(input())

for i in range(t):
    n = int(input())

    print('Case #', i + 1, ':', sep = '', end = ' ')
    
    if(n == 0):
        print('INSOMNIA')
        continue

    l = [0] * 10
    i = 1
    s = 0
    
    while(not all(l)):
        s = str(i * n)
        
        for j in range(len(s)):
            if(l[int(s[j])] == 0):
                l[int(s[j])] = 1

        i += 1

    print(s)        
