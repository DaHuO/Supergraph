n = []
t = int(input())
for i in range(t):
    n.append(input())
for i in range(t):
    dgt = ['0','1','2','3','4','5','6','7','8','9']
    m = 1
    while dgt != []:
        tv = str(int(n[i])*m)
        if tv == '0':
            answer = 'INSOMNIA'
            break
        else:
            for e in tv:
                if e in dgt:
                    dgt.remove(e)
            m += 1
            answer = tv
    print('Case #%d:' % (i+1), answer)
