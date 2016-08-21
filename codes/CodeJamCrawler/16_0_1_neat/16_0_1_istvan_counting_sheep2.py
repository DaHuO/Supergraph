# Counting Sheep
# CodeJam 2016
# Istvan Szabo

digits=set(['0','1','2','3','4','5','6', '7', '8' ,'9'  ])
f=open("A-large.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append(int(line))

T=int(input_lines2[0])
g = open("output.out", 'w')

for i in range(T):
    N=input_lines2[i+1]
    if N==0:
        g.write('Case #'+str(i+1)+': '+'INSOMNIA'+'\n')
    else:
        used=set()
        for s in str(N):
            used.add(s)
        M=N
        while used!=digits:
            M=M+N
            for s in str(M):
                used.add(s)
        g.write('Case #'+str(i+1)+': '+str(M)+'\n')
g.close()