def char2num(c):
    return ord(c) - 65
    
def num2char(n):
    return chr(n + 65)

f = open('C:\\study\\gjam\\jam2016\\A-large.in')
f_out = open('C:\\study\\gjam\\jam2016\\res.txt','w+')

T = int(f.readline())
print T

for i in range(T):
    
    N = int(f.readline()) 

    S = list(map(int, f.readline().split()))
    tag = []
      
    for k in range(len(S)):
        tag.append(num2char(k))

    res = ''
    while (sum(S) > 0):        
        S, tag = zip(*sorted(zip(S, tag)))
        S = list(S)
        tag = list(tag)
        
        if (sum(S) == S[N-1] + S[N-2]):
            res = res + tag[N-1] + tag[N-2] + ' '
            S[N-1] -= 1
            S[N-2] -= 1
            continue
        
        if (S[N-2] == 0):
            diff = S[N-1]
        else:
            diff = S[N-1] - S[N-2] + 1
        for k in range(diff):
            res = res + tag[N-1] + ' '

        S[N-1] = S[N-1] - diff
    
        
    res = res[:-1]          


    f_out.write("Case #"+str(i+1)+": "+res+'\n')



f.close()
f_out.close()

