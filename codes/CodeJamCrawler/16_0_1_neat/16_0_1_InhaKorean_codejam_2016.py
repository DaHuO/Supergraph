FILE_NAME = 'C:\\codejam\\A-large'

f = open(FILE_NAME + '.in', 'r')
o = open(FILE_NAME + '.out', 'w')
 
def case_result(case) :
    N = int(f.readline())

    if N == 0 :
        return str('INSOMNIA')

    i = N
    S = set()
    while True :
        for n in str(i) :
            S.add(n)
        if len(S) == 10 :
            return str(i)

        i += N

T = int(f.readline())
for case in range(1, T+1) :
    o.write('Case #'+str(case)+': '+case_result(case)+'\n')
 
f.close()
o.close()
 