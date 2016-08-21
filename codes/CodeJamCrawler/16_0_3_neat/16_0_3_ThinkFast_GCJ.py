
# coding: utf-8

# In[116]:

def solve(N,J):
    assert N == 32 and J == 500
    lines = ['']
    for k,v in ans.iteritems():
        lines.append('{} {}'.format(k*2, ' '.join([str(v[b]) for b in sorted(v.iterkeys())])))
    return '\n'.join(lines)


# In[ ]:

for x in ans.iterkeys():
    xx = x+x
    for b in xrange(2,11):
        print int(xx,b) % ans[x][b]


# In[120]:

for x in ans.iterkeys():
    xx = x+x
    print int(xx,b), ans[x].values()


# In[24]:

def isprime(n):
    x = 3
    m = int(n**0.5)+1
    while x < m:
        if n % x == 0:
            return x
        x += 1
    return False


# In[98]:

ans = dict()
i = 0
while i < 2**14:
    bin_rep = '1{0:014b}1'.format(i)
    temp = dict()
    for base in xrange(2,11):
        val = isprime(int(bin_rep, base))
        if val:
            temp[base] = val
        else:
            break
    if len(temp) == 9:
        ans[bin_rep] = temp
    if len(ans) == 500:
        break
    i += 1


# In[112]:

for k,v in ans.iteritems():
    for base,divisor in v.iteritems():
        if int(k, base) % divisor != 0:
            raise Exception()


# In[121]:

path = r'E:\Downloads\C-large.in'
with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in xrange(T):
        N,J = map(int, f.readline().split())
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(N,J)))

