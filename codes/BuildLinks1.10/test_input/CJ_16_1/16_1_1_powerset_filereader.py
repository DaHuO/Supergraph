with open('/Users/Justin/projects/codejam/A-large.in', 'r+') as f:
    lines = list(f)

from string import ascii_uppercase

T=lines.pop(0).strip()
lines = [ l.strip() for l in lines]

cases=[]
for i in range( int(T) ):
    S = lines.pop(0)

    cases.append({'S': S })

def solve(case):
    S=case['S']
    letters = [l for l in S]
    answer = ""
    answer += letters.pop(0)
    for l in letters:
        if ascii_uppercase.index(l) > ascii_uppercase.index( answer[0] ):
            answer = l + answer
        elif ascii_uppercase.index(l) < ascii_uppercase.index( answer[0] ):
            answer = answer + l
        else:
            if ascii_uppercase.index(l) < ascii_uppercase.index( answer[-1] ):
                answer = answer + l
            else:
                answer = l + answer

    return answer



out = open('/Users/Justin/projects/codejam/output.out', 'w')

j=0
for c in cases:
    j+=1
    st= 'Case #'+str(j)+': '+solve(c)+'\n'
    print st
    out.write(st)

