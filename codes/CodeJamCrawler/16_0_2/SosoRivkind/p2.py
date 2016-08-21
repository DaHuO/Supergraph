cases = int(raw_input())

flip = {'-' : '+', '+' : '-'}

for case in range(cases):
    s = list(raw_input())
    n = len(s)
    
    result = 0
    
    i = n - 1
    while i >= 0:
        if s[i] == '-':
            j = -1
            
            while s[j + 1] == '+':
                s[j + 1] = '-'
                j += 1

            if j > -1:
                result += 1

            while j + 1 < n and s[j + 1] == '-':
                j += 1

            for k in range(i / 2 + 1):
                s[k], s[i - k] = flip[s[i - k]], flip[s[k]]

            result += 1

            i -= j

        i -= 1

    print('Case #' + str(case + 1) + ': ' + str(result))
