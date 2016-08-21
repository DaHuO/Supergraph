def solve(n):     
    return 1 

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\D-small-attempt0.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        k,c,s = map(int,r.readline().split())
        answers = []
        for i in range(1,k+1):
            answer = 0
            for j in range(c-1,0,-1):
                answer = answer + (i-1) * k**j
            answer = answer + i
            answers.append(answer)       
        w.write('Case #{0}: {1}\n'.format(str(case), ' '.join(map(str,answers))))

