file = open('A-large.in.txt','r')
file_out = open('out1.txt','w')
file = file.readlines()
n = int(file[0])
for j in range(1,n+1):
    N = int(file[j].strip()) 
    if N == 0:
        file_out.write('Case #%i: %s\n'%(j,'INSOMNIA')) 
    else:
        all_ints = range(0,10)
        counting_ints = set([int(i) for i in str(N)])
        count = 1
        while set(all_ints) != set(counting_ints):
            count+=1
            if count>1000000:
                Nnew = 'INSOMNIA'
                break
            Nnew = count*N
            counting_ints.update([int(i) for i in str(Nnew)])
        if count ==1:
            file_out.write('Case #%i: %i\n'%(j,N))        
        else:
            file_out.write('Case #%i: %s\n'%(j,str(Nnew)))