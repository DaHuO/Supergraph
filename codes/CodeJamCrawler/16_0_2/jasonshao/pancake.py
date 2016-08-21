t = input()
for poo in range(t):
    s = list(raw_input())
    ans = 0
    for i in range(len(s) - 1, -1, -1):
        face = s[i]
        if face == '+':
            continue
        else:
            if s[0] == '-':
                #flip
                for j in range(0, i + 1):
                    s[j] = "+" if s[j] == '-' else '-'
                s[:i+1] = reversed(s[:i+1])
                ans += 1
            else:
                ans += 2
                count = 0
                for p in range(0, i + 1):
                    if s[p] == '+':
                        s[p] = '-'
                        count +=1
                    else:
                        break
                #flip
                for j in range(0, i + 1):
                    s[j] = '+' if s[j] == '-' else '-'
                s[:i+1] = reversed(s[:i+1])

    print "Case #" + str(poo + 1) + ": " + str(ans)
