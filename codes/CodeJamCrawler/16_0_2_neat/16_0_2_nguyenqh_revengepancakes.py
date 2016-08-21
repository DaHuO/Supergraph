
def reduce(s):
    prev = ' '
    news = []
    for c in s:
        if c != prev:
            news.append(c)
        prev = c
    if prev == '+': news.pop()
    
    return ''.join(news)

f = open('large.txt','r')
fo = open('out.txt','w')

T = int(f.readline())

for t in range(1,T+1):
    line = f.readline().rstrip('\n')

    s = reduce(line)
    
    fo.write('Case #{:d}: {:d}\n'.format(t,len(s)))
fo.close()
    
            
            
            

    
    
    
