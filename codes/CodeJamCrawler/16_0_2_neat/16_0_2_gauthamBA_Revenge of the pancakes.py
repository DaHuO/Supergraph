for t in range(int(input())):
    s = raw_input()
    i = 0
    flips = 0
    while i < len(s):
        if s[i] != '+':
            j = i
            while j < len(s) and s[j] == '-':
                j += 1
            flips += 1 if i == 0 else 2
            i = j
        else:
            i += 1
    print('Case #' + str(t + 1) + ': ' + str(flips))
