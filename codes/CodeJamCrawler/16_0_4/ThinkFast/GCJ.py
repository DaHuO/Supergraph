
# coding: utf-8

# In[138]:

def solve(K,C,S):
    required = (K / 2 + K % 2)
    if C == 1 and S < K or S < required:
        return "IMPOSSIBLE"
    
    if C == 1:
        solution = range(1,K+1)
        return ' '.join(map(str,solution))
    
    if K == 1:
        solution = [1]
        return ' '.join(map(str,solution))
    
    
    to_cover = range(K)
    sol = [((K*x)+y) for x,y in zip(to_cover[::2], to_cover[1::2])]
    if K % 2 == 1:
        sol.append(K**C - 1)
        
    solution = [x+1 for x in sol]
    
    #verify
    for x in solution:
        if x > K**C:
            raise Exception("Bug! {} {} {} {} {}".format(x,x+1,K,C,K**C))
            
    block_covered = [((x-1)/K)+1 for x in solution]
    position_covered = [(x-1)%K+1 for x in solution]
    if set(range(1,K+1)) - set(block_covered).union(set(position_covered)) != set():
        raise Exception("Bug! {} {}\n{}\n{} {}\n{}".format(K,C, solution,block_covered, position_covered,set(range(1,K+1)) - set(block_covered).union(set(position_covered))))

    #print
    return ' '.join(map(str,solution))


# In[137]:




# In[141]:

path = r'E:\Downloads\D-small-attempt1.in'
with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in xrange(T):
        K,C,S = map(int, f.readline().split())
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(K,C,S)))

