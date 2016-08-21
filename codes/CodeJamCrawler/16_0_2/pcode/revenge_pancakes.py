cache = {}
def revenge_pancakes(S):
    if S in cache:
        return cache[S]
    if S == '+' * len(S):
        return 0
    if S[-1] == '+':
        return revenge_pancakes(S[:-1])
    return 1 + revenge_pancakes(flip(S))

def flip(S):
    reverse = S
    flipped = []
    for char in reverse:
        if char == '-':
            flipped.append('+')
        else:
            flipped.append('-')

    return ''.join(flipped)
    
import sys
T = int(raw_input())
solutions=[]
for case in xrange(T):
    S = raw_input().strip()
    sol = revenge_pancakes(S)
    if sol not in cache:
        cache[S] = sol
    solutions.append('Case #'+str((case+1))+': '+str(sol))

#for solution in solutions:
#    print solution

with open('revenge_pancakes_out.txt', 'w') as f:
    for s in solutions[:-1]:
        f.write(s)
        f.write("\n")
    f.write(solutions[-1])



