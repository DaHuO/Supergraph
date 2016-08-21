cases = []
check = []

def digits(num):
    for c in num :
        check[int(c)] = True
    return check

with open('A-small-attempt0.in') as f:
    l = int(f.readline())
    for i,line in enumerate(f):
        check = [False]*10
        change = True
        N = int(line)
        n = 0
        while(False in check and n < 10000 and N != 0):
            n += N
            check = digits(str(n))
        if(False in check):
            ans = 'INSOMNIA'
        else:
            ans = str(n)
        s = 'Case #'+str(i+1)+': '+ans+'\n'
        print(s)
        cases.append(s)

with open('A-small-attempt0.out','w+') as g:
    g.writelines(cases)
            