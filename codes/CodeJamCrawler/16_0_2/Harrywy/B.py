def BFS(S):
    l = len(S)
    goal = '+' * l
    states = set()
    states.add(S)
    q = [S]
    new_q = []
    ans = 0
    while len(q)>0:
        for s in q:
            if s == goal:
                return ans
            for i in range(1,l+1):
                reverse = s[:i][::-1]
                change = ''
                for x in reverse:
                    if x == '-':
                        change += '+'
                    else:
                        change += '-'
                new_s = change + s[i:]
                if not new_s in states:
                    states.add(new_s)
                    new_q.append(new_s)
        q = new_q[:]
        new_q = []
        ans+=1

#print(BFS('--+-'))


outfile = open('out.out', 'w')

with open('in.in') as infile:
    T = infile.readline()
    for i in range(int(T)):
        S = infile.readline()
        ans = BFS(S.strip())
        outfile.write('Case #'+str(i+1)+': '+ str(ans)+'\n')
