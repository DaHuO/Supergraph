T = int(input())

for t in range(T):
    s = list(input())
    
    tail_start = len(s) - 1
    marker = s[-1]
    count = 0
    #print("initial", s)
    while (tail_start > 0):

        for j in range(len(s)-1, -1, -1):
            if s[j] == marker:
                if (tail_start - j > 1):
                    break
                tail_start = j
        
        if tail_start > 0:
            for i in range(tail_start):
                s[i] = ('+' if s[i] == '-' else '-')
                #print("after next move", s)
            count += 1

    if s[0] == '-':
        count += 1
        for i in range(len(s)):
            if s[i] == '-':
                s[i] = '+'
            else:
                s[i] = '+'
    #print(s, 'after', count, 'moves')
    print('Case #', t+1, ': ', count, sep='')
