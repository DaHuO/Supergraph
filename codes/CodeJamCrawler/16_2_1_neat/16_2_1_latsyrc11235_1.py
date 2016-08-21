f = [line.rstrip() for line in open('/Users/roshil/Desktop/A-small-attempt0 (2).in')]
out = open('/Users/roshil/Desktop/out.txt','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for i in range(1, testcases+1):
    r1 = f[line]
    line += 1
    r1 = r1.lower()
    word = [k for k in r1]
    s = []
    while len(word) > 0:
        #print word
        if 'z' in word:
            word.remove('z')
            word.remove('e')
            word.remove('r')
            word.remove('o')
            s.append(0)
        elif 'w' in word:
            word.remove('t')
            word.remove('w')
            word.remove('o')
            s.append(2)
        elif 'u' in word:
            word.remove('f')
            word.remove('o')
            word.remove('u')
            word.remove('r')
            s.append(4)
        elif 'r' in word:
            word.remove('t')
            word.remove('h')
            word.remove('r')
            word.remove('e')
            word.remove('e')
            s.append(3)
        elif 'x' in word:
            word.remove('s')
            word.remove('i')
            word.remove('x')
            s.append(6)
        
        elif 'g' in word:
            word.remove('e')
            word.remove('i')
            word.remove('g')
            word.remove('h')
            word.remove('t')
            s.append(8)
        elif 'o' in word:
            word.remove('o')
            word.remove('n')
            word.remove('e')
            s.append(1)
        elif 'f' in word:
            word.remove('f')
            word.remove('i')
            word.remove('v')
            word.remove('e')
            s.append(5)
        elif 'v' in word:
            word.remove('s')
            word.remove('e')
            word.remove('v')
            word.remove('e')
            word.remove('n')
            s.append(7)
        else:
            word.remove('n')
            word.remove('i')
            word.remove('n')
            word.remove('e')
            s.append(9)
    s.sort()
    ans = "".join([str(l) for l in s])
    print ans
    out.write("Case #"+str(i)+": "+str(ans) + "\n")
out.close()