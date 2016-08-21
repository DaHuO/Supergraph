def solve(n):
    yet_to_see = ['0','1','2','3','4','5','6','7','8','9']
    i = 1
    if n == 0:
        return 'INSOMNIA'
    else:
        while yet_to_see:
            x = str(n*i)
            for digit in x:
                if digit in yet_to_see:
                    yet_to_see.pop(yet_to_see.index(digit))
            i = i + 1
    return n * (i-1) 

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\A-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        n = int(r.readline())
        w.write('Case #{0}: {1}\n'.format(str(case), solve(n)))

