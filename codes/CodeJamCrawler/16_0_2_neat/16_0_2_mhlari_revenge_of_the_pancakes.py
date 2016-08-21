file = open('B-large.in.txt','r')
file_out = open('out2.txt','w')
file = file.readlines()
n = int(file[0])
for j in range(1,n+1):
    S = file[j].strip() 
    S = list(S)
    S = S[::-1]
    N = len(S)
    count = 0
    while S != ['+']*N:
        count+=1
        n_ind = S.index('-')
        for i in range(n_ind,N):
            if S[i]=='-':
                S[i]='+'
            else:
                S[i]='-'
        
    file_out.write('Case #%i: %i\n'%(j,count))    
        
