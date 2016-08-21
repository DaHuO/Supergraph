fid = open('input.txt')
T = fid.readline().strip()
fout = open('output.txt','w')

#This should return a string, to deal with INSOMNIA output
def steps(N):
    #The only way to get insomnia is with 0
    if N==0:
        return "INSOMNIA"
    i = 1
    score = [0]*10
    while sum(score)<10:
        for d in str(i*N):
            score[int(d)] = 1
        i = i + 1
    return str((i-1)*N)



for i,line in enumerate(fid):
    line = line.strip()
    if len(line)==0:
        continue
    N = int(line)
    out = steps(N)
    fout.write('Case #%d: %s\n' % (i+1, out))
