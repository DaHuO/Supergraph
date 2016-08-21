from collections import defaultdict
def solve(N, senators):
    freq = defaultdict(int)

    for i in xrange(N):
        freq[i] = senators[i]
    answer = []
    while senators:
        if senators == [1,1,1]:
            senator1 = None
            for k in freq.iterkeys():
                #print "first", k, freq[k]
                freq[k] -= 1
                senator1 = k
                #print "senator1", senator1
                if freq[k] == 0:
                    freq.pop(k, None)
                break
            answer.append(chr(65 + senator1))
            senators[0] -= 1
            while senators and senators[0] == 0:
                senators.pop(0)
            continue
        senators.sort(reverse=True)
        #print "senators", senators
        senator1 = None
        for k in freq.iterkeys():
            #print "first", k, freq[k]
            if freq[k] == senators[0]:
                freq[k] -= 1
                senator1 = k
                #print "senator1", senator1
                if freq[k] == 0:
                    freq.pop(k, None)
                break
        senator2 = None
        for k in freq.iterkeys():
            #print "second", k, freq[k]
            if freq[k] == senators[1]:
                freq[k] -= 1
                senator2 = k
                #print "senator2", senator2
                if freq[k] == 0:
                    freq.pop(k, None)
                break
        answer.append(chr(65 + senator1) + chr(65 + senator2))
        senators[0] -= 1
        senators[1] -= 1
        while senators and senators[0] == 0:
            senators.pop(0)

    joined = ' '.join(answer)
    return joined

T = int(raw_input())
solutions=[]
for case in xrange(T):
    N = int(raw_input())
    senators = map(int, raw_input().strip().split())
    sol = solve(N, senators)
    solutions.append('Case #'+str((case+1))+': '+str(sol))
#for solution in solutions:
#        print solution

"""
with open("bffs_large_test.in", 'r') as f:
    T = int(f.readline())
    solutions=[]
    for case in xrange(T):
        N = int(f.readline())
        students = map(int, f.readline().strip().split())
        sol = solve(students, N)
        solutions.append('Case #'+str((case+1))+': '+str(sol)) 
"""
with open('senate_out.txt', 'w') as f:
    for s in solutions[:-1]:
        f.write(s)
        f.write("\n")
    f.write(solutions[-1])
