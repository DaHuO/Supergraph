
def solve(S):
    answer = [S[0]]
    for char in S[1:]:
        if ord(char) >= ord(answer[0]):
            #print 'found larger'
            answer = [char] + answer
            #print answer
        else:
            #print 'smaller'
            answer.append(char)
            #print answer
    return ''.join(answer) 

T = int(raw_input())
solutions=[]
for case in xrange(T):
    S = raw_input().strip()
    sol = solve(S)
    solutions.append('Case #'+str((case+1))+': '+str(sol))

#for solution in solutions:
#    print solution

with open('last_word_out.txt', 'w') as f:
    for s in solutions[:-1]:
        f.write(s)
        f.write("\n")
    f.write(solutions[-1])