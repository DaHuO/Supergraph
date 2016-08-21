digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8' ,'9'])

def solution(N):
    if N==0:
        return 'INSOMNIA'
    else:
        seen = set() 
        current = 0
        while seen != digits:
            current += N
            for digit in str(current):
                seen.add(digit)
        return current

with open('input.in', 'r') as infile, open('output', 'w') as out:
    next(infile)
    for index, line in enumerate(infile):
        N = int(line)
        out.write("Case #{0}: {1}\n".format(index+1, solution(N)))
