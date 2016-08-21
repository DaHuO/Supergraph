for tc in range(1, int(input()) + 1): # t * s
    s = input() # s
    oc = s[0]
    result = 0
    for c in s: # s * 1
        if oc != c:
            result += 1
        oc = c
    if oc == '-':
        result += 1
    print("Case #", tc, ": ", result, sep='')
