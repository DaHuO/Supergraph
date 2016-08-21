l = []
with open('B-large.in.txt') as f:
    for line in f:
        l.append(line.splitlines())
f = open('outputb-large.txt', 'w')
y = int(l[0][0])
for j in range(y):
    s = list(l[j+1][0])
    ans = 0
    tam = len(s)
    f.write('Case #' + str(j+1)+': ')
    while(True):
        if all(s[i] == '+' for i in range(tam)):
            break
        if s[0] == '-':
            for k in range(tam):
                if s[k] == '-':
                    s[k] = '+'
                else:
                    break
        else:
            for k in range(tam):
                if s[k] == '+':
                    s[k] = '-'
                else:
                    break
        ans+=1
    f.write(str(ans))
    f.write('\n')
f.close()
