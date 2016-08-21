n = {'ZERO':0, 'ONE':1, 'TWO':2, 'THREE':3,
     'FOUR':4, 'FIVE':5, 'SIX':6, 'SEVEN':7, 'EIGHT':8,
     'NINE':9}

def solve(s):
    nums  = []
    x = list(s)
    if '\n' in x:
        x.pop(x.index('\n'))
    while x:
        if 'Z' in x:
            for c in 'ZERO':
                x.pop(x.index(c))
            nums.append('ZERO')
        elif 'W' in x:
            for c in 'TWO':
                x.pop(x.index(c))
            nums.append('TWO')
        elif 'U' in x:
            for c in 'FOUR':
                x.pop(x.index(c));
            nums.append('FOUR')
        elif 'G' in x:
            for c in 'EIGHT':
                x.pop(x.index(c));
            nums.append('EIGHT')
        elif 'X' in x:
            for c in 'SIX':
                x.pop(x.index(c));
            nums.append('SIX')
        elif 'V' in x and 'F' in x:
            for c in 'FIVE':
                x.pop(x.index(c));
            nums.append('FIVE')
        elif 'V' in x:
            for c in 'SEVEN':
                x.pop(x.index(c));
            nums.append('SEVEN')
        elif 'O' in x:
            for c in 'ONE':
                x.pop(x.index(c));
            nums.append('ONE')
        elif 'H' in x:
            for c in 'THREE':
                x.pop(x.index(c));
            nums.append('THREE')
        else:
            for c in 'NINE':
                x.pop(x.index(c));
            nums.append('NINE')
    res = [str(n[i]) for i in nums]
    res.sort()
    return ''.join(res)

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\A-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        s = r.readline()
        w.write('Case #{0}: {1}\n'.format(case, solve(s)))
        
